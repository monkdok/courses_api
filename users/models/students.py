from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager

User = get_user_model()


class StudentManager(UserManager):
    def get_queryset(self):
        from users.models import UserType
        return super().get_queryset().filter(
            is_staff=False,
            user_type=UserType.STUDENT.value
        )


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        from users.models import UserType
        self.user_type = UserType.sTudent.value
        super().save(*args, **kwargs)

    # Getting related objects of model CourseParticipant
    @property
    def course_participant(self):
        return self.courseparticipant_set.all()

    @property
    def courses(self):
        course_participants = self.courseparticipant_set.all()
        courses = []
        for course_participant in course_participants:
            courses.append(course_participant.course)
        return courses

    @property
    def courses_count(self):
        return len(self.courses)
