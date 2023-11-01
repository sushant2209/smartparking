from celery import shared_task
from datetime import datetime, timedelta
from .models import ParkingSpot

@shared_task
def remove_occupied_status(spot_id):
    spot = ParkingSpot.objects.get(spotid=spot_id)
    current_time = datetime.now()
    occupied_start_time = spot.occupied_start_time
    occupied_duration = spot.occupied_duration

    if occupied_start_time and occupied_duration:
        removal_time = occupied_start_time + timedelta(minutes=occupied_duration)
        if current_time >= removal_time:
            spot.isempty = True
            spot.occupied_start_time = None
            spot.occupied_duration = None
            spot.save()