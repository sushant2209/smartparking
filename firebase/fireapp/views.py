from django.shortcuts import render
from .models import ParkingSpot, Reservation
from django.shortcuts import redirect

def parking_spot_list(request):
    parking_spots = ParkingSpot.objects.all()
    return render(request, 'parking_spot_list.html', {'parking_spots': parking_spots})

def book_parking_spot(request, spot_id):
    parking_spot = ParkingSpot.objects.get(id=spot_id)
    Reservation.objects.create(user_name="sushant", parking_spot=parking_spot)
    parking_spot.is_available = False
    parking_spot.save()
    return redirect('fireapp:parking_spot_list')

def add_parking_spot(request):
    spot_number = request.POST['spot_number']
    ParkingSpot.objects.create(spot_number=spot_number)
    return redirect('fireapp:parking_spot_list')
