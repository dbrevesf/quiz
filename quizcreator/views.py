from django.shortcuts import get_object_or_404, render

from quizcreator.forms import QuestionForm, QuizForm
from .models import Quiz

def list_quiz(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quizcreator/index.html', {'quiz_list': quiz_list})

def quiz_detail(request, quiz_id):
    
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quizcreator/quiz_detail.html', {'quiz': quiz})

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


def create_quiz_step_2(request, context):

    context['question_form'] = QuestionForm(request.POST or None)
    return render(request, 'quizcreator/create_quiz_step_2.html', context)
