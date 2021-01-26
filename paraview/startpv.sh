#!/bin/bash

#start the pvserver
echo $SSH_CLIENT | awk '{ print $1}'

echo 'starting pvserver on' $SSH_CLIENT
#singularity --net --network-args “portmap=11111:11111/tcp” shell /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvserver --use-offscreen-rendering -rc --client-host=`echo $SSH_CLIENT | awk '{ print $1}'`

# singularity run /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvserver --use-offscreen-rendering -rc --client-host=172.16.200.7


#singularity exec  --net --network=none --network-args "portmap=11111:11111/tcp"  /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvserver --use-offscreen-rendering -rc --client-host=172.16.201.44


singularity exec  --net --network=none --network-args "portmap=11111:11111/tcp"  /usr/local/packages/singularity/images/paraview/pv-v5.7.1-osmesa-py3.simg  pvserver -rc --client-host=172.16.201.44



