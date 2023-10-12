from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=1000, default="")
    year = models.PositiveSmallIntegerField(default=2023)
    upload = models.FileField(upload_to="uploads/", default="")
    def __str__(self):
        return self.title


