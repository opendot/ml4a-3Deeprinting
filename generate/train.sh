#!/bin/bash

base_dir=$(realpath $1)
base_name="$2"

exec docker run --rm -it -v "$base_dir":/data crisbal/torch-rnn:base th train.lua -input_h5 "/data/${base_name}.h5" -input_json "/data/${base_name}.json" -gpu -1 -checkpoint_every 100 -checkpoint_name "/data/${base_name}-checkpoint"
