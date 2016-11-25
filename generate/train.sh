#!/bin/bash

input="$1"
if [ -z "$input" ]; then
    echo "train: specify the stl filename"
    exit 1
fi
base_dir=$(realpath $(dirname "$input"))
file_name=$(basename "$input")
base_name=${file_name%%.*}
extension=${file_name##*.}
checkpoint_every="$2"
if [ -z "$checkpoint_every" ]; then
    checkpoint_every=1000
    echo "train: checkpoining every $checkpoint_every iterations"
fi
image=$(cat image.conf)

exec docker run --rm -it -v "$base_dir":/data "$image" th train.lua -input_h5 "/data/${base_name}.h5" -input_json "/data/${base_name}.json" -gpu -1 -checkpoint_every "$checkpoint_every" -checkpoint_name "/data/${base_name}-checkpoint"
