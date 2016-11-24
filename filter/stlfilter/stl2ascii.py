from argparse import ArgumentParser
from StringIO import StringIO

from stl import read_binary_file, binary

from stlfilter import process

def convert(fq_in_path, fq_out_path):
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

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input-dir', '-i', help = 'The directory containing the source stl files.', default = '.')
    parser.add_argument('--output-dir', '-o', help = 'The directory that will contain the ascii stl files.', default = 'ascii')
    args = parser.parse_args()

    process(args.input_dir, args.output_dir, convert, '*.stl')
