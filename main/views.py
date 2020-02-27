from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# Create your views here.
def home(request):
    return render(request, "main/index.html")


def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "main/posts.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'main/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



