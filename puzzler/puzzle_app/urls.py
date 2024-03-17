from django.urls import path

from . import views

urlpatterns = [
    path('', views.generate_question, name='generate_question'),
]