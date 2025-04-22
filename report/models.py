from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    symbol_number = models.CharField(max_length=20, unique=True)
    school_name = models.CharField(max_length=100)
    exam_year = models.CharField(max_length=10)
    english = models.FloatField()
    math = models.FloatField()
    nepali = models.FloatField()
    science = models.FloatField()   
    health = models.FloatField()
    total = models.FloatField()
    percentage = models.FloatField()
    grade = models.CharField(max_length=20)
    
    
