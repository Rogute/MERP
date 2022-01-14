from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    thumbnail = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    e_mail = models.EmailField(max_length=128)
    reservation_code = models.CharField(max_length=30, unique=True)