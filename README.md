
# Django Student Marksheet

A web application built with Django to manage and display student marksheets. It allows teachers to input student details and their respective marks and generate the marksheet report as well as students can also view their academic performance.


## How the web app works

- Login as a techer or student depending on your role
![App Screenshot](/photos/login.png) 

- If a login credintals doesnot match then the alret message is shown in the login page
![App Screenshot](/photos/login2.png)

- If you login as a teacher then the home page is displayed where you have enter student details and marks as shown below
![App Screenshot](/photos/home.png)

- After entering the marksheet details the marksheet will be generated as follows
![App Screenshot](/photos/marsheet.png)

- If some error is occured during marksheet generation such as same marksheet uploaded twice
![App Screenshot](/photos/samemarksheet.png)

- If a student fails the exam then the marksheet will be in red color
![App Screenshot](/photos/Fail.png) 

- You donot need to enter any credentials to login as a student
![App Screenshot](/photos/student.png) 

- From the student page you can simply search the marksheet by entering your marksheet if the student marksheet doesnot exist then the error message will be shown
![App Screenshot](/photos/searchfail.png) 

- If the student details match then the same marksheet will be uploaded

## Features

- Handle the login properly only the superuser can login as a teacher
- No registration is required to login as a student
- Five subjects: English, Math, Nepali, Science and Health are given
- Teacher have to enter Stuent name, symbol number, data of birth, school name, exam year and mark of 5 subject for marksheet generation
- During marksheet generation various conditions are handled using try... catch... exception such as
    - Negative mark cannot be entered
    - Mark greater than 100 cannot be entered
    - String cannot be entered as a student mark
    - The symbol number cannot be entered twice
    - The user cannot access the home page or report page both requires login
- There is a 'logout' option for teacher in the home page as well as there is 'see student marksheet' button which will redirect teacher to student page
- Student can only see the marksheet only if the marksheet exist in the database

## Installation

Clone the repository

```bash
git clone https://github.com/SalanKatuwal/django-student-marksheet.git
cd django-student-marksheet
```
Apply migrations
```bash
python manage.py migrate
```
Create the super user
```bash
python manage.py createsuperuser
```
Run the development server
```bash
python manage.py runserver
```
## Usage

- Log in to the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.
- Login as a teacher at home page 
- Add student profiles and their respective marks.
- Students can view their marksheets by login as a student from the home page and entering their Symbol Number and School Name

## Contributing

Contributions are always welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you'd like to change.


## Acknowledgements

 - [Django Documentation](https://docs.djangoproject.com/en/5.2/)
 - [Python](https://docs.python.org/3/)


