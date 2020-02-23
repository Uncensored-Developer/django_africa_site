import pytest

from django_africa_site.videos.models import Video

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(video: Video):
    assert video.get_absolute_url() == f"/users/{video.slug}/"
