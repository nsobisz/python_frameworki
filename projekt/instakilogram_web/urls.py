from django.urls import path
from instakilogram_web.views import test_response, user_profile

urlpatterns = [
    path('test/', test_response),
    path('profile/<username>/', user_profile, name='user_profile'),
]