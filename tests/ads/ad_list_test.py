import pytest

from ads.serializers.ad import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client, access_token):
    ad_list = AdFactory.create_batch(3)
    expected_response = {
        "count": 3,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ad_list, many=True).data
    }

    response = client.get("/ad/",  HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 200
    assert response.data == expected_response
