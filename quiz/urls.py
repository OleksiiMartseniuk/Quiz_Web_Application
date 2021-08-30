from django.urls import path
from .views import QuizView, DetailView, ResultView, LoginView, RegistrationView, logout_view, ProfileView, DeleteView, RatingView, ClearView
urlpatterns = [
    path('', QuizView.as_view(), name='home'),
    path('detail/<str:name>/', DetailView.as_view(), name='detail'),
    path('result/', ResultView.as_view(), name='result'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('clear/', ClearView.as_view(), name='clear'),
    path('rating/', RatingView.as_view(), name='rating'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout_view, name='logout'),
]
