#!/bin/bash

#SBATCH --job-name=cj
#SBATCH --time=00:10:00
#SBATCH --error=cj.err
#SBATCH --output=cj.out

source ${HOME}/test-environment/bin/activate

{{ streamflow_command }}