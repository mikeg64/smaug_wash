#!/bin/bash
#$ -j y
#$ -V 
#$ -N plotsecs 
#$ -l mem=12G
#$ -l rmem=12G
##$ -l h_rt=8:00:00
##module add libs/cuda/4.0.17
#module add libs/cuda/6.5.14
module load apps/matlab/2020a/binary

#export TIMECOUNTER=0
#source timeused
#   matlab -nosplash -r "plotsecs_densslice_vecarrows_array"
   matlab -nosplash -nodisplay -r "plotsecs_magfield_array"
#source timeused

