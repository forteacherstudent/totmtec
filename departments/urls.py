from . import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

router.register('departments', views.DepartmentsViewSet)

urlpatterns = [
    path('home', views.home, name='home'),
]

urlpatterns += router.urls
