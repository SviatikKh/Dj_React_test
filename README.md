# Dj_React_test

Docker:
Backend:
https://hub.docker.com/repository/docker/sviatikkh/dj_react_test

Frontend:
https://hub.docker.com/repository/docker/sviatikkh/dj_react_frontend

Start App:

1. Clone App from github: git clone https://github.com/SviatikKh/Dj_React_test
2. cd dj_react
3. activate your virtual environment
4. pip install -r requirements.txt
5. manage.py makemigrations; manage.py migrate
6. manage.py runserver
7. cd dj_react/frontend
8. npm start
<br>
If you want to start app with docker
<br>
9. https://hub.docker.com/repository/docker/sviatikkh/dj_react_test
<p>9.1. docker pull sviatikkh/dj_react_test</p>
10. https://hub.docker.com/repository/docker/sviatikkh/dj_react_frontend
<p>10.1. docker pull sviatikkh/dj_react_frontend</p>
11. docker-compose run dj_react_test
12. docker-compose run dj_react_frontend


 

