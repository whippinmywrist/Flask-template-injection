FROM python:3.10-rc-alpine

RUN pip install flask

COPY app.py ./

EXPOSE 5000

ENTRYPOINT python -u app.py