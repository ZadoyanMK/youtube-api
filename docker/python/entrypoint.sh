#!/usr/bin/env bash


while ! nc -z mysql 3306;
do
    echo "waiting for db";
    sleep 5;
done;
while ! nc -z rabbitmq 5672;
do
    echo "waiting for rabbitmq";
    sleep 5;
done;

echo Connected!;

python manage.py makemigrations
python manage.py migrate
echo "Running command '$*'"
exec su -p - ${PYTHON_RUN_USER} -s /bin/bash -c "$*"