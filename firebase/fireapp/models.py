from django.db import models
import uuid 
from uuid import uuid4

class ParkingSpot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    spot_number = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.spot_number

class Reservation(models.Model):
    user_name = models.CharField(max_length=100)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.parking_spot}'
