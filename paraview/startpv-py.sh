#!/bin/bash


#$ -l mem=16G
#$ -l rmem=16G
#$ -N con2h5
#$ -j y
##$ -t 5-8:1
##$ -V 

#$ -l h_rt=8:00:00


#start the pvpython

singularity exec    /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvpython streamandslice-extract-jpg-loop.py


