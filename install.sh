#!/bin/sh

conda create -n myenv python=3.6.9
conda init bash
bash
conda activate myenv
pip install -r requirements.txt