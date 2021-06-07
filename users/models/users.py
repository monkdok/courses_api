from enum import Enum
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager


class UserType(Enum):
    NONE = None
    STUDENT = 'student'
    TEACHER = 'teacher'

    @property
    def verbose_name(self):
        if self is UserType.STUDENT:
            return 'Student'
        elif self is UserType.TEACHER:
            return 'Teacher'
        elif self is UserType.NONE:
            return '--------------'


class User(AbstractUser):
    username = None
    user_type = models.CharField(
        'User Type',
        max_length=20,
        choices=((user_type.value, user_type.verbose_name) for user_type in UserType),
        default=UserType.NONE.value,
        blank=True,
        null=True
    )
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'All users'

    def __str__(self):
        return self.email

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.is_staff and self.user_type:
            raise ValidationError(f"Staff can't be a {self.user_type}")
