#!/bin/bash

input="$1"
if [ -z "$input" ]; then
    echo train: specify the stl filename
    exit 1
fi
base_dir=$(realpath $(dirname "$input"))
base_name=$(basename "$input" .stl)

exec docker run --rm -it -v "$base_dir":/data crisbal/torch-rnn:base th train.lua -input_h5 "/data/${base_name}.h5" -input_json "/data/${base_name}.json" -gpu -1 -checkpoint_every 100 -checkpoint_name "/data/${base_name}-checkpoint"
