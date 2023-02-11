from django.urls import path
from .views import AddsList, AddsView, AddsCreate, AddsUpdate, AddsDelete, CommentsCreate, DeleteComments, ListNoModerAdds, CheckModer, CheckCancelModer

app_name = 'webapp'

urlpatterns = [
    path('', AddsList.as_view(), name='index'),
    path('adds/detail/<int:pk>/', AddsView.as_view(), name='detail_adds'),
    path('adds/create/', AddsCreate.as_view(), name='create_adds'),
    path('adds/<int:pk>/update/', AddsUpdate.as_view(), name='update_adds'),
    path('adds/<int:pk>/delete/', AddsDelete.as_view(), name='delete_adds'),
    path('comments/<int:pk>/delete/', DeleteComments.as_view(), name='delete_comment'),
    path('comments/<int:pk>/create/', CommentsCreate.as_view(), name='create_comments'),
    path('listnomoder/', ListNoModerAdds.as_view(), name='list_moder'),
    path('adds/<int:pk>/addsmoder', CheckModer.as_view(), name='adds_moder'),
    path('adds/<int:pk>/cancel', CheckCancelModer.as_view(), name='cancel_moder'),
]