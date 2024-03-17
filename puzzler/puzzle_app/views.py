from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse("test")

def generate_question(request):
    response = requests.get('https://opentdb.com/api.php?amount=1')
    data = response.json()

    if 'results' in data and data['results']:
        question = data['results'][0].get('question', 'Question not available')
    else:
        question = 'Question not available'
    
    dir = 'init.html'

    return render(request, dir, {'question': question})
