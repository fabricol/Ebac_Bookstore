# In your factories.py file used by the tests, correct the field name
import factory
from product.models import Category, Product
from order.models import User  # Adjust the import path as needed

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker('word')  # Assuming it should be 'title'

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker('word')
    price = factory.Faker('random_number')
    # Add other necessary fields

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # Add necessary fields and default values