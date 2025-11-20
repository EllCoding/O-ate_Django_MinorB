from django.db import models
from django.contrib.auth.models import User
from pets.models import Pet
from django_google_maps.fields import AddressField, GeoLocationField

class Report(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('resolved', 'Resolved'),
        ('invalid', 'Invalid'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='reports')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.name} - {self.status}"

class locationReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='locations')
    location = AddressField()
    geolocation = GeoLocationField(blank=False, null=False, default='0,0')

    def __str__(self):
        return f"Location for {self.report.pet.name} report"
        
# The geolocation field will store latitude and longitude in the format 'lat,lng' or GPS coordinates.
# https://www.gps-coordinates.net/my-location