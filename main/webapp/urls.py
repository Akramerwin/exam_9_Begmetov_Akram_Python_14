from django.urls import path
from .views import AddsList, AddsView, AddsCreate, AddsUpdate, AddsDelete

app_name = 'webapp'

urlpatterns = [
    path('', AddsList.as_view(), name='index'),
    path('adds/detail/<int:pk>/', AddsView.as_view(), name='detail_adds'),
    path('adds/create', AddsCreate.as_view(), name='create_adds'),
    path('adds/<int:pk>/update/', AddsUpdate.as_view(), name='update_adds'),
    path('adds/<int:pk>/delete', AddsDelete.as_view(), name='delete_adds'),
]