from rest_framework import serializers
from courses.models import Course, CourseParticipant


class CourseParticipantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseParticipant
        fields = ['student', 'course', 'is_completed', ]


class CourseParticipantSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = CourseParticipant
        fields = ['id', 'student', 'course', 'is_completed', ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(instance.id)
        rep['student'] = instance.student.get_full_name()
        return rep


class CourseSerializer(serializers.ModelSerializer):
    course_participant = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'url', 'name', 'description', 'start_date',
            'end_date', 'students_count',
            'course_participant',
        ]

    @staticmethod
    def get_course_participant(obj):
        query = CourseParticipant.objects.filter(course=obj)[:10]
        serializer = CourseParticipantSerializer(query, many=True)
        return serializer.data
