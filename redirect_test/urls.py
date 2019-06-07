from . import views
from django.urls import path

app_name = 'redirect_test'
urlpatterns = [
    path('redirect', views.simple_form, name='form'),
]
