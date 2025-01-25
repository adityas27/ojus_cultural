from django.shortcuts import render
from django.http import JsonResponse
from .  import data as data
from django.core.mail import send_mail
import json
# Create your views here.
def events_all(requests,):
    """
    Sends complete details of all the events happening
    """
    return JsonResponse(data.sports_data)

def event_details(requests, sport):
    """
    View to handle the event details page
    """
    return JsonResponse(data.sports_data[sport])

def register(requests):
    pass

def send_emails(request, recievers, content):
    """
    Endpoint to send emails
    --> Sending post request to this view whenever mail is to be sent
    Note this won't automatically send email
    Signals would be better choice for sending conformation mail after registeration 
    """
    # email credentials
    subject="Email Verification"
    message = f"""{content}"""

    sender = "" # sender's email
    receiver = recievers

    # send email
    send_mail(
    subject,
    message,
    sender,
    receiver,
    fail_silently=False,)

def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON body
            name = data.get('name')  # Example form field
            email = data.get('email')  # Example form field

            # Process the data (e.g., save to the database, send an email, etc.)
            return JsonResponse({'message': f"Received name: {name}, email: {email}"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)