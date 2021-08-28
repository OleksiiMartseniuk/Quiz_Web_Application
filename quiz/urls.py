from django.urls import path
from .views import QuizView, DetailView, ResultView, LoginView, RegistrationView, logout_view
urlpatterns = [
    path('', QuizView.as_view(), name='home'),
    path('detail/<str:name>/', DetailView.as_view(), name='detail'),
    path('result/', ResultView.as_view(), name='result'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout_view, name='logout'),
]
