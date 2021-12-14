from django.db import models

class Quiz(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class Question(models.Model):

    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    time_to_expire = models.IntegerField(default=180)

    def __str__(self) -> str:
        return f"{self.id}: {self.content}"


class Response(models.Model):

    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f"{self.id}: {self.content}"


