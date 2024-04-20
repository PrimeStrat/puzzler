from django.urls import path

from . import views
from .views import edit_profile

urlpatterns = [
    path('question/', views.generate_question, name='generate_question'),
    path('answer/', views.answer, name='answer'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]