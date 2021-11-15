from django.urls import path
from . import views

urlpatterns = [
   path('', views.main, name='main'),
   path('main', views.main, name='main'),
   path('register', views.register, name='register'),
   path('space/<str:id>', views.space, name='space'),
   path('space/book/<str:id>', views.book, name='book'),
   path('booking_list', views.booker_booking_list, name='booker_booking_list'),
]
