# 3Deeprinting - Generate

First thing pick, according to the hardware and libs you have on your system,
one of the Docker [Torch RNN images](https://github.com/crisbal/docker-torch-rnn)
by writing one of the corresponding stirngs `crisbal/torch-rnn:base`,
`crisbal/torch-rnn:cuda6.5`, or `crisbal/torch-rnn:cuda7.5` in the file named
`image.conf` in this directory.

Then, put an ASCII STL model in the `data` directory; assume it is named
`pot.stl` first run the *preprocessing* as

    ./preprocessing.sh data/pot.stl

at the end, you should find a `pot.h5` and `pot.json` in the `data` dir; now run
the *training* as

    ./train data/pot.stl 1000

where `1000` is the number of iterations among checkpoints; while the
computation runs, you should see some file named `pot-checkpoint_NNNN.t7` in the
`data` dir. As soon as you have one of such chekpoint you and *sample* the
genrator as


    ./sample.sh data/pot.stl 3000 20000

where `3000` is the checkpoint that you want to use (meaning that
`pot-checkpoint_3000.t7` must be present in `data` dir) and `20000` is the
length of the file you want to generate.

If you have a RAW model, instead, just replace `pot.raw` in place of `pot.stl`
in all the above commands.
