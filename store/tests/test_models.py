from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name="book", slug="book")

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes.
        Test Category default name
        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), "book")


class TestProductModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="book", slug="book")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1,
            title="Machine learning",
            created_by_id=1,
            slug="machine-learning",
            price="10.00",
            image="ml",
        )

    def test_product_model_entry(self):
        """
        Test Product model data insertion/types/field attributes.
        Test Product default name
        """

        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "Machine learning")
