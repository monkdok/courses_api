import csv

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import Student
from users.serializers import StudentSerializer
from users.utils import export_csv


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ExportViewSet(APIView):
    def get(self, request, export_format=None):
        student_id = request.GET.get('student')
        if not export_format:
            response = export_csv(student_id)
            return response

    @classmethod
    def get_extra_actions(cls):
        return []
