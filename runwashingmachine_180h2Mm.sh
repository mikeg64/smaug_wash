#!/bin/bash
#$ -j y
#$ -V 
#$ -l arch=intel*
##$ -l gpu=1,gpu_arch=nvidia-k40m
#$ -l gpu=1,gpu_arch=nvidia-m2070

##$ -P cs-test
#$ -P mhd
##$ -P gpu
#$ -N washingmachine
#$ -l mem=12G
#$ -l rmem=12G
#$ -l h_rt=168:00:00
module add libs/cuda/6.5.14

#cp solarmodels/Makefile.spicule src/Makefile
#cp solarmodels/make_inputs.spicule src/make_inputs
#cp solarmodels/iosac2.5d.cpp.spicule src/iosac2.5d.cpp


#cd src
#make clean
#make smaug
#cd ..

cd include
cp iosac2.5dparams.washing_mach_180.h iosmaugparams.h
cd ..

cd src
cp usersource.washing_mach_180.cu usersource.cu
#cp boundary_3d.cu boundary.cu
make clean
make -f Makefile_3d smaug
cd ..



export TIMECOUNTER=0
source timeused
bin/smaug a
source timeused

