import csv
from django.http import HttpResponse
from users.models import Student


def export_csv(student_id: int):
    student = Student.objects.filter(id=student_id).first()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{student.get_full_name()}.csv"'
    field_names = ['Name', 'Courses num', 'Completed courses num']
    writer = csv.DictWriter(response, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({
        'Name': student.get_full_name(),
        'Courses num': student.course_participant.count(),
        'Completed courses num': student.course_participant.filter(is_completed=True).count()})
    return response
