from django.views.generic import TemplateView
from django.db.models import Sum, Count
from apps.contacts.models import Contact
from apps.companies.models import Company
from apps.deals.models import Deal
from apps.activities.models import Activity


class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_contacts'] = Contact.objects.count()
        context['total_companies'] = Company.objects.count()
        context['open_deals'] = Deal.objects.exclude(stage__in=['won', 'lost']).count()
        context['won_value'] = Deal.objects.filter(stage='won').aggregate(
            total=Sum('value')
        )['total'] or 0
        context['deals_by_stage'] = Deal.objects.values('stage').annotate(count=Count('id'))
        context['recent_activities'] = Activity.objects.select_related(
            'deal', 'contact'
        ).order_by('-date')[:5]
        context['recent_deals'] = Deal.objects.select_related(
            'contact', 'company'
        ).order_by('-created_at')[:5]
        return context
