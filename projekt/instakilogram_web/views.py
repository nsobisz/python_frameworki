from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm, LoginForm, EditForm
from instakilogram_web.models import Post, Insta_users


def user_profile(request, username):
    user = get_object_or_404(Insta_users, username=username)
    title_page = "Instakilogram"

    if request.method == 'POST':
        user.delete()
        return redirect('login')


    posts = Post.objects.filter(author = username)
    return render(
        request,
        'profile.html',
        {
            'title': title_page,
            'posts': posts,
            'user': user}
    )

def user_edit(request, username):
    user = get_object_or_404(Insta_users, username=username)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(reverse('user_profile', kwargs={'username': username}))
    else:
        form = EditForm(instance=user)

    return render(
        request,
        'edit.html',
        {
            'form': form,
            'user': user}
    )


def testORM(response):
    query = None
    return HttpResponse(query)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Insta_users.objects.filter(username=username, password=password)

            if len(user) != 0:

                return redirect( reverse('user_profile', kwargs={'username': username}))
            else:

                form.add_error(None, 'Nieprawidłowa nazwa użytkownika lub hasło.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})