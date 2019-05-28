FROM python:3.7

COPY ./src /src

WORKDIR /src

RUN pip install --no-cache-dir -r requirements/dev.txt

COPY ./docker/dev_windows/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]