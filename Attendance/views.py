from django.shortcuts import render, redirect
from .models import Student, Attendance
from django.contrib import messages
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('student_list')
    
    return render(request, 'attendance/student_list.html', {
        'students': students,
        'form': form
    })

def take_attendance(request):
    students = Student.objects.all()
    
    if request.method == 'POST':
        date = request.POST.get('date')
        
        for student in students:
            status = request.POST.get(f'student_{student.id}')
            
            if status in ['present', 'absent']:
                Attendance.objects.update_or_create(
                    student=student,
                    date=date,
                    defaults={'is_present': status == 'present'}
                )
        
        messages.success(request, "Attendance submitted successfully.")
        return redirect('attendance_report')
    
    return render(request, 'attendance/take_attendance.html', {'students': students})

def attendance_report(request):
    records = Attendance.objects.select_related('student').order_by('-date', 'student__roll_number')
    return render(request, 'attendance/attendance_report.html', {'records': records})