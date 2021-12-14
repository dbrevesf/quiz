from django.urls import path
from . import views


app_name = 'quizcreator'
urlpatterns = [
    path('', views.list_quiz, name='index'),
    path('<int:quiz_id>/', views.quiz_detail, name='detail')
]