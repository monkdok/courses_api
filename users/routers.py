from rest_framework import routers
from users.views.students import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

