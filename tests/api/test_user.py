# import pytest
# from rest_framework.test import APIClient
#
# from base.models import Product
#
# from rest_framework.authtoken.admin import User
#
# """
# API Test -> Integration Test - testing if Api can create a user successfully
# """
#
# # @pytest.mark.django_db - communicating with database then deleting the added element from the database
# # if we delete this line of code, the database will actually have the product in it.
#
# client = APIClient()
#
#
# @pytest.mark.django_db
# def test_api_user_creation():
#     payload = dict(
#         name="test_user@test.com", email="test_user@test.com", password="password789"
#     )
#     response = client.post("/api/users/register/", payload)
#     payload = dict(username=response.data["username"], password="password789")
#     response = client.post("/api/users/login/", payload)
#     assert response.status_code == 200
#
#
# @pytest.mark.django_db
# def test_api_login():
#     # Register user
#     payload = dict(first_name='Michael', last_name='Scott', email='michael_s@gmail.com', password='yespassword')
#     client.post("/api/register/", payload)
#
#     # Sign in
#     response = client.post("/api/login/", dict(email='michael_s@gmail.com', password='yespassword'))
#
#     # Status code for login
#     assert response.status_code == 200
#
#
# def create_product():
#     return Product.objects.create(
#         name="Jimi Hendrix Guitar",
#         price=200,
#         brand="Fender",
#         countInStock=1,
#         category="Electric Guitar",
#         description="Best guitar")
#
#
# @pytest.mark.django_db
# def test_product_creation():
#     p = create_product()
#     assert isinstance(p, Product) is True
#     assert p.name == "Jimi Hendrix Guitar"
#
#
# # Api test  - Integration testing
# @pytest.mark.django_db
# def test_api_product_creation():
#     user = User.objects.create_superuser(username="Admin7", password='adminadmin', email='admin7@gmail.com')
#     client.force_authenticate(user)
#     payload = dict(
#         name="Jimi Hendrix Guitar",
#         price=200,
#         brand="Fender",
#         countInStock=1,
#         category="Electric Guitar",
#         description="Best guitar"
#     )
#     response = client.post("/api/products/create/")
#     assert response.status_code == 200
