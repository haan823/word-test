from django.shortcuts import render, redirect
from django.urls import reverse
from .word import kor, eng

def get_quiz(request):
    # localhost:8000/word2?index=0&correct=0
    if request.method == 'GET':
        index = int(request.GET.get('index', 0))
        correct = int(request.GET.get('correct', 0))

        action = ""
        if index == 4:
            action += reverse('result')

        context = {
            "index": index,
            "quiz": eng[index],
            "action": action,
            "correct": correct
        }
        return render(request, 'word2/index.html', context)

    if request.method == 'POST':
        index = int(request.POST.get('index'))
        before_correct = int(request.POST.get('correct'))
        answer = request.POST.get('answer')

        correct = before_correct

        if answer == kor[index]:
            correct += 1

        if(int(index)<4):
            next_url = 'quiz'
        else:
            next_url = 'result'

        # next_url = 'quiz' if int(index) < 4 else 'result'

        # localhost:8000/word2/?index={}&correct={}
        # localhost:8000/word2/result?index={}&correct={}

        return redirect(
            reverse(next_url) +
            '?index={index}&correct={correct}'
            .format(index=index + 1, correct=correct)
        )

def get_result(request):
    if request.method == 'POST':
        correct = int(request.POST.get('correct'))
        index = int(request.POST.get('index'))
        answer = request.POST.get('answer')

        result = correct
        if answer == kor[index]:
            result += 1

        context = {
            "correct": result,
            "wrong": 5-result
        }
        return render(request, 'word2/result.html', context)