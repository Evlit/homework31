import pytest


@pytest.fixture()
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test"
    password = "123qwe"

    django_user_model.objects.create_user(username=username, password=password)
    response = client.post("/user/token/", {"username": username, "password": password}, format='json')

    return response.data["access"]
