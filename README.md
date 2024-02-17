# VoluConnect

## Developer Guide

### Installation
1. Install pip, if haven’t  
   `sudo apt install python3-pip -y`
2. Install Django, if haven’t  
   `sudo apt install python3-django`
3. Pip Install the relevant packages for the web app as such  
  `pip install -r /path/to/requirements.txt`
4. To run the program on localhost, enter the following command  
   `sudo python3 manage.py runserver `

## Admin Guide
### Custom Form Generator and Management
1. Login into the Django Admin Dashboard 127.0.0.1:8000/admin.
2. Click on the "Add" option on the Forms row.
3. Fill in neccessary information and set Owner to root.
4. Click "save" and remember the number assigned to the form.
5. To remove a form, click on the box beside the form name.
6. Change the action to "Delete selected events".
7. Click "Go" to remove the event.

### Event Management System
1. Click on the "Add" option under Events row.
2. Fill in neccessary information and ensure the number filled in is the number assigned to the form
3. Click "save" and the form will appear on the webpage.
4. To remove an event, click on the box beside the event name.
5. Change the action to "Delete selected events".
6. Click "Go" to remove the event.

### Qr Code Attendance Taking System
1. Login into the VoluConnect Admin Dashboard 127.0.0.1:8000/admin.
2. Click on the "Add" option on the Event qrcodes row.
3. Fill in neccessary information.
4. Download QRcode to be scanned by volunteers at the start and end of every project to track their attendance.
5. For there are any discrepencies, admin can manually override the attendance by clicking the "Attendances" button.
6. Select the attendance to change.
7. Make the changes and click "Save".

### Export PDF
1. Login into the VoluConnect Admin Dashboard 127.0.0.1:8000/admin.
2. Click on the "Attendances" button.
3. Change the action to either "Export questions" or "Export responses".
4. Select the form name and click "Go".
