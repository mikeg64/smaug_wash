#!/bin/bash


#$ -l mem=8G
#$ -l rmem=8G
#$ -N con2h5
#$ -j y
##$ -t 5-8:1
##$ -V 

#$ -l h_rt=8:00:00


#start the pvpython

#singularity exec    /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvpython stream_contour_extract_jpg_loop-linesource.py

#singularity exec    /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvpython hello.py


singularity exec    /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvpython velslice_magtotslice_extract_saus_z_jpg_loop.py
