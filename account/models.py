from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):
    """class used to customizing authentication in app

    Args:
        BaseUserManager ([class]): provides the core implementation of a user model.
    """

    def create_superuser(self, email, user_name, password, **other_fields):
        """method to create superuser that is used to login in admin account

        Args:
            email ([String]): user email
            user_name ([String]): name of user
            password ([String]): hashed password

        Raises:
            ValueError: [Superuser must be assigned to is_staff=True.]
            ValueError: [Superuser must be assigned to is_superuser=True.]

        Returns:
            [user]: []
        """
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        """method to create user and save details in db

        Args:
            email ([String]): user email
            user_name ([String]): name of user
            password ([String]): hashed password

        Raises:
            ValueError: [You must provide an email address]

        Returns:
            [user]: []
        """
        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    """base class to define user model that what properties
    it requires.

    Args:
        AbstractBaseUser ([class]): [provides the core implementation of a user model,
                                    including hashed passwords and tokenized password resets]
        PermissionsMixin ([class]): [abstract model you can include in the class hierarchy for
                                     your user model, giving you all the methods and database
                                     fields necessary to support Django’s permission model]
    """

    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(_("about"), max_length=500, blank=True)
    # Delivery details
    country = CountryField()
    phone_number = models.CharField(max_length=15, blank=True)
    postcode = models.CharField(max_length=12, blank=True)
    address_line_1 = models.CharField(max_length=150, blank=True)
    address_line_2 = models.CharField(max_length=150, blank=True)
    town_city = models.CharField(max_length=150, blank=True)
    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    class Meta:
        """used to change the behavior of your model fields
        like changing order options,verbose_name and lot of other options.
        It's completely optional to add Meta class in your model."""

        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message):
        """method used to send email after successfully activating the user

        Args:
            subject ([String]): [Subject of email]
            message ([String/Object]): [message it can be plain text or html]
        """
        send_mail(
            subject,
            message,
            "l@1.com",
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        """represents the class objects as a string
        Returns:
            [String]: [name of user]
        """
        return self.user_name
