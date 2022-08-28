FROM docker.io/continuumio/miniconda3:latest
WORKDIR /app
# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml
# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
RUN conda clean --all
RUN conda install -c conda-forge pyomo
RUN conda install -c conda-forge ipopt glpk
# The code to run when container is started:
COPY run.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "run.py"]