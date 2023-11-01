from django import forms
from .models import ParkingSpot

class ParkingSpotForm(forms.ModelForm):
    class Meta:
        model = ParkingSpot
        fields = ['name','isempty']  # Add more fields if necessary
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = ParkingSpot
        fields = ['occupied_duration', 'occupied_start_time']  # Add other fields as needed