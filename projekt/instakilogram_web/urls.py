from django.urls import path
from instakilogram_web.views import test_response, user_profile, login, testORM

urlpatterns = [
    path('test/', test_response),
    path('profile/<username>/', user_profile, name='user_profile'),
    path('login/', login),
]