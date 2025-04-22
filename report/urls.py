from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name= 'login'),
    path('home', views.home, name='home'),
    path('report',views.report,name = "report"),
    path('logout',views.logout,name = "logout"),
    path('student',views.student, name="student"),
    path('student_report',views.student_report, name="student_report"),
 ]