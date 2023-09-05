from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Comment



def intro_view(request: HttpRequest):

    return render(request, "main/home.html")


def service_view(request: HttpRequest):

    return render(request, "main/service.html")


def work_view(request: HttpRequest):

    return render(request, "main/work.html")

def about_view(request: HttpRequest):

    return render(request, "main/about.html")

def work_view(request: HttpRequest):

    return render(request, "main/work.html")

def review_view(request: HttpRequest):

    return render(request, "main/review.html")

def blog_view(request: HttpRequest):

    return render(request, "main/blog.html")

def contact_view(request: HttpRequest):
    comments = Comment.objects.all()
    if request.method == "POST" and request.user.is_staff:
        new_comment = Comment(user=request.user,subject=request.POST["subject"], message=request.POST["message"])
        new_comment.save()

    return render(request, "main/contact.html",{ "comments" : comments, "Comment" : Comment})
def message_view(request: HttpRequest):
     
     comments = Comment.objects.all()

     return render(request, "services/.html", { "comments" : comments, "Comment" : Comment})
