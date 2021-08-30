from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Answer, Quiz, Marks_Of_User, Rating
from .forms import LoginForm, RegistrationForms
from django.contrib.auth import authenticate, login, logout


class QuizView(View):

    def get(self, request):
        quiz = Quiz.objects.all()
        return render(request, 'quiz/home.html', {'quiz': quiz})


class DetailView(View):
    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        name_quiz = kwargs.get('name')
        quiz = Quiz.objects.get(name=name_quiz)
        return render(request, 'quiz/detail.html', {'quiz': quiz})

    def post(self, request, **kwargs):
        correct = 0
        name_quiz = kwargs.get('name')
        quiz = Quiz.objects.get(name=name_quiz)
        for count in quiz.get_questions():
            rez = Answer.objects.get(content=request.POST.get(f'{count}'), question=count)
            if rez.correct:
                correct += 1
        percentage = (correct / quiz.number_of_questions) * 100
        timer = quiz.time - int(request.POST.get('timer'))
        incorrect = quiz.number_of_questions - correct
        if not Marks_Of_User.objects.filter(quiz=quiz, user=request.user).exists():
            if Rating.objects.filter(user=request.user).exists():
                rating = Rating.objects.get(user=request.user)
                rating.rating = rating.rating + (percentage*10)
                rating.save()
            else:
                Rating.objects.create(
                    user=request.user,
                    rating=percentage*10
                )
        Marks_Of_User.objects.create(quiz=quiz,
                                     user=request.user,
                                     score=(percentage*10),
                                     percentage=percentage,
                                     time=timer,
                                     correct=correct,
                                     incorrect=incorrect)
        return redirect('result')


class ResultView(View):
    def get(self, request, *args, **kwargs):
        marks_of_user = Marks_Of_User.objects.latest('data')
        quiz = Quiz.objects.get(name=marks_of_user.quiz.name)
        context = {
            'marks_of_user': marks_of_user,
            'quiz': quiz
        }
        return render(request, 'quiz/result.html', context)


class LoginView(View):

    def get(self, request):
        form = LoginForm(request.POST or None)
        return render(request, 'quiz/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'quiz/login.html', {'form': form})


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForms(request.POST or None)
        return render(request, 'quiz/registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForms(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            rating = Rating.objects.create(user=request.user)
            rating.save()
            return redirect('home')
        return render(request, 'quiz/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


class ProfileView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        marks_of_user = Marks_Of_User.objects.filter(user=request.user)
        rating = Rating.objects.create(user=request.user)
        context = {
            'marks_of_user': marks_of_user,
            'rating': rating
        }
        return render(request, 'quiz/profile.html', context)


class DeleteView(View):

    def get(self, request, **kwargs):
        marks_of_user_id = kwargs.get('pk')
        marks_of_user = Marks_Of_User.objects.get(id=marks_of_user_id)
        marks_of_user.delete()
        return redirect('profile')


class ClearView(View):

    def get(self, request, **kwargs):
        rating = Rating.objects.get(user=request.user)
        marks_of_user = Marks_Of_User.objects.filter(user=request.user)
        for obj in marks_of_user:
            obj.delete()
        rating.rating = 0
        rating.save()
        return redirect('profile')


class RatingView(View):

    def get(self, request):
        rating = Rating.objects.order_by('-rating')
        print(rating)
        return render(request, 'quiz/rating.html', {'rating': rating})

