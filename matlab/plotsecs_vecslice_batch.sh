#!/bin/bash

#$ -l mem=16G
#$ -l rmem=16G
#$ -N psecs_vecs
#$ -j y
#$ -t 5-8:1
#$ -V  
#$ -l h_rt=8:00:00


##module add libs/cuda/4.0.17
#module add libs/cuda/6.5.14
module load apps/matlab/2014a


#export TIMECOUNTER=0
#source timeused
   matlab -nosplash -r "plotsecs_vecslice_vecarrows_array_batch"
#source timeused
