from argparse import ArgumentParser
from errno import EEXIST, ENOENT
from fnmatch import fnmatch
from os import chmod, makedirs, walk
from os.path import join, expandvars, expanduser, isdir, abspath, dirname, sep
from StringIO import StringIO

from stl import read_binary_file, binary

def safe_makedirs(path, mode = 0700):
    try:
        makedirs(path)
    except OSError as e:
        if e.errno == EEXIST and isdir(path): pass
        else: raise RuntimeError( '{0} exists and is not a directory'.format(path))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input-dir', '-i', help = 'The directory containing the source binary stl files.', default = '.')
    parser.add_argument('--output-dir', '-o', help = 'The directory that will contain the ascii stl files.', default = 'ascii')
    args = parser.parse_args()

    base_dir = dirname(args.input_dir + sep)
    prefix_len = len(base_dir) + 1
    for dirpath, dirnames, filenames in walk(base_dir, topdown = False):
        for path in filenames:
            fq_in_path = join(dirpath, path)
            if fnmatch(fq_in_path,'*.stl'):
                dest_dir = join(args.output_dir, dirpath[prefix_len:])
                safe_makedirs(dest_dir)
                fq_out_path = join(dest_dir, path)
                print 'reading: {}...'.format(fq_in_path),
                with open(fq_in_path) as f: data = f.read()
                if data.startswith('solid'):
                    with open(fq_out_path, 'w') as f: f.write(data)
                    print ' copied in: {}'.format(fq_out_path)
                else:
                    try:
                        solid = read_binary_file(StringIO(data))
                    except binary.FormatError:
                        print ' FAILED to convert!'
                    else:
                        with open(fq_out_path, 'w') as f: solid.write_ascii(f)
                        print ' converted in: {}'.format(fq_out_path)
