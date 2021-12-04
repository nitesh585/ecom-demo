from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from store.views import *

from ..models import Category, Product


class TestSkip(TestCase):
    def setUp(self) -> None:
        """create user and category that is going to be
        used in the test cases
        """
        self.client = Client()
        self.factory = RequestFactory()
        User.objects.create(username="admin")
        Category.objects.create(name="book", slug="book")
        self.data1 = Product.products.create(
            category_id=1,
            title="Machine learning",
            created_by_id=1,
            slug="machine-learning",
            price="10.00",
            image="ml",
        )

    def test_url_allowed_hosts(self):
        """Test Homepage response status"""

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """Test Product Detail status"""
        response = self.client.get(
            reverse("store:product_details", args=["machine-learning"])
        )

        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """Test Category Detail status"""
        response = self.client.get(reverse("store:category_details", args=["book"]))

        self.assertEqual(response.status_code, 200)

    def test_url_allowed_hosts(self):
        """Test Allowed Hosts"""

        response = self.client.get("/", HOST_HOST="noaddress.com")
        self.assertTrue(response.status_code, 400)
        response = self.client.get("/", HOST_HOST="yourcompany.com")
        self.assertTrue(response.status_code, 200)
