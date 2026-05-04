from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('companies/', include('apps.companies.urls')),
    path('deals/', include('apps.deals.urls')),
    path('activities/', include('apps.activities.urls')),
]
