from django.urls import path
from django.conf import settings
from .views import VideosListView, VideoDetailView, VideoAdminView


app_name = 'videos'

urlpatterns = [
    path('', VideosListView.as_view(), name='list'),
    path(settings.ADMIN_URL, VideoAdminView.as_view(), name='admin'),
    path('<slug:slug>/', VideoDetailView.as_view(), name='detail'),

]
