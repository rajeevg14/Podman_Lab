FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN /opt/app-root/bin/python3.9 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


ENTRYPOINT [ "python" ]

CMD [ "src/main.py" ]
