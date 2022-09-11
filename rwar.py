#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from src import File
from clint.arguments import Args
from clint.textui import puts, colored, indent
from pyfiglet import Figlet

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
    f = Figlet(font='slant')
    print(f.renderText('rwar'))

    args = parser.parse_args()

    # take the only argument as input
    myssg = File.SSG(args.output[0], args.stylesheet[0]
                     if args.stylesheet is not None else None)

    # start the static site generator
    myssg.start(args.input[0])
