from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from app.views import *

router = DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', CreateStudent.as_view(), name='students'),
    path('students/', ListStudents.as_view(), name='list'),
    path('students/<int:pk>/', RetrieveStudent.as_view(), name='retrieve'),
    path('delete/<int:pk>/', DeleteStudent.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateStudent.as_view(), name='update'),
]

