from django.forms import ModelForm
from .models import Question

class QuestionCreationForm(ModelForm):
    class Meta:
        model = Question
        fields = ["marks","question","option1","option2","option3","option4","answer"]