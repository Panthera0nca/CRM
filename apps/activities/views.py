from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Activity
from .forms import ActivityForm


class ActivityListView(ListView):
    model = Activity
    template_name = 'activities/list.html'
    context_object_name = 'activities'
    paginate_by = 20


class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/form.html'
    success_url = reverse_lazy('activities:list')


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/form.html'
    success_url = reverse_lazy('activities:list')


class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activities/confirm_delete.html'
    success_url = reverse_lazy('activities:list')
