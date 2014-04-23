from django.db import models
from django.db.models import Q
import datetime

# Create your models here.


class User(models.Model):
    username = models.CharField(unique=True, max_length=128)
    name = models.CharField(unique=True, max_length=128)
    wb_id = models.IntegerField(unique=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username

    def get_locations(self):
        return UserLocation.objects.filter(user=self).order_by('-create_date')

    def get_latest_location(self):
        return get_locations()[0] or None

    def get_follows(self):
        return [f.user1 if not f.user1==self else f.user2 for f in Follow.objects.filter(Q(user1=self) | Q(user2=self))]


class UserLocation(models.Model):
    user = models.ForeignKey(User, related_name='owner')
    lon = models.FloatField()
    lat = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.name + " " + self.get_location()

    def get_location(self):
        return {'lon':self.lon, 'lat':self.lat}


class Follow(models.Model):
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')

    def __unicode__(self):
        return self.user1.name + "<->" + self.user2.name


class Service(models.Model):
    name = models.CharField(max_length=15)    #  Type of Service "police, ambulance, fire brigade"
    lon = models.FloatField()
    lat = models.FloatField()
    join_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name + " " + self.get_location()

    def get_location(self):
        return {'lon':self.lon, 'lat':self.lat}
