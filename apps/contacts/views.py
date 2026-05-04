from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm


class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/list.html'
    context_object_name = 'contacts'
    paginate_by = 20


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/detail.html'
    context_object_name = 'contact'


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/form.html'
    success_url = reverse_lazy('contacts:list')


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/form.html'
    success_url = reverse_lazy('contacts:list')


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contacts/confirm_delete.html'
    success_url = reverse_lazy('contacts:list')
