from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import DecimalField as DjangoDecimalField
from django.contrib.auth import get_user_model
from .models import UserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileForm
from products.models import Product
from ads.models import AdCampaign
from leads.models import Lead
from customers.models import Customer
from contracts.models import Contract

User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Дашборд'

        context['products_count'] = Product.objects.count()
        context['campaigns_count'] = AdCampaign.objects.count()
        context['leads_count'] = Lead.objects.count()
        context['customers_count'] = Customer.objects.count()
        context['contracts_count'] = Contract.objects.count()

        total_revenue = Contract.objects.aggregate(
            total=Coalesce(Sum('amount'), 0, output_field=DjangoDecimalField())
        )['total']
        total_budget = AdCampaign.objects.aggregate(
            total=Coalesce(Sum('budget'), 0, output_field=DjangoDecimalField())
        )['total']

        context['total_revenue'] = total_revenue
        context['total_budget'] = total_budget

        roi = 0
        if float(total_budget) > 0:
            roi = (float(total_revenue) / float(total_budget)) * 100
        context['roi'] = round(roi, 1)

        context['recent_leads'] = Lead.objects.order_by('-created_at')[:5]
        context['recent_customers'] = Customer.objects.order_by('-created_at')[:5]
        context['recent_contracts'] = Contract.objects.order_by('-start_date')[:5]

        return context


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user_obj'


class UserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')
    success_message = "Пользователь успешно создан"

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')
    success_message = "Пользователь успешно обновлен"


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_list')
    success_message = "Пользователь успешно удален"


class UserProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('users:user_list')
    success_message = "Профиль успешно обновлен"

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('user_id')
        return UserProfile.objects.get(user_id=user_id)