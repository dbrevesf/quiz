from django.shortcuts import get_object_or_404, render
from .models import Quiz

def list_quiz(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quizcreator/index.html', {'quiz_list': quiz_list})

def quiz_detail(request, quiz_id):
    
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quizcreator/quiz_detail.html', {'quiz': quiz})
