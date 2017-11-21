from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Depart(models.Model):
    doctor = models.ForeignKey(User)
    nurse = models.CharField(max_length=10)
    number = models.IntegerField(max_length=5)
    title = models.CharField(max_length=10)
    meddate = models.DateTimeField(blank=True, null=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title