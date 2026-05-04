from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='list'),
    path('nuevo/', views.ContactCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.ContactUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ContactDeleteView.as_view(), name='delete'),
]
