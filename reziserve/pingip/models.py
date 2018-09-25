from __future__ import unicode_literals

from django.db import models

# Create your models here.
class serversm3(models.Model):
    IP = models.CharField(max_length=50)
    Domain = models.CharField(max_length=50)

class m3servers(models.Model):
    IP = models.CharField(max_length=50)
    Domain = models.CharField(max_length=150)
    Hostname = models.CharField(max_length=150)
    Location = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    Division = models.CharField(max_length=50)
    Region = models.CharField(max_length=50)

class states(models.Model):
    Name = models.CharField(max_length=50)
    Abbr = models.CharField(max_length=50)

class teak(models.Model):
    IP = models.CharField(max_length=50)
    Domain = models.CharField(max_length=150)
    Hostname = models.CharField(max_length=150)
    Location = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    Division = models.CharField(max_length=50)
    Region = models.CharField(max_length=50)

class cgw(models.Model):
    IP = models.CharField(max_length=50)
    Domain = models.CharField(max_length=150)
    Hostname = models.CharField(max_length=150)
    Location = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    Division = models.CharField(max_length=50)
    Region = models.CharField(max_length=50)