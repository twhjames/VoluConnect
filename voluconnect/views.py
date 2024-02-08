from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EventForm
from .models import Event, Attendance, VolunteerUser, EventQrcode
from django.core.paginator import Paginator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import qrcode, socket
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html", {})

def blog_details(request):
    return render(request, "blog_details.html", {})

def blog(request):
    return render(request, "blog.html", {})

def contact(request):
    return render(request, "contact.html", {})

def courses(request):
    events = Event.objects.all()
    return render(request, "courses.html", {'events': events})

def course_details(request, number):
    event = get_object_or_404(Event, number=number)
    return render(request, "course_details.html", {'event': event})

def form_response(request, number, title):
    event = get_object_or_404(Event, number=number)
    return render(request, "form_response.html", {'event': event, 'title': title})

def elements(request):
    return render(request, "elements.html", {})

def login(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "register.html", {})

def dashboard(request):
    return render(request, "dashboard.html", {})

def attendance(request):
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "attendance.html", {'page_obj' : page_obj})

def events(request):
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'events.html', {'page_obj' : page_obj})

def forms(request):
    return render(request, "forms.html", {})

def profile(request):
    return render(request, "profile.html", {})    

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "add_event.html", {'form':form, 'submitted':submitted})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect(reverse('events'))  
    return render(request, "events.html")

@require_http_methods(["GET", "POST"])
def edit_event(request, event_id=None):
    if request.method == 'GET':
        # Fetch event data and return as JSON
        event = get_object_or_404(Event, pk=event_id)
        return JsonResponse({'name': event.event_name, 'organisation': event.organisation, 'location': event.location, 'datetime': event.event_date, 'id': event.pk})

    if request.method == 'POST':
        # Handle event update
        event = get_object_or_404(Event, pk=request.POST.get('event_id'))
        event.event_name = request.POST.get('name')
        event.organisation = request.POST.get('organisation')
        event.location = request.POST.get('location')
        event.event_date = request.POST.get('datetime')
        # ... update other fields ...
        event.save()
        return JsonResponse({'status': 'success'})

def exportEventTablePDF(request):
    # Craft out the relevant search query & retrieve from database
    query = request.GET.get('search', '')
    if query:
        events = Event.objects.filter(event_name__icontains=query)
    else:
        events = Event.objects.all()

    # Create a HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="event_list.pdf"'

    # Create a PDF object, using the response object as its "file."
    buffer = SimpleDocTemplate(response, pagesize=letter)

    # Create a list to hold the PDF elements.
    elements = []

    # Define the table data and headers.
    data = [['Event', 'Organisation', 'Location', 'Date & Time']]  # Table headers
    data += [[item.event_name, item.organisation, item.location, item.event_date] for item in events]

    # Create a Table with the data.
    table = Table(data)

    # Add some style to the Table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ])
    table.setStyle(style)

    # Ensure each row size can accommodate the data
    row_heights = [30] * len(data)
    table.rowHeights = row_heights

    # Add the Table to the elements list.
    elements.append(table)

    # Build the PDF.
    buffer.build(elements)

    # Return the response.
    return response

def take_event_attendance(request, event_id):
    # Get the event object
    event = get_object_or_404(Event, pk=event_id)
    eventName = event.event_name

    # Get all the registered volunteers for this particular event
    volunteerList = Attendance.objects.filter(event = event)
    qrcodeImage = EventQrcode.objects.get(event = event).qr_image_url
    if not len(qrcodeImage.name) == 0:
        print("not empty")
        qrcodeImage = f"http://127.0.0.1:8000/static/media/EventID-{event_id}_qrcode.png"
    else:
        print("empty")
        qrcodeImage = ""
    volunteerList = volunteerList.select_related('user')

    # Create paginator
    paginator = Paginator(volunteerList, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # If no volunteers, inform admin with a pop-up msg
    if not volunteerList.exists():
        return HttpResponseRedirect('/attendance?infoMsg=EmptyVolunteerList')
    
    # Direct admin to take attendance for that event
    context = {
        'event_id' : event_id,
        'event_name' : eventName,
        'volunteer_list' : volunteerList,
        'page_obj': page_obj,
        'qr_image_url' : qrcodeImage,
    }
    return render(request, 'take_event_attendance.html', context)

def qrGenerator(request):
    if request.method == "GET":
        # Get the event object
        event_id = request.GET.get('event_id')
        event = get_object_or_404(Event, pk=event_id)

        # Get the ipV4 address of the server
        skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        skt.connect(("8.8.8.8", 80))
        ip = skt.getsockname()[0]

        # Create the take attendance link
        link = f"http://{ip}:8000/atsManagement/{event.pk}"

        # Function to generate and display a QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image file to model
        qrFilePath = settings.MEDIA_ROOT + f"EventID-{event_id}_qrcode.png"
        img.save(f"{qrFilePath}")
        m = EventQrcode.objects.get(event=event_id)
        m.qr_image_url = qrFilePath
        m.save()
        qrFilePath = f"http://127.0.0.1:8000/static/media/EventID-{event_id}_qrcode.png"
        return JsonResponse({'qrFilePath': qrFilePath})

def atsManagement(request, event_id):
    if request.method == "POST":
        try:
            userEmail = request.POST["user_email"]
            attendee = Attendance.objects.get(user_email=userEmail)
            takeAttendance(event_id, attendee.pk)
        except VolunteerUser.DoesNotExist:
            # User does not have a valid accounted
            return render(request, "attendance_login.html", {'loginStatus':'Failed'})

def takeAttendance(request, event_id, user_id):
    try:
        # Check if user is registed for this event & mark attendance
        attendee = Attendance.objects.get(event_id = event_id, user_id = user_id)
        if attendee.ats_status == 'ABSENT':
            attendee.ats_status = 'PRESENT'
            attendee.save()
            return render(request, "attendance_result.html", {'attendanceStatus':'Success'})
        else:
            return render(request, "attendance_result.html", {'attendanceStatus':'Taken'})
    except Attendance.DoesNotExist:
        # User did not register for this event
        return render(request, "attendance_result.html", {'attendanceStatus':'DoesNotExist'}) 

def attendance_login(request):
    return render(request, "attendance_login.html", {})

def attendance_result(request):
    return render(request, "attendance_result.html", {})