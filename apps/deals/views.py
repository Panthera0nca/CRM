from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Deal
from .forms import DealForm


class DealListView(ListView):
    model = Deal
    template_name = 'deals/list.html'
    context_object_name = 'deals'
    paginate_by = 20


class DealKanbanView(TemplateView):
    template_name = 'deals/kanban.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stages = Deal.STAGE_CHOICES
        context['columns'] = [
            {
                'key': key,
                'label': label,
                'deals': Deal.objects.filter(stage=key).select_related('contact', 'company'),
            }
            for key, label in stages
        ]
        return context


class DealDetailView(DetailView):
    model = Deal
    template_name = 'deals/detail.html'
    context_object_name = 'deal'


class DealCreateView(CreateView):
    model = Deal
    form_class = DealForm
    template_name = 'deals/form.html'
    success_url = reverse_lazy('deals:list')


class DealUpdateView(UpdateView):
    model = Deal
    form_class = DealForm
    template_name = 'deals/form.html'
    success_url = reverse_lazy('deals:list')


class DealDeleteView(DeleteView):
    model = Deal
    template_name = 'deals/confirm_delete.html'
    success_url = reverse_lazy('deals:list')
