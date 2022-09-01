import datetime

from rest_framework import serializers
from . import models
from django.db.models import Count,Avg


class DepartmentSerializer(serializers.ModelSerializer):
    num_of_employees = serializers.SerializerMethodField()
    retired_employees = serializers.SerializerMethodField()
    average_salary = serializers.SerializerMethodField()

    def get_num_of_employees(self, department):
        count = models.Employee.objects.filter(department=department).aggregate(cnt=Count('name'))

        return count['cnt']
        '''count = 0
        employees = models.Employee.objects.all()
        for employee in employees:
            if employee.department == department:
                count += 1
        return count'''


    def get_retired_employees(self, department):
        d = datetime.datetime.now() - datetime.timedelta(days=60*365)
        retired_emp = models.Employee.objects.values_list('name',flat=True).filter(department=department,date_of_birth__lte=d)
        return list(retired_emp)
        #return ['Hello']
        '''retired_employee_names = []
        employees = models.Employee.objects.all()
        for employee in employees:
            if employee.department != department:
                # Only consider employees who belong to current department
                continue
            # Employee is retired if their year of birth + 60 is less than current year.
            if employee.date_of_birth.year + 60 < datetime.date.today().year:
                retired_employee_names.append(employee.name)
        return retired_employee_names'''

    def get_average_salary(self, department):
        avg_sal = models.Employee.objects.filter(department=department).aggregate(average_salary=Avg('salary'))
        return avg_sal['average_salary']
        '''counter = 0
        total_salary = 0
        employees = models.Employee.objects.all()
        for employee in employees:
            if employee.department == department:
                counter += 1
                total_salary += employee.salary
        if counter == 0:
            return 0
        return total_salary / counter'''


    class Meta:
        model = models.Department
        fields = ("name", "average_salary", "num_of_employees", "retired_employees")
