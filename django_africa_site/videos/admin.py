from django.contrib import admin
from django.http.request import HttpRequest
from django.db.models import QuerySet
from .models import Video, VideoCategory


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {"fields": ("tags",)})
    ]
    list_display = ["title", "link", "category", "tags_list"]
    search_fields = ["title", "category", "tags"]

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).prefetch_related('tags')

    def tags_list(self, obj):
        return ', '.join(i.name for i in obj.tags.all())


admin.site.register(VideoCategory)
