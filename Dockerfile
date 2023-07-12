FROM python:3.11.4-alpine3.17
WORKDIR /code
COPY ./requirements ./requirements
RUN addgroup worker && \
    adduser -G worker --no-create-home --disabled-password worker && \
    pip install --no-cache-dir --upgrade -r ./requirements
COPY ./app ./app
RUN chown worker:worker -R ../code
USER worker
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
