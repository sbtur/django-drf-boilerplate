import pytest
import json
from django.urls import reverse
from rest_framework import status
from django.conf import settings

@pytest.mark.django_db
def test_example(client, token):
	
	response = client.get(
		reverse("example-list"),
        headers={"HTTP_AUTHORIZATION": "Token {}".format(token)},
        content_type="application/json",
    )

	assert response.json().get("text") is not None
	assert response.status_code == status.HTTP_200_OK