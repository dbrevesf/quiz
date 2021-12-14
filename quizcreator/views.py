from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from quizcreator.forms import QuestionForm, QuizForm
from .models import Quiz

def list_quiz(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quizcreator/index.html', {'quiz_list': quiz_list})


def quiz_detail(request, quiz_id):
    context = {}
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    context['quiz'] = quiz
    context['questions'] = questions
    print(context)
    return render(request, 'quizcreator/quiz_detail.html', context)


def create_quiz(request):
    context = {}
    if 'name' in request.POST.keys():
        quiz_name = request.POST['name']
        quiz = Quiz(name=quiz_name)
        quiz.save()
        context = {}
        context['quiz_id'] = quiz.id
        context['quantity'] = request.POST['quantity']
        return create_quiz_step_2(request, context)
    context['quiz_form'] = QuizForm(request.POST or None)
    return render(request, 'quizcreator/create_quiz.html', context)


def create_quiz_step_2(request, context=None):
    print(request.POST)
    quiz = None
    if context == None:
        context = {}
    if 'content' and 'time_to_expire' in request.POST:
        contents = request.POST['content']
        times = request.POST['time_to_expire']
        quiz = Quiz.objects.filter(id=request.POST['quiz_id'])[0]
        for content, expire in zip(contents, times):
            quiz.question_set.create(content=content, time_to_expire=expire)
            quiz.save()
        return HttpResponseRedirect('/')
    context['question_form'] = QuestionForm(request.POST or None)
    return render(request, 'quizcreator/create_quiz_step_2.html', context)
