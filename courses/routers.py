from rest_framework import routers
from courses.views import CourseViewSet, CourseParticipantViewSet

router = routers.DefaultRouter()

router.register(r'list', CourseViewSet)
router.register(r'participant', CourseParticipantViewSet)
# router.register(r'participant/assign/<int:id>/', CourseParticipantViewSet)
# router.register(r'participant/unassign/<int:id>/', CourseParticipantViewSet)
