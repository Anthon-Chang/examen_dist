FROM python:latest

COPY servidor.py .

RUN pip install flask
RUN pip install requests

EXPOSE 5000

CMD [ "python", "servidor.py" ]