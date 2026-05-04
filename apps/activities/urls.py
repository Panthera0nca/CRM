from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.ActivityListView.as_view(), name='list'),
    path('nueva/', views.ActivityCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.ActivityUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ActivityDeleteView.as_view(), name='delete'),
]
