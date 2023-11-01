from django.urls import path
from . import views

app_name = 'fireapp'

urlpatterns = [
    path('', views.parking_spot_list, name='parking_spot_list'),
    path('book/<uuid:spot_id>/', views.book_parking_spot, name='book_parking_spot'),
    path('add/', views.add_parking_spot, name='add_parking_spot'),
]
