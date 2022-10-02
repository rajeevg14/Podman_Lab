FROM docker.io/continuumio/miniconda3


COPY . .


# Create the environment:
RUN conda update -n base -c defaults conda
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["/conda", "run", "-n", "opence_env", "/bin/bash", "-c"]

# The code to run when container is started:
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "opence_env", "python", "main.py"]
