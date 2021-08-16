FROM python:3

RUN apt-get update

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /code/

RUN pip install -r /code/requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]