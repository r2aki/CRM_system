from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from products.models import Product
from .models import Lead
from .forms import LeadForm
from contracts.models import Contract
from customers.models import Customer


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'
    paginate_by = 10

    def get_queryset(self):
        return Lead.objects.all().order_by('-created_at')


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:lead_list')
    success_message = "Потенциальный клиент успешно создан"


class LeadUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('leads:lead_list')
    success_message = "Потенциальный клиент успешно обновлен"


class LeadDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:lead_list')
    success_message = "Потенциальный клиент успешно удален"


class LeadConvertView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Contract
    fields = ['name', 'product', 'document', 'start_date', 'end_date', 'amount']
    template_name = 'leads/leads-convert.html'
    success_message = "Клиент успешно переведен в активные"

    def get_success_url(self):
        return reverse('customers:customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.lead = get_object_or_404(Lead, pk=self.kwargs['pk'])
        context['lead'] = self.lead
        context['title'] = f'Конвертация клиента: {self.lead}'
        context['product_list'] = Product.objects.filter(is_active=True)
        return context

    def form_valid(self, form):
        contract = form.save(commit=False)
        contract.save()

        customer = Customer.objects.create(
            first_name=self.lead.first_name,
            last_name=self.lead.last_name,
            middle_name=self.lead.middle_name,
            phone=self.lead.phone,
            email=self.lead.email,
            contract=contract
        )

        self.lead.delete()
        messages.success(self.request, self.success_message)
        return redirect(self.get_success_url())