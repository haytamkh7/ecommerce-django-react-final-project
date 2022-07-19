import pytest
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from base.models import Product


def create_user():
    return User.objects.create(first_name='Jimmy',
                               username='test_user@test.com',
                               password='password')


@pytest.mark.django_db
def test_create_user():
    new_user_jimmy = create_user()
    assert isinstance(new_user_jimmy, User) is True
    assert new_user_jimmy.first_name == 'Jimmy'


@pytest.mark.django_db
def test_set_check_password():
    new_user_jimmy = create_user()
    new_user_jimmy.set_password("new-password")
    assert new_user_jimmy.check_password("new-password") is True

# @pytest.mark.django_db
# def test_product_creation():
#     p = create_product()
#     assert isinstance(p, Product) is True
#     assert p.name == "Jimi Hendrix Guitar"
