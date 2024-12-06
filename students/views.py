from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# View to display all students
def index(request):
    students = Student.objects.all()  # Get all students
    return render(request, 'students/index.html', {
        'students': students
    })

# View to display a single student's details
def view_student(request, id):
    student = get_object_or_404(Student, pk=id)  # Safer method to get student by id
    return render(request, 'students/view_student.html', {
        'student': student  # Pass student details to the template
    })

# View to add a new student
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)  # Initialize form with POST data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the new student (ModelForm handles the creation)
            return HttpResponseRedirect(reverse('index'))  # Redirect to index page after success
    else:
        form = StudentForm()  # Initialize an empty form
    return render(request, 'students/add.html', {
        'form': form  # Pass the form to the template
    })

# View to edit an existing student
def edit(request, id):
    student = get_object_or_404(Student, pk=id)  # Safer method to get student by id
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  # Populate form with existing student data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the updated student details
            return HttpResponseRedirect(reverse('index'))  # Redirect to index page after success
    else:
        form = StudentForm(instance=student)  # Pre-fill the form with existing student data
    return render(request, 'students/edit.html', {
        'form': form,  # Pass the form to the template
        'student': student  # Pass student details (optional)
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))


