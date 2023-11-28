from django.urls import path
from instakilogram_web.views import user_profile, login, register, user_edit

urlpatterns = [

    path('profile/<username>/', user_profile, name='user_profile'),
    path('edit/<username>/', user_edit, name='user_edit'),
    path('login/', login, name="login"),
    path('register/', register, name = "register"),
]