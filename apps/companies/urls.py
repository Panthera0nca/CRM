from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='list'),
    path('nueva/', views.CompanyCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.CompanyUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.CompanyDeleteView.as_view(), name='delete'),
]
