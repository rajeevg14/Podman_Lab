FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /src

RUN /opt/app-root/bin/python3.9 -m pip install --upgrade pip

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "src/FMTensorFlowCNN_inference.py" ]