FROM conda/miniconda3

WORKDIR /src

RUN conda install -c conda-forge pyomo
RUN conda install -c conda-forge ipopt glpk

COPY . .

CMD ["python", "src/main.py"]
