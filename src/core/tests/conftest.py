import pytest
from rest_framework.authtoken.models import Token


@pytest.fixture
def token(client, django_user_model):
    username = "admin"
    password = "admin"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    token = Token.objects.get_or_create(user=user)
    return token
