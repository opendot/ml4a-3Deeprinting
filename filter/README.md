# 3deeprinting - Filter

To convert between formats, first install `python-stl` as

    pip install -r requirements.txt

that must be done in a virtualenv, or in the system libs, just once.

Then to convert a dir `from` containing a bunch of `.stl` files from STL binary
or ASCII format to STL ASCII format saving the results in a dir `to` just run

    python -m stlfilter.bin2ascii -i from -o to

similarly, to convert a dir `from` containing a bunch of `.stl` files from STL
binary or ASCII format to RAW format saving the results in a dir `to` just run

    python -m stlfilter.stl2raw -i from -o to

Observe that since parsing of STL ASCII format is *very* slow, you can skip
such files adding `-s` to the conversion options, as in

    python -m stlfilter.stl2raw -si from -o to
