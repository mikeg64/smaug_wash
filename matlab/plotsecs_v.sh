#!/bin/bash
#$ -j y
#$ -V 
#$ -N plotsecs_v 
#$ -l mem=12G
#$ -l rmem=12G
##$ -l h_rt=8:00:00
##module add libs/cuda/4.0.17
#module add libs/cuda/6.5.14
module load apps/matlab/2018b

#export TIMECOUNTER=0
#source timeused
   matlab -nosplash -r "plotsecs_array_v"
#source timeused

