FROM python:3.8
MAINTAINER ryuneeee@gmail.com

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "app:app"]