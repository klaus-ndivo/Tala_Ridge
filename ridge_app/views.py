from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gardens(request):
    return render(request, 'gardens.html')

def accomodation(request):
    return render(request, 'accomodation.html')