from django.urls import path
from . import views


app_name = 'quizcreator'
urlpatterns = [
    path('', views.list_quiz, name='index'),
    path('<int:quiz_id>/', views.quiz_detail, name='detail'),
    path('create/', views.create_quiz, name='create'),
    path('create_quiz_step_2/', views.create_quiz_step_2, name='create_quiz_step_2'),
]