from factory import DjangoModelFactory, Faker, SubFactory
from django_africa_site.videos.models import Video, VideoCategory


class VideoCategoryFactory(DjangoModelFactory):

    name = Faker('name')

    class Meta:
        model = VideoCategory
        # django_get_or_create = ['name', 'slug']


class VideoFactory(DjangoModelFactory):

    title = Faker('text')
    description = Faker('text')
    thumbnail = Faker('url')
    link = Faker('url')
    category = SubFactory(VideoCategory)

    class Meta:
        model = Video
