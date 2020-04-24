FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:8000", "-w", "4", "run:app"]