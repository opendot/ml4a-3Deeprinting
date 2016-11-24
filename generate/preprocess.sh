#!/bin/bash

base_dir=$(realpath $1)
base_name="$2"

exec docker run --rm -it -v "$base_dir":/data crisbal/torch-rnn:base python scripts/preprocess.py --input_txt "/data/${base_name}.stl" --output_h5 "/data/${base_name}.h5" --output_json "/data/${base_name}.json"
