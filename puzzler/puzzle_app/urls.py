from django.urls import path

from . import views

urlpatterns = [
    path('question/', views.generate_question, name='generate_question'),
    path('answer/', views.answer, name='answer'),
]