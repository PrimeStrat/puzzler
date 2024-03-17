from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse("test")

def generate_question(request):
    response = requests.get('https://opentdb.com/api.php?amount=1')
    data = response.json()
    question = data['results'][0]['question']
    return render(request, 'puzzler/puzzle_app/templates/init.html', {'question': question})
