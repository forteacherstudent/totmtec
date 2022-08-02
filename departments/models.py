from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=12)
    location = models.CharField(max_length=12)  # Can either be US or Canada

    def __str__(self):
        return f"{self.name} @ {self.location}"


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)
    salary = models.PositiveIntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name} @ {self.department}"
