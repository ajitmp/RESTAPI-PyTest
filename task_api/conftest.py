import pytest

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasks.settings')

import django
django.setup()


from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()
