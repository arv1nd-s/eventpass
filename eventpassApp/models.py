from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    address = models.TextField()
    pincode = models.IntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to="event-images")
    ticket_price = models.IntegerField()

class Booking(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)