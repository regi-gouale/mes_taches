FROM python:3.10

RUN pip install --upgrade pip
RUN pip install pipenv

ENV PROJECT_DIR /app

COPY . /${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["gunicorn", "--graceful-timeout", "5", "--chdir", "mes_taches", "app:app",  "-w", "1", "-b", "0.0.0.0:8080"]
