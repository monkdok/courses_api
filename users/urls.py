from django.urls import path, include
from .routers import router
from .views.students import ExportViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('export/<str:export_format>/', ExportViewSet.as_view()),
]
urlpatterns += router.urls
