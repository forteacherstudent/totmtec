from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.shortcuts import render

from . import serializers, models


def home(request):
    return render(request, "index.html")


class DepartmentsViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()
