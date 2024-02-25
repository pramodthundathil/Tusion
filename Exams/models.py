from django.db import models
from main_app.models import Subject

# Create your models here.
class Exam(models.Model):
   exam_name = models.CharField(max_length=50)
   subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
   question_number = models.PositiveIntegerField(null = True)
   expery = models.DateTimeField(auto_now_add = False, null=True)
   total_marks = models.PositiveIntegerField(null = True)
   def __str__(self):
        return self.exam_name
   


class Question(models.Model):
    course=models.ForeignKey(Exam,on_delete=models.CASCADE, null = True)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
