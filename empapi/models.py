from django.db import models


class Emp(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=250)
    salary = models.PositiveIntegerField()
    experiance = models.PositiveIntegerField()


    def __str__(self):
        return self.name
