from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from courses.models import Course, CourseParticipant
from courses.serializers import CourseSerializer, CourseParticipantSerializer, CourseParticipantCreateSerializer
from users.models import Student


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseParticipantViewSet(ModelViewSet):
    queryset = CourseParticipant.objects.all()
    serializer_class = CourseParticipantSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseParticipantSerializer
        elif self.action == 'retrieve':
            return CourseParticipantSerializer
        elif self.action == 'create':
            return CourseParticipantCreateSerializer
        elif self.action == 'destroy':
            return CourseParticipantSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        student_id = self.request.data.get('student')
        course_id = self.request.data.get('course')
        student = Student.objects.filter(id=student_id).first()
        course = Course.objects.filter(id=course_id).first()
        obj, created = CourseParticipant.objects.get_or_create(
            student=student,
            course=course
        )
        if created:
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_409_CONFLICT)


