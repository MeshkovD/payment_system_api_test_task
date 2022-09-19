FROM python:3-onbuild

EXPOSE 8000

RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py create_demo


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
