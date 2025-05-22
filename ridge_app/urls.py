from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gardens/', views.gardens, name='gardens'),
    path('accomodation/', views.accomodation, name='accomodation'),  # <-- Add this line
    # ...other patterns...
]
