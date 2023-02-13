import factory
from ads.models import Ad, User, Category


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123qwe"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    is_published = False
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    name = factory.Faker("name")
    price = 2500.0
    description = "description"
