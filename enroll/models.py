from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    emp_dept = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.emp_name} - {self.emp_dept}"
