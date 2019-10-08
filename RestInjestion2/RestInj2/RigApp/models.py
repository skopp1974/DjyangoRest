from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rig(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    rig_location = models.CharField(max_length=50)
    well_bore_diameter = models.CharField(max_length=50, default=None, blank=True)
    well_name = models.CharField(max_length=50, default=None, blank=True)
    well_location = models.CharField(max_length=50, default=None, blank=True)
    well_diameter = models.PositiveIntegerField(default=None, blank=True)
    well_depth = models.PositiveIntegerField(default=None, blank=True)
    raw_data_file = models.CharField(max_length=500)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
# class Rig(models.Model):
#     title = models.CharField(max_length=50)
#     location = models.CharField(max_length=50, default=None, blank=True)
#     author = models.CharField(max_length=500) #ForeignKey('auth.User')
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     modified_at = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return self.well_name
