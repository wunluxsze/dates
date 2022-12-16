from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from engine.models import *
from engine.forms import *

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', context={'posts': posts})


def create(request):
    initialize()
    postform = PostForm()
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('home')
    else:
        return render(request, 'create.html', {'form': postform})


def edit(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponseNotFound('<h1>Post is not found</h1>')
    postform = PostForm()
    if request.method == "POST":
        postform = PostForm(request.POST, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('home')
    else:
        return render(request, 'edit.html', {'form': postform})


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('home')
    except:
        return HttpResponseNotFound('<h1>Post is not found</h1>')


def initialize():
    if Author.objects.all().count() == 0:
        Author.objects.create(name='Толстой')
        Author.objects.create(name='Гоголь')
        Author.objects.create(name='Пушкин')

    if Publisher.objects.all().count() == 0:
        Publisher.objects.create(name='Война и мир')
        Publisher.objects.create(name='Вий')
        Publisher.objects.create(name='Три Богатыря')

    if Category.objects.all().count() == 0:
        Category.objects.create(name='Для детей')
        Category.objects.create(name='Для взрослых')
        Category.objects.create(name='Для старых')