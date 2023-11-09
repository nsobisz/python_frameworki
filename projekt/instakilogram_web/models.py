

from django.db import models



# Create your models here.

class Insta_users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    imgThumb = models.ImageField(upload_to="media_img", null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=150,blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              blank=True)

    def __str__(self):
        return self.insta_username()

    def insta_username(self):
        return "{}".format(self.username)

class Post(models.Model):
    post_ID = models.AutoField(primary_key=True, editable=False)
    author = models.ForeignKey(Insta_users, on_delete=models.CASCADE)
    content = models.TextField(default="")
    date = models.DateField(auto_now_add=True)
    imgThumb = models.ImageField(upload_to="media_img", null=True, blank=True)

    def __str__(self):
        return self.id_with_date()

    def id_with_date(self):
        return "{} ({})".format(self.post_ID, self.date)


