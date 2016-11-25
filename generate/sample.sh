#!/bin/bash

input="$1"
if [ -z "$input" ]; then
    echo sample: specify the stl filename
    exit 1
fi
base_dir=$(realpath $(dirname "$input"))
file_name=$(basename "$input")
base_name=${file_name%%.*}
extension=${file_name##*.}
checkpoint="$2"
if [ -z "$checkpoint" ]; then
    echo sample: specify the checkpoint number
    exit 1
fi
length="$3"
if [ -z "$length" ]; then
    echo sample: specify the length of the file to generate
    exit 1
fi
image=$(cat image.conf)

exec docker run --rm -it -v "$base_dir":/data "$image" th sample.lua -checkpoint "/data/${base_name}-checkpoint_${checkpoint}.t7" -length "$length" -gpu -1
