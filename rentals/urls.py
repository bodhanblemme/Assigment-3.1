from django.urls import path
from .views import *

urlpatterns = [
    path('equipment/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/create/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment_delete'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('rentals/', RentalListView.as_view(), name='rental_list'),
    path('rentals/<int:pk>/', RentalDetailView.as_view(), name='rental_detail'),
    path('rentals/create/', RentalCreateView.as_view(), name='rental_create'),
    path('rentals/<int:pk>/update/', RentalUpdateView.as_view(), name='rental_update'),
    path('rentals/<int:pk>/delete/', RentalDeleteView.as_view(), name='rental_delete'),
]