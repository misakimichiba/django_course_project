from django.shortcuts import render
from .models import User

# Create your views here.

def register(request):
  users = User.objects.all()
  return render(request, 'users/register.html', { 'users': users })

# def post_page(request, slug):
#   post = Post.objects.get(slug=slug)
#   return render(request, 'posts/post_page.html', { 'post': post })