from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Company
from .forms import CompanyForm


class CompanyListView(ListView):
    model = Company
    template_name = 'companies/list.html'
    context_object_name = 'companies'
    paginate_by = 20


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/detail.html'
    context_object_name = 'company'


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/form.html'
    success_url = reverse_lazy('companies:list')


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/form.html'
    success_url = reverse_lazy('companies:list')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'companies/confirm_delete.html'
    success_url = reverse_lazy('companies:list')
