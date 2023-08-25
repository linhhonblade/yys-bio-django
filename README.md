Command to build docker image
```shell
docker build -t yys_django:tag .
```

Command to run image first time with migrate and loaddata
```shell
docker run --network host --env-file .env yys_django:v0 sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py loaddata */fixtures/*"
```

Command to collect static files
```shell
docker run --env-file .env yys_django:v0 sh -c "python manage.py collectstatic --noinput"
```

Command to up service
```shell
docker run --env-file env -p 80:8000 yys_django:v0
```

