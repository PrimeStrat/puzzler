from django.shortcuts import render
from django.http import HttpResponse
import requests
import random

def index(request):
    return HttpResponse("test")

def generate_question(request):
    # Loop until a question is found
    question = 'reload'
    answers = []
    while(question == 'reload'):
        response = requests.get('https://opentdb.com/api.php?amount=1')
        data = response.json()

        correct_answer = ""
        if 'results' in data and data['results']:
            question = data['results'][0].get('question', 'good')
            correct_answer = data['results'][0].get('correct_answer')
            answers.append(correct_answer)
            incorrect_answers = data['results'][0].get('incorrect_answers')
            answers.extend(incorrect_answers)
        else:
            question = 'reload'
    
    # Char replace
    question = question.replace("&quot;", "\"")
    question = question.replace("&#039;", "\'")
    question = question.replace("&ouml;", "\'")
    for answer in answers:
        answer = answer .replace("&quot;", "\"")
        answer = answer .replace("&#039;", "\'")
        answer = answer .replace("&ouml;", "\'")

    # Shuffle Answers
    random.shuffle(answers)

    # Render the template with question and answers
    if(len(answers) == 2):
        return render(request, 'init.html', {'correctanswer': correct_answer, 'question': question, 'answer1': answers[0], 'answer2': answers[1]})
    elif(len(answers) == 3):
        return render(request, 'init.html', {'correctanswer': correct_answer, 'question': question, 'answer1': answers[0], 'answer2': answers[1], 'answer3': answers[2]})
    elif(len(answers) == 4):
        return render(request, 'init.html', {'correctanswer': correct_answer, 'question': question, 'answer1': answers[0], 'answer2': answers[1], 'answer3': answers[2], 'answer4': answers[3]})

def answer(request):
    if request.method == 'POST':
        correct_answer = request.POST.get('correctanswer')
        user_answer = request.POST.get('user_answer')
        is_correct = "Incorrect"
        if user_answer == correct_answer:
            is_correct = "Correct"
        return render(request, 'answer.html', {'correct_answer': correct_answer, 'user_answer': user_answer, 'is_correct': is_correct})
    else:
        return HttpResponse("Method Not Allowed", status=405)
    
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/edit.html', {'form': form})