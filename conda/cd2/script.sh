#!/bin/sh

/root/anaconda3/bin/conda update -n base -c defaults conda
/root/anaconda3/bin/conda --version
/root/anaconda3/bin/conda list
/root/anaconda3/bin/conda config --prepend channels https://ftp.osuosl.org/pub/open-ce/current/
/root/anaconda3/bin/conda config --show channels
/root/anaconda3/bin/conda init bash
/root/anaconda3/bin/conda create --name opence_env python=3.9
/root/anaconda3/bin/conda activate opence_env
/root/anaconda3/bin/conda info --envs
/root/anaconda3/bin/conda env list
/root/anaconda3/bin/conda config --env --set always_yes true
/root/anaconda3/bin/conda install numba
/root/anaconda3/bin/conda install -c conda-forge pycuda
/root/anaconda3/bin/conda install -c conda-forge nvidia cudatoolkit
/root/anaconda3/bin/conda install -c conda-forge cupy cudnn cutensor nccl
