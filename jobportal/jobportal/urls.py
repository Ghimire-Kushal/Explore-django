"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

# The URL patterns map routes to the corresponding views in the jobportal application.
# Each path associates a URL with the view function that handles the request.
urlpatterns = [
    # Application URL configuration.
    # Keep route comments close to the paths they describe.
    # Clear route notes make future maintenance easier.
    # Group related endpoints together for easier navigation.
    # Keep this module focused on route declarations.
    # Routes are evaluated from top to bottom.
    # Keep specific routes above broader fallback routes.
    # Core application routes.
    # Django administration route.
    path('admin/', admin.site.urls),
    # Public landing page.
    # The root route serves the main application entry point.
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # Student directory route.
    # Student and course management routes.
    path('students/', views.student_list, name='students'),
    # Course catalog route.
    path('courses/', views.course_list, name='courses'),
    # Attendance tracking route.
    path('attendance/', views.attendance_list, name='attendance'),

    # Development-only live reload route.
    path('__reload__/', include('django_browser_reload.urls')),

]
