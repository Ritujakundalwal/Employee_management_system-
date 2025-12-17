from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name


