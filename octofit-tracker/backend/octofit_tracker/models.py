from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50)
    members = models.JSONField()

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)
    schedule = models.CharField(max_length=100, null=True, blank=True)
    max_attendance = models.IntegerField(null=True, blank=True)

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()

class Workout(models.Model):
    user = models.CharField(max_length=100)
    workout = models.CharField(max_length=100)
    reps = models.IntegerField(null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
