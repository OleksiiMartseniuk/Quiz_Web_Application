from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    ### изменить
    url = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    desc = models.CharField(max_length=500)
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.name)
        super().save(*args, **kwargs)

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'question: {self.question.content}, answer: {self.content}, correct: {self.correct}'


class Marks_Of_User(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    percentage = models.FloatField()
    time = models.IntegerField(help_text="lead time", default="1")
    data = models.DateTimeField(auto_now_add=True)
    ### изменить
    correct = models.IntegerField(blank=True, null=True)
    incorrect = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{str(self.quiz)} ({self.user.username})'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
