import pytest

from utils import get_posts_all


def test_get_posts_all():
	assert type(get_posts_all()) == list