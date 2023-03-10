import pytest

from ads.serializers.ad import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_detail(client, access_token):
    ad = AdFactory.create()

    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 200
    assert response.data == AdListSerializer(ad).data
