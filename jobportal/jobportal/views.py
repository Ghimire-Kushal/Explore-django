from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')  
def student_list(request):
    students = Student.objects.select_related("course").all()

    context = {
        "students": students,
        "student_count": students.count(),
    }

    return render(request, "students.html", context)


def course_list(request):
    courses = Course.objects.prefetch_related("students").all()

    context = {
        "courses": courses,
        "course_count": courses.count(),
    }

    return render(request, "courses.html", context)


def attendance_list(request):
    attendance_records = Attendance.objects.select_related(
        "student",
        "student__course",
    ).all()

    context = {
        "attendance_records": attendance_records,
        "attendance_count": attendance_records.count(),
    }

    return render(request, "attendance.html", context)