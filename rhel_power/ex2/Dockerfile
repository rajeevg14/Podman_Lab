FROM registry.access.redhat.com/ubi8/python-38

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# set default flask app and environment
ENV FLASK_APP flaskr
ENV FLASK_ENV development

# This is primarily a reminder that we need access to port 5000
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "src/main.py" ]
