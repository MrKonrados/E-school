from django.shortcuts import render, get_list_or_404, redirect

from .forms import StudentForm, StudentGradeForm
from .models import Student, SchoolGrade

def student_create_or_edit(request, pk=None):
    if pk == None:
        student = Student()
    else:
        student = get_list_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            return redirect('student_detail', student_id=student)

    else:
        form = StudentForm(instance=student)
        subject_forms = [StudentGradeForm(instance=instance) for instance in SchoolGrade.objects.all()]

    return render(request, 'student_form.html', {'form': form, 'subject_forms': subject_forms, })