from django.shortcuts import render
from django.http import JsonResponse
from .  import data as data_sports
from django.core.mail import send_mail
import json
from django.conf.urls.static import static 
from django.conf import settings
import os
# Create your views here.


"""
ENDPOINTS FOR retrieving DATA 
"""
# SPORTS
def sport_events(requests,):
    """
    Sends complete details of all the sporting events
    """
    return JsonResponse(data_sports.sports_data)

def sport_events_details(requests, sport):
    """
    View to handle the sports details page
    """
    return JsonResponse(data_sports.sports_data[sport])

# CULTURAL
def cultural_events(requests,):
    """
    Sends complete details of all the cultural events
    """
    # Open and read the JSON file
    with open("static\json\cultural.json", 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def cultural_events_details(requests, events):
    """
    Sends complete details of all the cultural events
    """
    # Open and read the JSON file
    with open("static\json\cultural.json", 'r') as file:
        data = json.load(file)

    return JsonResponse(data[events])




"""
REGISTERATION AND ALL KINDS OF FORM SUBMISSION 
"""
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


"""
SENDING EMAILS AND OTHER UPDATES
"""
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

