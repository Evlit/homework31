from pytest_factoryboy import register

from tests.factories import AdFactory, CategoryFactory, UserFactory

# Fixtures
pytest_plugins = "tests.fixtures"


# Factories
register(CategoryFactory)
register(UserFactory)
register(AdFactory)
