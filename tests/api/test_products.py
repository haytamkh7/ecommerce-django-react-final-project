import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


def create_product():
    return Product.objects.create(
        name=" Product Name ",
        price=0,
        brand="Sample brand ",
        countInStock=0,
        category="Sample category",
        description=" ",
    )


@pytest.mark.django_db
def test_api_product_creation():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="123", is_staff=True)
    client.force_authenticate(user)
    response = client.post("/api/products/create/")
    data = response.data
    print(data)
    assert data["name"] == " Product Name "
