from errno import EEXIST, ENOENT
from fnmatch import fnmatch
from os import chmod, makedirs, walk
from os.path import join, isdir, dirname, sep

from stl import read_binary_file, binary

def safe_makedirs(path, mode = 0700):
    try:
        makedirs(path)
    except OSError as e:
        if e.errno == EEXIST and isdir(path): pass
        else: raise RuntimeError( '{0} exists and is not a directory'.format(path))

def process(input_dir, output_dir, callback, fnpattern = '*', **kwargs):
    base_dir = dirname(input_dir + sep)
    prefix_len = len(base_dir) + 1
    for dirpath, dirnames, filenames in walk(base_dir, topdown = False):
        for path in filenames:
            fq_in_path = join(dirpath, path)
            if fnmatch(fq_in_path, fnpattern):
                dest_dir = join(output_dir, dirpath[prefix_len:])
                safe_makedirs(dest_dir)
                fq_out_path = join(dest_dir, path)
                callback(fq_in_path, fq_out_path, **kwargs)
