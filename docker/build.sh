#!/bin/bash

orange=`tput setaf 3`
reset_color=`tput sgr0`

ARCH=`uname -m`
NUM_THREADS=`nproc`

cd "$(dirname "$0")"
root_dir=$PWD 
cd $root_dir

/bin/bash context.sh

echo "Building for ${orange}${ARCH}${reset_color}"
echo "Building is carried out in ${orange} ${NUM_THREADS} threads${reset_color}"

docker build . \
    -f $root_dir/Dockerfile_bridge \
    --build-arg UID=$(id -u) \
    --build-arg GID=$(id -g) \
    --build-arg NUM_THREADS=${NUM_THREADS} \
    -t ${ARCH}foxy/semseg_m2f:latest
