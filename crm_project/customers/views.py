from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from .forms import CustomerForm


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'
    paginate_by = 10

    def get_queryset(self):
        return Customer.objects.all().order_by('-created_at')


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'
    context_object_name = 'customer'


class CustomerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    success_url = reverse_lazy('customers:customer_list')
    success_message = "Клиент успешно создан"


class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-edit.html'
    success_url = reverse_lazy('customers:customer_list')
    success_message = "Клиент успешно обновлен"


class CustomerDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:customer_list')
    success_message = "Клиент успешно удален"