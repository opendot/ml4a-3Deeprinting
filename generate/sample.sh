#!/bin/bash

input="$1"
if [ -z "$input" ]; then
    echo sample: specify the stl filename
    exit 1
fi
base_dir=$(realpath $(dirname "$input"))
base_name=$(basename "$input" .stl)
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

exec docker run --rm -it -v "$base_dir":/data crisbal/torch-rnn:base th sample.lua -checkpoint "/data/${base_name}-checkpoint_${checkpoint}.t7" -length "$length" -gpu -1
