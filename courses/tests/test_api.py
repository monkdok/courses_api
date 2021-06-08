import random
from datetime import date, timedelta
from rest_framework import status
from rest_framework.test import APITestCase
from courses.models import Course, CourseParticipant
from courses.serializers import CourseSerializer
from users.models import UserType, Student


class CourseApiTestCase(APITestCase):
    def setUp(self):
        # Courses
        start_date, end_date = course_schedule()
        self.course_1 = Course.objects.create(
            name='First Test Course Name',
            description='First Test Course Description',
            start_date=start_date,
            end_date=end_date
        )

        start_date, end_date = course_schedule()
        self.course_2 = Course.objects.create(
            name='Second Test Course Name',
            description='Second Test Course Description',
            start_date=start_date,
            end_date=end_date
        )

        # Students
        self.student_1 = Student.objects.create(
            email='student_1@gmail.com',
            first_name='John',
            last_name='Peterson',
            user_type=UserType.STUDENT.value
        )
        self.student_2 = Student.objects.create(
            email='student_2@gmail.com',
            first_name='Peter',
            last_name='Johnson',
            user_type=UserType.STUDENT.value
        )

    def test_get(self):
        # url = reverse('courses-list')
        url = '/courses/'
        response = self.client.get(url)
        serialized_data = CourseSerializer(
            [self.course_1, self.course_2],
            many=True
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_course_participant_assign_unassign(self):
        # Assign testing
        course_participant = CourseParticipant.objects.create(
            course=self.course_1,
            student=self.student_1
        )
        self.assertEqual(
            (course_participant.course, course_participant.student),
            (self.course_1, self.student_1)
        )

        # Unssign testing
        course_participant.delete()
        self.assertFalse(CourseParticipant.objects.filter(pk=course_participant.pk).exists())

    def test_csv_export(self):
        url = '/users/export/csv/'
        response = self.client.get(url, data={'student': self.student_1.id})
        result = response.content.decode()
        line_split = result.split('\n')
        word_split = [line.replace('\r', '').split(',') for line in line_split]
        field_names = ['Name', 'Courses num', 'Completed courses num']
        field_values = [
            self.student_1.get_full_name(),
            str(self.student_1.course_participant.count()),
            str(self.student_1.course_participant.filter(is_completed=True).count())
        ]
        self.assertListEqual(field_names, word_split[0])
        self.assertListEqual(field_values, word_split[1])
        self.assertEqual(status.HTTP_200_OK, response.status_code)


def course_schedule():
    start_date = date.today() + timedelta(weeks=random.randint(2, 10))
    end_date = start_date + timedelta(weeks=random.randint(2, 40))
    return start_date, end_date
