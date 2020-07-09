# zulu-in-django
zulu in django
installation:
1. run $ sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
2. open virtual environment
3. install the requirements file
4. do $python manage.py runserver
5. enter the site: http://localhost:8000/
enjoy

6. run the line:
7. echo "from django.contrib.auth.models import User; User.objects.create_superuser('myadmin', 'myemail@example.com', 'hunter2')" | python manage.py shell
8. to create a user for the admin site with:

9. username: myadmin
10. password: hunter2
