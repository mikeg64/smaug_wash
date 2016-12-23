#!/bin/bash
#$ -j y
#$ -V 
#$ -l arch=intel*
##$ -l gpu=1,gpu_arch=nvidia-k40m
#$ -l gpu=1,gpu_arch=nvidia-m2070

##$ -P cs-test
##$ -P mhd
#$ -P gpu
#$ -N washm_mov1
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
cp iosmaugparams.washing_mach_mov1_h12p5Mm_kg.h iosmaugparams.h
cp initialisation_user.h.wash_180 initialisation_user.h
cd ..

#rm bin/iosmaug.o
cd src
cp usersource.washing_mach_mov1_h12p5Mm_kg.cu usersource.cu

cp boundary_3d.cu boundary.cu
make clean
#rm centdiff1.o
#rm centdiff2.o
make -f Makefile_3d smaug
#make -f Makefile_3d_k40 smaug
cd ..



export TIMECOUNTER=0
source timeused
#bin/smaug a init
bin/smaug a
source timeused

