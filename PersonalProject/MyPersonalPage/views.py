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


def AiChatBot(request: HttpRequest):

    posts = Post.objects.all()
    return render(request, 'MyPersonalPage/AIchatbot.html', {'form': posts})



def GenderClassification(request: HttpRequest):

    posts = Post.objects.all()
    return render(request, 'MyPersonalPage/GenderClass.html', {'form': posts})

def photos(request: HttpRequest):
    photo = Post.objects.all()
    return render(request, 'MyPersonalPage/photos.html', {'form': photo})

def videos(request: HttpRequest):
    video = Post.objects.all()
    return render(request, 'MyPersonalPage/videos.html', {'form': video})