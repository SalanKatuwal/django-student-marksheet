from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.

def student_report(request):
    if request.session.get('entry') == 'student':
        symbol_number = request.session.get('symbol_number')
        try:
            student = Student.objects.get(symbol_number=symbol_number)
            request.session['subject'] = ['english', 'math', 'nepali', 'science', 'health']
            marks = [student.english, student.math, student.nepali, student.science, student.health]
            data = {
                'student': student,
                'marks': marks
            }
            return render(request, 'report.html', data)
        except Student.DoesNotExist:
            messages.info(request, 'Student not found')
            return redirect('home') 
    else:
        return redirect('login')

def student(request):
    if request.user.is_authenticated:
        request.session['identity'] = 'teacher'
    else:
        request.session['identity'] = 'student'
    if request.method == 'POST':
        symbol_number = request.POST.get('symbol_number')
        school_name = request.POST.get('school_name')
        if Student.objects.filter(symbol_number = symbol_number, school_name = school_name).exists():
                request.session['symbol_number'] = symbol_number
                request.session['entry'] = 'student'
                return redirect('student_report')
        else:
            messages.info(request, 'The student marksheet does not exist')
            return redirect('student')
    entry = request.session.pop('entry', None)
    symbol_number = request.session.pop('symbol_number', None)
    return render(request,'student.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'You are not authorized to access this page.')
                return redirect('login')
        else:  
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    if request.user.is_authenticated:   
        return redirect('home')
    return render(request, 'login.html')

@login_required(login_url='login')
def report(request):   
    if request.method == 'POST':
        # Handle form submission here
        try:
            name = request.POST.get('name')
            date_of_birth = request.POST.get('date_of_birth')
            symbol_number = request.POST.get('symbol_number')
            school_name = request.POST.get('school_name')
            exam_year = int(request.POST.get('exam_year'))
            english = float(request.POST.get('english'))
            math = float(request.POST.get('math'))
            nepali = float(request.POST.get('nepali'))
            science = float(request.POST.get('science'))
            health = float(request.POST.get('health'))
            marks = [english, math, nepali, science, health]
            total = sum(marks)
            if any(m < 0 for m in marks):
                raise ValueError("Marks cannot be negative")
            if any(m > 100 for m in marks):
                raise ValueError("Marks cannot be greater than 100")

            percentage = (total / 500) * 100
            
            if any(m < 40 for m in marks):
                grade = 'Fail'
            elif percentage >= 80:
                grade = 'Distinction'
            elif percentage >= 70:
                grade = 'First Division'
            elif percentage >= 60:
                grade = 'Second Division'
            elif percentage >= 50:
                grade = 'Third Division'
            elif percentage >= 40:
                grade = 'Just pass'
            else:
                grade = 'Fail'
            
            if Student.objects.filter(symbol_number = symbol_number).exists():
                messages.info(request , 'The student marksheet already exists')
                return redirect('home')
            Student.objects.create(
                name = name,
                date_of_birth= date_of_birth,
                symbol_number = symbol_number,
                school_name= school_name,
                exam_year= exam_year,
                english= english,
                math= math,
                nepali= nepali,
                science= science,
                health= health,
                total= total,
                percentage= percentage,
                grade= grade
            )
            request.session['entry'] = 'teacher'
            request.session['subject']= ['english', 'math', 'nepali', 'science', 'health']
            request.session['symbol_number'] = symbol_number
            return redirect('report')
        except ValueError as e:
            if str(e) == "Marks cannot be negative":
                messages.info(request, 'Marks cannot be negative')
            elif str(e) == "Marks cannot be greater than 100":
                messages.info(request, 'Marks cannot be greater than 100')
            else:
                messages.info(request, 'Please enter valid marks')
            return redirect('home')
        except Exception as e:
            messages.info(request, 'Please enter valid marks')
            return redirect('home')
    symbol_number = request.session.get('symbol_number')
    if not symbol_number:
        messages.info(request, 'Please enter the marks first')
        return redirect('home')
    try:
        student = Student.objects.get(symbol_number=symbol_number)
        marks = [student.english, student.math, student.nepali, student.science, student.health]
        data = {
            'student': student,
            'marks': marks
        }
        return render(request, 'report.html', data)
    except Student.DoesNotExist:
        messages.info(request, 'Student not found')
        return redirect('home')
        

@login_required(login_url='login')
def home(request):
    symbol_number = request.session.pop('symbol_number',None)
    return render(request,'home.html')

def logout(reqeust):
    auth.logout(reqeust)
    return redirect('login')