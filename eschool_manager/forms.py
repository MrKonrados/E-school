from django.forms import ModelForm
from .models import Student, SchoolGrade, SchoolSubject


class StudentGradeForm(ModelForm):
    class Meta:
        model = SchoolGrade
        exclude = ['pk', 'student']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['pk']
