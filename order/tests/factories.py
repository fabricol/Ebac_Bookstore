import factory
from django.contrib.auth.models import User
from order.models import Order
from product.models import Category, Product





class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')

    class Meta:
        model = User

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category
    title = factory.Faker('word')

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    title = factory.Faker("pystr")
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    product = factory.RelatedFactoryList(ProductFactory, 'order', size=1)

    class Meta:
        model = Order