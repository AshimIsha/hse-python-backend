FROM python:3.9.5 as base

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y \
    && mkdir /app

COPY ./* /app

WORKDIR ./app

RUN pip install -r ./requirements.txt

EXPOSE 8080
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

FROM base as dev
CMD ["bash", "-c", "while true; do sleep 1; done"]

FROM base as local
ENTRYPOINT ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]
