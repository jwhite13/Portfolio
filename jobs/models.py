from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=30)
    course = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=30, null=True)
    year = models.CharField(max_length=4, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    summary = models.CharField(max_length=200)
    long_summary = models.CharField(max_length=500)
    cover_photo = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title