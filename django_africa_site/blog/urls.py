from django.urls import path
from .views import ckeditor_form_view, PostDetailView


app_name = 'blog'


urlpatterns = [
    path('', ckeditor_form_view, name='ckeditor-form'),
    path(
        '<int:pk>/<slug:slug>/',
        PostDetailView.as_view(),
        name='detail'
    )
]
