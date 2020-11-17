"""MDxFind algorithm converter

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
  Author of the program:
  - 0x69BE027C97
"""
from docopt import docopt
import os

def load_algorithms():
    algorithms = []
    with open('./algorithms.txt', 'r') as input_file:
        for i, line in enumerate(input_file):
            if not i:
                continue
            mdxfind, hashesorg = line.rstrip().split('\t')
            algorithms.append({
                    'mdxfind': mdxfind,
                    'hashesorg': hashesorg
                })
        return algorithms

if __name__ == '__main__':
    # 
    algorithms = load_algorithms()
    arguments = docopt(__doc__, version='1.0')
    file_1 = "./mixed_founds.cracked"
    file_2 = "./mixed_salted_founds.cracked"
    file_3 = "./left_founds.cracked"
    output_file_handle_1 = open(file_1, 'a+')
    output_file_handle_2 = open(file_2, 'a+')
    output_file_handle_3 = open(file_3, 'a+')

    with open('./' + arguments['--input-file'], 'r') as input_file:
        for i, line in enumerate(input_file):
            hash_algorithm, hash_ = line.rstrip().split(' ', 1)
            # find a match in algorithms
            matched = False
            for algorithm in algorithms:
                if hash_algorithm == algorithm['mdxfind']:
                    # split by salt or not
                    if "SALT" in algorithm['mdxfind'] or "SALT" in algorithm['hashesorg']:
                        output_file_handle_2.write(algorithm['hashesorg'] + " " + hash_ + "\n")
                    else:
                        output_file_handle_1.write(algorithm['hashesorg'] + " " + hash_ + "\n")
                    matched = True
                    break
            if not matched:
                output_file_handle_3.write(hash_algorithm + " " + hash_ + "\n")
    print("Done, making files sorted & unique")
    os.system("sort -u " + file_1 + "> tmp")
    os.system("mv tmp " + file_1)
    os.system("sort -u " + file_2 + "> tmp")
    os.system("mv tmp " + file_2)
    os.system("sort -u " + file_3 + "> tmp")
    os.system("mv tmp " + file_3)
    print("Done! Now upload " + file_1 + " to hashes.org with algorithm \"mm\" and no salt")
    print("upload " + file_2 + " to hashes.org with algorithm \"mm\" and \":\" as salt, with checkbox")
    print(file_3 + " Contains hashes that did not match any in the algorithm list.")