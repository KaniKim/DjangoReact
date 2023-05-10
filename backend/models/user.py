from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import (
    EmailField,
    CharField,
    BooleanField,
    DateTimeField,
    UUIDField,
)
from django.utils import timezone


class User(AbstractBaseUser):
    id = UUIDField(
        verbose_name="ID Field", max_length=64, unique=True, primary_key=True
    )
    email = EmailField(verbose_name="Email Address", max_length=255, unique=True)
    nickname = CharField(verbose_name="NickName", max_length=30, unique=True)
    name = CharField(verbose_name="RealName", max_length=30, unique=False)
    is_active = BooleanField(verbose_name="Is Active", default=False)
    is_staff = BooleanField(verbose_name="Is Staff", default=False)
    joined_date = DateTimeField(verbose_name="Date Joined", default=timezone.now())
    expired_date = DateTimeField(verbose_name="Date Expired", default=timezone.now())
    password = CharField(verbose_name="Password", max_length=1023)
    ethereum_address = CharField(
        verbose_name="Ether Address", max_length=255, unique=True
    )

    class Meta:
        app_label = "user"
