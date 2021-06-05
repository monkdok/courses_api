from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager

User = get_user_model()


class TeacherManager(UserManager):
    def get_queryset(self):
        from users.models import UserType
        return super().get_queryset().filter(
            is_staff=False,
            user_type=UserType.TEACHER.value
        )


class Teacher(User):
    objects = TeacherManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        from users.models import UserType
        self.user_type = UserType.TEACHER.value
        super().save(*args, **kwargs)