import pytest
from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, access_token, user):
    ad_list = AdFactory.create_batch(3)
    expected_response = {
        "id": 1,
        "name": "Тестовая подборка",
        "owner": user.pk,
        "items": [ad.pk for ad in ad_list]
    }

    data = {
        "name": "Тестовая подборка",
        "owner": user.pk,
        "items": [ad.pk for ad in ad_list]
        }

    response = client.post("/selection/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
    # content_type = "application/json",
    assert response.status_code == 201
    assert response.data == expected_response
