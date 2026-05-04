from django.urls import path
from . import views

app_name = 'deals'

urlpatterns = [
    path('', views.DealListView.as_view(), name='list'),
    path('kanban/', views.DealKanbanView.as_view(), name='kanban'),
    path('nuevo/', views.DealCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DealDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.DealUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.DealDeleteView.as_view(), name='delete'),
]
