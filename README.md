
# Django Student Marksheet

A web application built with Django to manage and display student marksheets. It allows teachers to input student details and their respective marks, generate marksheet reports, and enables students to view their academic performance.
---
## Live Demo
Check out the project here [Demo 🡕](https://www.salankatuwal.com.np/marksheet.html)
---
## How It Works

1. **Login as Teacher or Student**:
     - Teachers log in using superuser credentials.
     - Students can directly access their marksheets without credentials.
     ![Login Page](/photos/login.png)

2. **Invalid Login**:
     - Displays an alert message if login credentials are incorrect.
     ![Invalid Login](/photos/login2.png)

3. **Teacher Dashboard**:
     - Teachers can input student details and marks.
     ![Teacher Dashboard](/photos/home.png)

4. **Marksheet Generation**:
     - Successfully generates a marksheet after inputting valid details.
     ![Marksheet](/photos/marsheet.png)

5. **Error Handling**:
     - Displays an error if the same marksheet is uploaded twice.
     ![Duplicate Marksheet Error](/photos/samemarksheet.png)

6. **Failing Students**:
     - Marksheets for failing students are highlighted in red.
     ![Failing Marksheet](/photos/Fail.png)

7. **Student Access**:
     - Students can search for their marksheets using their symbol number and school name.
     - Displays an error if the details do not match.
     ![Student Search Error](/photos/searchfail.png)

8. **Successful Search**:
     - Displays the marksheet if the details match.
     ![Student Marksheet](/photos/student.png)

---

## Features

- **Role-Based Login**: Teachers can log in using superuser credentials, while students can access their marksheets without registration.
- **Subject Management**: Supports five subjects: English, Math, Nepali, Science, and Health.
- **Marksheet Generation**: Teachers can input student details (name, symbol number, date of birth, school name, exam year, and marks) to generate marksheets.
- **Error Handling**: Includes robust validation to handle:
    - Negative marks
    - Marks greater than 100
    - Non-numeric input for marks
    - Duplicate symbol numbers
- **Access Control**: Home and report pages are restricted to logged-in users.
- **Teacher Features**: Teachers can log out or navigate to the student page to view marksheets.
- **Student Features**: Students can search for their marksheets using their symbol number and school name.

---

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/SalanKatuwal/django-student-marksheet.git
     cd django-student-marksheet
     ```

2. Apply migrations:
     ```bash
     python manage.py migrate
     ```

3. Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```

4. Run the development server:
     ```bash
     python manage.py runserver
     ```

---

## Usage

1. Log in to the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) using superuser credentials.
2. Log in as a teacher from the home page.
3. Add student profiles and their respective marks.
4. Students can view their marksheets by entering their symbol number and school name on the student page.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

---

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Python Documentation](https://docs.python.org/3/)

---

