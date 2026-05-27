FROM python:latest

COPY cliente.py .

RUN pip install flask
RUN pip install requests

EXPOSE 5005

CMD [ "python", "cliente.py" ]