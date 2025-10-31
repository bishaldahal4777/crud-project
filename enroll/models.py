from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(max_length=4)
    emp_name = models.CharField(max_length=100)
    emp_dept = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"self.emp_name - self.emp-dept"

