from django.urls import path
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sign-up/', views.sign_up, name="sign-up"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name="profile")
]


