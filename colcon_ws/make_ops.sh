#!/bin/bash

export CUDA_HOME="/usr/local/cuda-11.3"
cd ./src/semseg/mask2former/modeling/pixel_decoder/ops
sh make.sh
cd ../../../..
