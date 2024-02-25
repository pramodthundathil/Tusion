from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages 
from .models import Exam, Question
from main_app.models import Course, StudentResult , Subject, Student
from .forms import QuestionCreationForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def AddanExam(request):
    subject = Subject.objects.all()
    exams = Exam.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        sub = request.POST["sub"]
        sub1 = Subject.objects.get(id = int(sub))
        exam = Exam.objects.create(exam_name = name,subject = sub1,question_number= 0,total_marks = 0)
        exam.save()
        messages.info(request,"Exam Created Please add Questions to exam")
        return redirect("AddanExam")
 
    context = {
        "subject":subject,
        "exams":exams
    }
    return render(request,"exam/examcreation.html",context)


def AddQuestionstoexam(request,pk):
    exam  = Exam.objects.get(id = pk)
    form = QuestionCreationForm()
    question = Question.objects.filter(course = exam)

    if request.method == "POST":
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.course = exam
            question.save()
            exam.question_number += 1
            exam.total_marks += question.marks
            exam.save()
            messages.info(request,"Data added...")
            return redirect("AddQuestionstoexam", pk = pk)
        
    context = {
        "form":form,
        "exam":exam,
        "question":question
    }
    return render(request,"exam/addquestions.html",context)

def DeleteExam(request,pk):
    Exam.objects.get(id=pk).delete()
    messages.info(request,"Data Deleted...")
    return redirect("HostExam")


def Examexperyupdate(request,pk):
    exam = Exam.objects.get(id = pk)
    if request.method == "POST":
        date = request.POST["date"]
        exam.expery = date
        exam.save()
        messages.info(request,"Data Saved...")
        return redirect("AddanExam")
    return redirect("AddanExam")

def DeleteQuestion(request,pk):
    question = Question.objects.get(id = pk)
    exam = question.course
    exam.question_number -= 1
    exam.total_marks -= question.marks
    exam.save()
    question.delete()
    messages.info(request,"Question Deleted....")
    return redirect("AddQuestionstoexam",pk = exam.id)


def StudentExams(request):
   
    exam = Exam.objects.all()
    context = {
        "exam":exam
    }
    return render(request,"exam/studentexam.html",context)
   
def AttendtheExam(request,pk):
    exam = Exam.objects.get(id  = pk)
    if StudentResult.objects.filter(student = Student.objects.get(admin = request.user),exam = exam.id ).exists():
        text = ''''
        <h1 style='color:blue;text-align:center'>
        You Already attended this exam please go to
        <a href="/student/home/" style='padding:10px 20px;border-radius:10px;background-color:red;color:white'>Exam Home</a>
        </h1>
        '''
        return HttpResponse(text)

    context = {
        "exam":exam
    }
    return render(request,"exam/examattenstart.html",context)

def EneterExamination(request,pk):
    exam = Exam.objects.get(id = pk)
    questions = Question.objects.filter(course = exam)


    context = {
        "exam": exam,
        "questions":questions
    }
    if request.method=='POST':
        pass
    response= render(request,"exam/Examination.html",{'course':exam,'questions':questions})
    response.set_cookie('course_id',exam.id)
    return response

@csrf_exempt
def calculate_marks(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        exam=Exam.objects.get(id=course_id)
        
        total_marks=0
        questions= Question.objects.all().filter(course=exam)
        for i in range(len(questions)):
            
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = Student.objects.get(admin = request.user)
        result = StudentResult.objects.create(student = student,subject = exam.subject ,exam = exam.id,test= total_marks)
        result.save()
        return redirect("ExamCompleted")
    return redirect("StudentExams")

def ExamCompleted(request):
    return render(request,"exam/examcompleted.html")


def StudentMarkView(request):
    student = Student.objects.get(admin = request.user)
    mark = StudentResult.objects.filter(student = student)
    exams = []
    for i in mark:
        ex = Exam.objects.get(id = int(i.exam))
        exams.append(ex)

    print(exams,"--------------------------------")
    context = {
        "mark":mark,
        "exams":exams
    }
    return render(request,"exam/studentmarkview.html",context)
