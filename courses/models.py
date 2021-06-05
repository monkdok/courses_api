from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from users.models import Student


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Course(TimeStampMixin):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date should be greater than start date.")

    # Getting related objects of model CourseParticipant
    @property
    def course_participant(self):
        return self.course_participant_set.all()

    @property
    def students(self):
        course_participants = self.courseparticipant_set.all()
        students = []
        for course_participant in course_participants:
            students.append(course_participant.student.get_full_name())
        return students

    @property
    def students_count(self):
        return len(self.students)


class CourseParticipant(TimeStampMixin):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'"{self.course}". Student: {self.student}'
