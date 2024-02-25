from django.urls import path 
from .import views 


urlpatterns = [
    path("AddanExam",views.AddanExam,name="AddanExam"),
    path("AddQuestionstoexam/<int:pk>",views.AddQuestionstoexam,name="AddQuestionstoexam"),
    path("DeleteExam/<int:pk>",views.DeleteExam,name="DeleteExam"),
    path("Examexperyupdate/<int:pk>",views.Examexperyupdate,name="Examexperyupdate"),
    path("DeleteQuestion/<int:pk>",views.DeleteQuestion,name="DeleteQuestion"),
    path("StudentExams",views.StudentExams,name="StudentExams"),
    path("AttendtheExam/<int:pk>",views.AttendtheExam,name="AttendtheExam"),
    path("EneterExamination/<int:pk>",views.EneterExamination,name="EneterExamination"),
    path("calculate_marks",views.calculate_marks,name="calculate_marks"),
    path("ExamCompleted",views.ExamCompleted,name="ExamCompleted"),
    path("StudentMarkView",views.StudentMarkView,name="StudentMarkView"),
        
] 