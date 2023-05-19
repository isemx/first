from django.db import models


# Create your models here.
class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=250)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return self.title
