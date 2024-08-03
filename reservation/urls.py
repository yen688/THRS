from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rule', views.rule, name='rule'),
    path('calendar', views.calendar, name='calendar'),
    path('confirmForm/<str:date>', views.confirmForm, name='confirmReservation'),
    path('confirm', views.confirm, name='confirm'),
    path('bookinglist', views.bookingList, name='bookingList'),
]