from rest_framework import routers
from courses.views import CourseViewSet, CourseParticipantViewSet

router = routers.DefaultRouter()

router.register(r'', CourseViewSet)
router.register(r'participant', CourseParticipantViewSet)
