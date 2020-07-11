from django.db import models


# Create your models here.


class Operating_system(models.Model):
    operating_system = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.operating_system


class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True)
    IP_address = models.CharField(max_length=30, blank=True)
    MAC_address = models.CharField(max_length=30, blank=True)
    operating_system = models.ManyToManyField(Operating_system)
    users_name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    Installation_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    objects = models.Manager()

    def __unicode__(self):
        return self.computer_name
