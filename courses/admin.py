from django.contrib import admin
from courses.models import Course, CourseParticipant


class CourseParticipantInline(admin.TabularInline):
    model = CourseParticipant


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = (CourseParticipantInline, )
    list_display = ('name', 'start_date', 'end_date', 'students', 'students_count', )
    list_display_links = ('name', )
    list_editable = ('start_date', 'end_date', )
    list_filter = ('start_date', 'end_date', )


