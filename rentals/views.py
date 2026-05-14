from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Equipment, Client, Rental
from .forms import EquipmentForm, ClientForm, RentalForm
from django.views.generic import TemplateView

class EquipmentListView(ListView):
    model = Equipment
    template_name = 'rentals/equipment_list.html'


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'rentals/equipment_detail.html'


class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'rentals/equipment_form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentUpdateView(UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'rentals/equipment_form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'rentals/equipment_confirm_delete.html'
    success_url = reverse_lazy('equipment_list')


class ClientListView(ListView):
    model = Client
    template_name = 'rentals/client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'rentals/client_detail.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'rentals/client_form.html'
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'rentals/client_form.html'
    success_url = reverse_lazy('client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'rentals/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


class RentalListView(ListView):
    model = Rental
    template_name = 'rentals/rental_list.html'


class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rentals/rental_detail.html'


class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_form.html'
    success_url = reverse_lazy('rental_list')


class RentalUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_form.html'
    success_url = reverse_lazy('rental_list')


class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rentals/rental_confirm_delete.html'
    success_url = reverse_lazy('rental_list')

class HomeView(TemplateView):
    template_name = 'rentals/home.html'