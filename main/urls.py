from django.urls import path
from main import views
from main.views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', views.home, name="home_view"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('posts/new/', PostCreateView.as_view(), name="post-create"),
]
