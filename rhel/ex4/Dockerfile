FROM registry.access.redhat.com/ubi8/python-38

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "src/main.py"]
