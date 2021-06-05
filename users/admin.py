from django.contrib import admin

from courses.admin import CourseParticipantInline
from users.forms import CustomUserCreationForm
from users.models import User, Student, Teacher
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('User type', {'fields': ('user_type', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'user_type'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'user_type', )
    ordering = ('email',)


@admin.register(Student)
class StudentAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'courses', 'courses_count', )
    inlines = (CourseParticipantInline,)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', ),
        }),
    )


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', ),
        }),
    )
