#! /bin/python3

import argparse


parser = argparse.ArgumentParser(
    prog='rwar', description="A simple static site generator")
parser.add_argument('--input', '-i', nargs=1, required=True,
                    help="Input file/directory")
parser.add_argument('--output', '-o', nargs=1, required=False,
                    help="Output directory (dist by default)", default=['./dist'])
parser.add_argument('--stylesheet', '-s', nargs=1, required=False,
                    help='Stylesheet for generated HTML', default=None)
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s v0.1')


if __name__ == '__main__':
    args = parser.parse_args()
