from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gardens/', views.gardens, name='gardens'),
    path('accomodation/', views.accomodation, name='accomodation'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('swimming/', views.swimming, name='swimming'), # <-- Add this line
    path('bar/', views.bar, name='bar'), # <-- Add this line
    path('conferencing/', views.conferencing, name='conferencing'), # <-- Add this line
    path('contacts/', views.contacts, name='contactsr'), # <-- Add this line
    path('book/', views.book, name='book'), # <-- Add this line

    # ...other patterns...
]
