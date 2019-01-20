from django.db import models
from django.utils import timezone


class Link(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    taglist = models.CharField(max_length=1000)
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.created_date
        self.save()

    def __str__(self):
        return self.title
