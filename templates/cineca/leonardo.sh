#!/bin/bash

#SBATCH --job-name=cj
#SBATCH --account=IscrC_HOPE_0
#SBATCH --partition=boost_usr_prod
#SBATCH --time=00:05:00
#SBATCH --error=cj.err
#SBATCH --output=cj.out


source ${HOME}/venv/bin/activate


{{ streamflow_command }}

