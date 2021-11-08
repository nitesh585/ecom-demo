from unittest.case import skip

from django.contrib.auth.models import User
from django.http import response
from django.http.request import HttpRequest
from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from store.views import *

from ..models import Category, Product


# @skip("simulating skipping the testcase during unittest")
class TestSkip(TestCase):
    # def test_skip():
    #     pass

    def setUp(self) -> None:
        self.client = Client()
        self.factory = RequestFactory()
        User.objects.create(username="admin")
        Category.objects.create(name="book", slug="book")
        self.data1 = Product.objects.create(
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

    def test_homepage_html(self):
        """Test Homepage HTML"""

        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode("utf-8")

        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        """Test Homepage HTML using FactoryRequest"""

        request = self.factory.get("/item/machine-learning")
        response = all_products(request)
        html = response.content.decode("utf-8")

        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)
