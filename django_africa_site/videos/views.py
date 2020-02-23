from django.views.generic import ListView, DetailView, FormView
from typing import Any, Dict
from .models import Video, VideoCategory
from .forms import AddVideoForm


class VideosListView(ListView):
    template_name = 'videos/list.html'
    model = Video
    paginate_by = 15


class VideoDetailView(DetailView):
    template_name = 'videos/detail.html'
    model = Video


class VideoAdminView(FormView):
    template_name = 'videos/admin/index.html'
    form_class = AddVideoForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = VideoCategory.objects.all()
        return context
