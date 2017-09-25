from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    theme = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    timestamp = models.DateField()
    image = models.ImageField(upload_to='events', blank=True, null=True)


class Speaker(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    date = models.DateField()
    about = models.TextField()
    facebook = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    twitter = models.URLField(null=True)
    profile_pic = models.ImageField(upload_to='speakers', null=True, blank=True)


class Organizer(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    facebook = models.URLField(default="https://www.facebook.com/")
    linkedin = models.URLField(default="https://www.linkedin.com/")
    profile_pic = models.ImageField(upload_to='speakers')
    # twitter = models.URLField(default="https://www.twitter.com/")


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    image = models.ImageField(upload_to='sponsors', null=True, blank=True)
