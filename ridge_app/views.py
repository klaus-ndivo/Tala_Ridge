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
        data = json.loads(request.body)
        # Save booking to DB here if needed

        # Send notification email
        send_mail(
            subject="New Booking Received",
            message=f"Booking details:\nName: {data.get('name')}\nEmail: {data.get('email')}\nDate: {data.get('date')}\nGuests: {data.get('guests')}\nMessage: {data.get('message')}",
            from_email="noreply@talaridge.com",
            recipient_list=["charlesndivo847@gmail.com"],  # Change to your admin email
            fail_silently=False,
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid request'}, status=400)