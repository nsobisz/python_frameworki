from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from instakilogram_web.models import Post, Insta_users


def test_response(request):
    return HttpResponse("To jest przykład url")


def user_profile(request, username):
    user = get_object_or_404(Insta_users, username=username)
    title_page = "To jest tytuł strony"
    options = [
        "option 1",
        "option 2",
        "option 3"
    ]

    posts = Post.objects.filter(author = username)
    return render(
        request,
        'profile.html',
        {
            'title': title_page,
            'options': options,
            'posts': posts,
            'user': user}
    )
