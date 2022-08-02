import datetime

from rest_framework import serializers
from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    num_of_employees = serializers.SerializerMethodField()
    retired_employees = serializers.SerializerMethodField()
    average_salary = serializers.SerializerMethodField()

    def get_num_of_employees(self, department):
        count = 0
        employees = models.Employee.objects.all()
        for employee in employees:
            if employee.department == department:
                count += 1
        return count

    def get_retired_employees(self, department):
        retired_employee_names = []
        employees = models.Employee.objects.all()
        for employee in employees:
            if employee.department != department:
                # Only consider employees who belong to current department
                continue
            # Employee is retired if their year of birth + 60 is less than current year.
            if employee.date_of_birth.year + 60 < datetime.date.today().year:
                retired_employee_names.append(employee.name)
        return retired_employee_names

    def get_average_salary(self, department):
        counter = 0
        total_salary = 0
        employees = models.Employee.objects.all()
        for employee in employees:
            if employee.department == department:
                counter += 1
                total_salary += employee.salary
        if counter == 0:
            return 0
        return total_salary / counter


    class Meta:
        model = models.Department
        fields = ("name", "average_salary", "num_of_employees", "retired_employees")
