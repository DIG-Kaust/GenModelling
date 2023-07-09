#!/bin/bash
# 
# Installer for package
# 
# Run: ./install.sh
# 

echo 'Creating normalizing_flows environment'

# create conda env
conda env create -f environment.yml
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate normalizing_flows
conda env list
echo 'Created and activated environment:' $(which python)

# check cupy works as expected
echo 'Checking cupy version and running a command...'
python -c 'import cupy as cp; print(cp.__version__); import torch; print(torch.__version__);  print(torch.cuda.get_device_name(torch.cuda.current_device())); print(torch.ones(10).to("cuda:0"))'

echo 'Done!'

