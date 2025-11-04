from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import CustomUserCreationForm


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Регистрация успешно завершена! Добро пожаловать в систему."

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response