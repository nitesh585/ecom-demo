from django.conf import settings
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    """Model manager for product. A Manager is the interface through which
    database query operations are provided to Django models.
    """

    def get_queryset(self):
        """method should return a QuerySet with the properties you require.
        which will filter out only active(in stock) products.
        """
        return super(ProductManager, self).get_queryset().filter(is_active=True)


# Create your models here.
class Category(models.Model):
    """category model, A model is the single, definitive source of information about your data.
    It contains the essential fields and behaviors of the data you’re storing.
    """

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        """used to change the behavior of your model fields
        like changing order options,verbose_name and lot of other options.
        It's completely optional to add Meta class in your model."""

        verbose_name_plural = "categories"

    def __str__(self):
        """represents the class objects as a string
        Returns:
            [String]: [name of user]
        """
        return self.name

    def get_absolute_url(self):
        """provide absolute url for this category model"""
        return reverse("store:category_details", args=[self.slug])


class Product(models.Model):
    """Product  model, A model is the single, definitive source of information about your data.
    It contains the essential fields and behaviors of the data you’re storing.
    """

    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="product_creator",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    products = ProductManager()

    class Meta:
        """used to change the behavior of your model fields
        like changing order options,verbose_name and lot of other options.
        It's completely optional to add Meta class in your model."""

        verbose_name_plural = "products"
        ordering = ("-created",)

    def __str__(self):
        """represents the class objects as a string
        Returns:
            [String]: [name of user]
        """
        return self.title

    def get_absolute_url(self):
        """provide absolute url for this product model"""
        return reverse("store:product_details", args=[self.slug])
