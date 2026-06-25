from django.urls import path
from .views import hello_view, DepartmentListAPIView, CourseListAPIView, CourseDetailAPIView
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet
router = DefaultRouter()
router.register(r'viewset/courses', CourseViewSet, basename='course')
urlpatterns = [
    path('hello/', hello_view),

    # Department API
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),

    # APIView based Course APIs
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
]

urlpatterns += router.urls