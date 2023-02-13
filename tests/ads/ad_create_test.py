import pytest

from ads.models import Category


@pytest.mark.django_db
def test_ad_create(client, access_token):
    Category.objects.create(name="тестовая1")
    expected_response = {
                "id": 1,
                "is_published": False,
                "category": "тестовая1",
                "author": "test",
                "name": "Test test Test test",
                "price": 2500.0,
                "description": "description",
                "image": None
            }

    data = {"is_published": False,
            "category": "тестовая1",
            "author": "test",
            "name": "Test test Test test",
            "price": 2500.0,
            "description": "description",
            }

    response = client.post(
        "/ad/create/", data,
        content_type="application/json",  HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 201
    assert response.data == expected_response
