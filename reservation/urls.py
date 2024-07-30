from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rule', views.rule, name='rule'),
    path('confirmForm', views.confirmForm, name='confirmReservation'),
    path('confirm', views.confirm, name='confirm'),
]