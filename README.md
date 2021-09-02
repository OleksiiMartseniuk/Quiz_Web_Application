 # Quiz Web Application
 It is django based quiz app for multiple choice questions.

 ## Current features

* Login / Register
* Administrator appointment
* Adding quizzes via Excel file
* Storing of quiz results under each user
* User rating
* User profile
* Reset rating
* Deleting a separate report for each passed quiz
* Log out of profile

## Snaps of project
Login:
![][login]

Registration:
![][registration]

Home:
![][home]

Quiz:
![][quiz1]
![][quiz2]

Result:
![][result]

Profile:
![][profile]

Rating:
![][rating]

Uplioad-file (The page is available only to the administrator):
![][uplioad_file]

[uplioad_file]:./screenshots/uplioad-file.png 
[rating]: ./screenshots/rating.png
[profile]: ./screenshots/profile.png
[result]: ./screenshots/result.png
[quiz2]: ./screenshots/quiz2.png
[quiz1]: ./screenshots/quiz1.png
[home]: ./screenshots/home.png
[registration]: ./screenshots/registration.png
[login]: ./screenshots/authorization.png

# Instructions

1. ## Installations

Make sure to have python version 3 install on you pc or laptop.
<br>
**Clone repository**
<br>
`https://github.com/OleksiiMartseniuk/Quiz_Web_Application.git`

2. ## Installing dependencies

It will install all required dependies in the project.
<br>
`pip install -r requirements.txt`

2. ## Migrations

To run migrations.
<br>
`python manage.py migrate`

3. ## Create superuser
   
To create super user run.
<br>
`python manage.py createsuperuser`
<br>
After running this command it will ask for username, password. You can access admin panel from
<br>
`localhost:8000/admin/`

4. ## Running locally

To run at localhost. It will run on port 8000 by default.
<br>
`python manage.py runserver`
