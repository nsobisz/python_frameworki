from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from instakilogram_web.models import Post, Insta_users


def test_response(request):
    return HttpResponse("To jest przykład url")


def user_profile(request, username):
    user = get_object_or_404(Insta_users, username=username)
    title_page = "Instakilogram"
    posts = Post.objects.filter(author = username)
    return render(
        request,
        'profile.html',
        {
            'title': title_page,
            'posts': posts,
            'user': user}
    )

def login(request):

    title_page = "Instakilogram"

    return render(
        request,
        'login.html',
        {
            'title': title_page,

           }
    )

def testORM(response):
    query = Post.objects.all()
    return HttpResponse(query)

