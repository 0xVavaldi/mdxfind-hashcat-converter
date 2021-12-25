"""MDxFind algorithm converter -Hashcat

Usage:
  convert.py --input-file=<file>
  convert.py (-h | --help)
  convert.py --version

Options:
  -h --help            Show this screen.
  --version            Show version.
  --input-file=<file>  Input file from mdxfind.

Credits:
  For the cracking suite algorithm spreadsheet:
  - Tycho
  - S3in!c
  - penguinkeeper
"""
from docopt import docopt
import os

def load_algorithms():
    algorithms = []
    with open('./algorithms-2.0.txt', 'r') as input_file:
        for i, line in enumerate(input_file):
            if not i:
                continue
            mdxfind, hashcat = line.rstrip().split('\t')
            algorithms.append({
                    'mdxfind': mdxfind,
                    'hashcat': hashcat
                })
        return algorithms

if __name__ == '__main__':
    algorithms = load_algorithms()
    arguments = docopt(__doc__, version='1.0')
    file_1 = "./others.cracked"
    output_file_handle_1 = open(file_1, 'a+', encoding="utf-8")

    with open('./' + arguments['--input-file'], 'r', encoding='utf-8') as input_file:
        for i, line in enumerate(input_file):
            if ' ' not in line:
                print(line.rstrip())
                continue
            hash_algorithm, hash_ = line.rstrip().split(' ', 1)
            # find a match in algorithms
            matched = False
            for algorithm in algorithms:
                if hash_algorithm == algorithm['mdxfind']:
                    # split by salt or not
                    output_file_handle_2 = open(algorithm['hashcat'] + ".cracked", 'a+', encoding="utf-8")
                    output_file_handle_2.write(hash_ + "\n")
                    matched = True
                    # do not break, this will give duplicate output in some cases but is a dirty solution to algorithms not quite matching.
            if not matched:
                output_file_handle_1.write(hash_algorithm + " " + hash_ + "\n")
    print("Done, making files sorted & unique")
    os.system("sort -u " + file_1 + "> tmp")
    os.replace("tmp", file_1)
