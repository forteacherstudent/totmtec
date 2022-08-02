from django.contrib import admin
from . import models


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    Admin for Department model
    """


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin for Employee model
    """


