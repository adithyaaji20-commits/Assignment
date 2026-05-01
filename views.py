from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse ("Hello World")

def home(request):
    context = {
        'is_logged_in':False
    }
    return render (request, 'home.html',context)

def student_list (resuest):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render (resuest, 'students.html',context)

def create_student (request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        
        
        else:
            form = StudentForm()

            return render(request, 'student_app/student_form.html', {'form': form})
    
        
        

            















    



    
        

    