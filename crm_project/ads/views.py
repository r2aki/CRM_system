from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import DecimalField as DjangoDecimalField
from .models import AdCampaign
from .forms import AdCampaignForm
from leads.models import Lead
from customers.models import Customer
from contracts.models import Contract


class AdCampaignListView(LoginRequiredMixin, ListView):
    model = AdCampaign
    template_name = 'ads/ads-list.html'
    context_object_name = 'campaigns'
    paginate_by = 10

    def get_queryset(self):
        return AdCampaign.objects.all().order_by('-start_date')


class AdCampaignDetailView(LoginRequiredMixin, DetailView):
    model = AdCampaign
    template_name = 'ads/ads-detail.html'
    context_object_name = 'campaign'


class AdCampaignCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AdCampaign
    form_class = AdCampaignForm
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:ad_campaign_list')
    success_message = "Рекламная кампания успешно создана"


class AdCampaignUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AdCampaign
    form_class = AdCampaignForm
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:ad_campaign_list')
    success_message = "Рекламная кампания успешно обновлена"


class AdCampaignDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = AdCampaign
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:ad_campaign_list')
    success_message = "Рекламная кампания успешно удалена"


class AdCampaignStatisticsView(LoginRequiredMixin, TemplateView):
    template_name = 'ads/ads-statistic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статистика рекламных кампаний'

        campaigns = AdCampaign.objects.all().order_by('-start_date')
        statistics_data = []

        for campaign in campaigns:
            potential_clients_count = Lead.objects.filter(campaign=campaign).count()
            active_clients_count = Customer.objects.filter(contract__lead__campaign=campaign).count()

            total_revenue = Contract.objects.filter(lead__campaign=campaign).aggregate(
                total=Coalesce(Sum('amount'), 0, output_field=DjangoDecimalField())
            )['total']

            roi = 0
            if campaign.budget > 0:
                roi = (float(total_revenue) / float(campaign.budget)) * 100

            statistics_data.append({
                'campaign': campaign,
                'potential_clients_count': potential_clients_count,
                'active_clients_count': active_clients_count,
                'conversion_rate': round(
                    (active_clients_count / potential_clients_count * 100) if potential_clients_count > 0 else 0, 1),
                'total_revenue': total_revenue,
                'roi': round(roi, 1),
            })

        total_potential_clients = Lead.objects.count()
        total_active_clients = Customer.objects.count()
        total_revenue = Contract.objects.aggregate(
            total=Coalesce(Sum('amount'), 0, output_field=DjangoDecimalField())
        )['total']
        total_budget = AdCampaign.objects.aggregate(
            total=Coalesce(Sum('budget'), 0, output_field=DjangoDecimalField())
        )['total']

        overall_roi = 0
        if float(total_budget) > 0:
            overall_roi = (float(total_revenue) / float(total_budget)) * 100

        context['statistics_data'] = statistics_data
        context['total_potential_clients'] = total_potential_clients
        context['total_active_clients'] = total_active_clients
        context['total_revenue'] = total_revenue
        context['total_budget'] = total_budget
        context['overall_roi'] = round(overall_roi, 1)

        return context