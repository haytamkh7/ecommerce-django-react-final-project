import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from base.models import Product

"""
Integration testing testing api to register user
"""


@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    payload = dict(name="testing123", email="test11@test.com", password="super-secret")
    response = client.post("/api/users/register/", payload)
    data = response.data
    print(data)
    assert data["name"] == payload["name"]
