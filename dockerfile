FROM python:3.12.8

WORKDIR /devtools_task
COPY ./requirements.txt /devtools_task/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /devtools_task/requirements.txt
RUN pip install fastapi uvicorn
RUN chmod +x deployment-service
COPY ./main.py /devtools_task/main.py
#
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]