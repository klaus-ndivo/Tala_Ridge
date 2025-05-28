from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
import json

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
            subject=f"Contact Us Message from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email="noreply@talaridge.com",
            recipient_list=["charlesndivo847@gmail.com"],  # Change to your admin email
            fail_silently=False,
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'ok'})
        return render(request, 'home.html', {'contact_success': True})
    return render(request, 'home.html')

def gardens(request):
    return render(request, 'gardens.html')

def accomodation(request):
    return render(request, 'accomodation.html')

def restaurant(request):
    return render(request, 'restaurant.html')

def swimming(request):
    return render(request, 'swimming.html')

def bar(request):
    return render(request, 'bar.html')

def conferencing(request):
    return render(request, 'conferencing.html')

def contacts(request):
    return render(request, 'contactsr.html')

@csrf_exempt
def book(request):
    if request.method == 'POST':
        # Use request.POST for form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        room_type = request.POST.get('room_type')
        message = request.POST.get('message')
        # Send notification email
        send_mail(
            subject="New Booking Received",
            message=f"Booking details:\nName: {name}\nEmail: {email}\nRoom Type: {room_type}\nMessage: {message}",
            from_email="noreply@talaridge.com",
            recipient_list=["charlesndivo847@gmail.com"],  # Change to your admin email
            fail_silently=False,
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid request'}, status=400)