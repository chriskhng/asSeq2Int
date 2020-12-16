#!/bin/bash
#SBATCH -t 01:30:00 # 90 minutes
#SBATCH --mem=5g
#SBATCH --output=SeqHitReadOut.%J.txt

./main.sh


