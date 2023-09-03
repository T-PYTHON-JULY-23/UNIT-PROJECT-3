from django.shortcuts import render, redirect
from .models import Post,Comment,User
from .forms import PostForm
from django.http import HttpRequest, HttpResponse

def Gallery(request: HttpRequest):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('MyPersonalPage:MyProjects')  # Redirect to the posts page after successful submission
    else:
        form = PostForm()
    return render(request, 'MyPersonalPage/Gallery.html', {'form': form})



def MyProjects(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'MyPersonalPage/MyProjects.html', {'form': posts})


def MyCV(request: HttpRequest):

    posts = Post.objects.all()
    return render(request, 'MyPersonalPage/MyCV.html', {'form': posts})