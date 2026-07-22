from django.contrib import admin

from .models import Attendance, Course, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "duration")
    search_fields = ("code", "name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "full_name",
        "email",
        "course",
        "enrolled_on",
    )
    list_filter = ("course", "enrolled_on")
    search_fields = ("student_id", "full_name", "email")


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "status")
    list_filter = ("status", "date")
    search_fields = (
        "student__student_id",
        "student__full_name",
    )
    date_hierarchy = "date"