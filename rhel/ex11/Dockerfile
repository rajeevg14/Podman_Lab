FROM docker.io/continuumio/anaconda3
WORKDIR /src
COPY src/requirements.txt src/requirements.txt
RUN pip3 install -r src/requirements.txt
RUN conda config --set channel_priority false
RUN conda update --all --yes
RUN conda install -c conda-forge/label/gcc7 glpk
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/src"
CMD [ "python3", "src/main.py"]