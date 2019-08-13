from django.db import models


# Create your models here.
class News(models.Model):
    by = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    points = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    sentiment = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "newapp"

    def __str__(self):
        return self.title
