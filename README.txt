Superuser login:

username: sprinary
passward: sman@123!



1. Does the web application use Django to serve static HTML content?

Visit: http://127.0.0.1:8000/api/static/

2. Has the learner committed the project to a Git repository?
Visit: https://github.com/aliyuthman/LittleLemon

3. Does the application connect the backend to a MySQL database?

Check: Setting.py for database user configuration

4. Are the menu and table booking APIs implemented?

Visit Booking: http://127.0.0.1:8000/api/booking/
Visit Menu: http://127.0.0.1:8000/api/menu/


5. Is the application set up with user registration and authentication?

Visit (user registration): http://127.0.0.1:8000/auth/users/
Visit (user login authentication): http://127.0.0.1:8000/auth/token/login



6. Does the application contain unit tests?

Check Test Folder inside LittleLemon/tests

Run on terminal: python manage.py test 'LittleLemon/tests'

7. Can the API be tested with the Insomnia REST client?
Test user can be use:
For token: 8770ce3887c5d9755aeb37520854cc1088154e57
For passward fields:
    password: 11@user1
    username: test1
    email: test1@test.com
