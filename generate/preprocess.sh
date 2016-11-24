#!/bin/bash

input="$1"
if [ -z "$input" ]; then
    echo preprocess: specify the stl filename
    exit 1
fi
base_dir=$(realpath $(dirname "$input"))
base_name=$(basename "$input" .stl)

exec docker run --rm -it -v "$base_dir":/data crisbal/torch-rnn:base python scripts/preprocess.py --input_txt "/data/${base_name}.stl" --output_h5 "/data/${base_name}.h5" --output_json "/data/${base_name}.json"
