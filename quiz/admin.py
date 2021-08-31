from django.contrib import admin
from .models import Quiz, Question, Answer, Marks_Of_User, Rating


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Marks_Of_User)
admin.site.register(Rating)

