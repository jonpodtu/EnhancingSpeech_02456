#!/bin/sh
#BSUB -J V2_DW
#BSUB -o outputs/V2_DW/%J.out
#BSUB -e outputs/V2_DW/%J.err
#BSUB -q gpua40
#BSUB -n 1
#BSUB -R "rusage[mem=12G]"
#BSUB -R "span[hosts=1]"
### -- Select the resources: 1 gpu in exclusive process mode --
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -N
#BSUB -W 24:00
# end of BSUB options

nvidia-smi
# Load the cuda module
module load cuda/11.6

# activate the virtual environment 
source .venv/bin/activate

CUDA_LAUNCH_BLOCKING=1 python src/stargan/train.py --config_path ./src/Configs/config_DW.yml