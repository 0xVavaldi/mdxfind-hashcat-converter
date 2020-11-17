"""MDxFind algorithm converter

Usage:
  convert.py --input-file=<file>
  convert.py (-h | --help)
  convert.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --input-file  Input file from mdxfind.

"""
import docopt 

def load_algorithms():
    algorithms = []
    with open('algorithms.txt', 'r') as input_file:
        for i, line in enumerate(input_file):
            print(i)
            exit()
            line.split('\t')
            for salt in salts:
                output.write(line.strip('\n').strip('\r') + ":" + salt + "\n")


if __name__ == '__main__':
    # 0x69BE027C97
    arguments = docopt(__doc__, version='0.1')
    print(arguments)