from django.db import models


class POIType(models.Model):
    name = models.CharField(max_length=200)
    icon = models.TextField()
    display = models.IntegerField()
    special_fields = models.BooleanField()

    def __str__(self):
        return self.name


class POI(models.Model):
    name = models.CharField(max_length=200)
    special_icon = models.BooleanField()
