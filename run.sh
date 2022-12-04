#!/bin/sh
#BSUB -J StarganPhoneHome
#BSUB -o outputs/StarganPhoneHome/%J.out
#BSUB -e outputs/StarganPhoneHome/%J.err
#BSUB -q gpua100
#BSUB -n 1
#BSUB -R "rusage[mem=30G]"
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

CUDA_LAUNCH_BLOCKING=1 python src/stargan/train.py --config_path ./src/Configs/config.yml