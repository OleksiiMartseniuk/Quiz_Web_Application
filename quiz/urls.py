from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuizView.as_view(), name='home'),
    path('detail/<str:name>/', views.DetailView.as_view(), name='detail'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('clear/', views.ClearView.as_view(), name='clear'),
    path('rating/', views.RatingView.as_view(), name='rating'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout/', views.logout_view, name='logout'),
]
