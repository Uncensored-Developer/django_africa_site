from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from model_utils.models import TimeStampedModel


class VideoCategory(TimeStampedModel):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, **kwargs):
        self.slug = slugify(str(self.name))
        return super().save(**kwargs)

    class Meta:
        ordering = ['name', ]


class Video(TimeStampedModel):

    title = models.CharField(max_length=250)
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    link = models.URLField()
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)

    tags = TaggableManager()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('videos:detail', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        self.slug = slugify(str(self.title))
        return super().save(**kwargs)

    class Meta:
        ordering = ['-created', ]
