from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contract
from .forms import ContractForm


class ContractListView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'
    paginate_by = 10

    def get_queryset(self):
        return Contract.objects.all().order_by('-start_date')


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'
    context_object_name = 'contract'


class ContractCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-create.html'
    success_url = reverse_lazy('contracts:contract_list')
    success_message = "Контракт успешно создан"


class ContractUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-edit.html'
    success_url = reverse_lazy('contracts:contract_list')
    success_message = "Контракт успешно обновлен"


class ContractDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:contract_list')
    success_message = "Контракт успешно удален"