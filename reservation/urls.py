from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rule', views.rule, name='rule'),
    path('inquire', views.inquire, name='inquire'),
    path('inquireList', views.inquireList, name='inquireList'),
    path('cancelSucess', views.cancelSucess, name='cancelSucess'),    
    path('mail', views.mail, name='mail'),
    path('calendar', views.calendar, name='calendar'),
    path('confirmForm', views.confirmForm, name='confirmForm'),
    path('confirm', views.confirm, name='confirm'),
    path('bookinglist', views.bookingList, name='bookingList'),
]