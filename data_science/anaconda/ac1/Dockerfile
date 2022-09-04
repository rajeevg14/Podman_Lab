FROM docker.io/continuumio/miniconda3:latest
WORKDIR /app
# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml
# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
RUN conda update -n base -c defaults conda
RUN conda clean --all
RUN conda config --show channels
# The code to run when container is started:
COPY run.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "run.py"]