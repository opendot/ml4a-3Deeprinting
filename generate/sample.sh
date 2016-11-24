#!/bin/bash

base_dir=$(realpath $1)
base_name="$2"
checkpoint="$3"
length="$4"

exec docker run --rm -it -v "$base_dir":/data crisbal/torch-rnn:base th sample.lua -checkpoint "/data/${base_name}-checkpoint_${checkpoint}.t7" -length "$length" -gpu -1
