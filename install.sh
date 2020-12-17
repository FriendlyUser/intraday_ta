#!/bin/sh

conda create -n myenv python=3.6.9
conda init bash
bash
conda activate myenv
conda install -c conda-forge voila
pip install numpy
pip install -r requirements.txt