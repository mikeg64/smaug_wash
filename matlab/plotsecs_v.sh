#!/bin/bash
#$ -j y
#$ -V 
#$ -N pvert 
#$ -l mem=16G
##$ -l rmem=24G
#$ -l h_rt=14:00:00
##module add libs/cuda/4.0.17
#module add libs/cuda/6.5.14
#module load apps/matlab/2018b
module load apps/matlab/2018b/binary

#export TIMECOUNTER=0
#source timeused
   matlab -nosplash -r "pvertvvt"
#source timeused

