from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    edited_by_blog = models.BooleanField(default=False)
    pic = models.FileField(upload_to='uploads/')
    edited_by_clock = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title