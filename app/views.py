from django.shortcuts import render
from .models import *
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class CreateStudent(CreateAPIView):
    serializer_class = StudentSerializer

class ListStudents(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer

class RetrieveStudent(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer

    def get_queryset(self, pk, *args, **kwargs):
        queryset = Student.objects.get(id=pk)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(kwargs['pk'])
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteStudent(DestroyAPIView):
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs['pk'])
        student.delete()
        return Response("Student has been deleted", status=status.HTTP_204_NO_CONTENT)

class UpdateStudent(UpdateAPIView):
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs['pk'])
        serializer = self.serializer_class(student)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def update(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs['pk'])
        student.first_name = request.data['first_name']
        student.last_name = request.data['last_name']
        student.email = request.data['email']
        student.username = request.data['username']
        student.password = request.data['password']
        student.phone = request.data['phone']
        student.birthday = request.data['birthday']
        return Response("Student has been deleted", status=status.HTTP_200_OK)

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer