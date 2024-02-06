from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EventForm
from .models import Event
from django.core.paginator import Paginator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

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
    return render(request, "courses.html", {})

def cards(request):
    return render(request, "cards.html", {})

def children(request):
    return render(request, "children.html", {})

def gardening(request):
    return render(request, "gardening.html", {})

def labour(request):
    return render(request, "labour.html", {})

def painting(request):
    return render(request, "painting.html", {})

def rations(request):
    return render(request, "rations.html", {})

def elements(request):
    return render(request, "elements.html", {})

def login(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "register.html", {})

def dashboard(request):
    return render(request, "dashboard.html", {})

def attendance(request):
    return render(request, "attendance.html", {})

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

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
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