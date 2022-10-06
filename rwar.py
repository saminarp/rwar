#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
import json
from clint.arguments import Args
from src.File import SSG
from src.Utils import greeting
from os.path import isfile

args = Args()
parser = argparse.ArgumentParser(prog='rwar',
                                 description="Static site generator to create a website from text files")
parser.add_argument('--input', '-i',
                    nargs=1, required=(not ('--config' in sys.argv or '-c' in sys.argv)),
                    help="Input file/directory")
parser.add_argument('--output', '-o',
                    nargs=1, required=False, help="Output directory (dist by default)",
                    default=['./dist'])
parser.add_argument('--stylesheet', '-s',
                    nargs=1, required=False, default=['https://cdn.jsdelivr.net/npm/water.css@2/out/water.css'],
                    help='Stylesheet for generated HTML (by default:%(default)s)')
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s v0.1')
parser.add_argument('--lang', '-l', nargs=1, required=False, default=['en-CA'],
                    help='Language of the generated HTML (by default:%(default)s)')
parser.add_argument('--config', '-c',
                    nargs=1, required=False, help="Configuration JSON file", default=None)

options = parser.parse_args()

if __name__ == '__main__':
    greeting()
    args = parser.parse_args()
    # take the only argument as input
    rwar = SSG(args.output[0], args.stylesheet[0]
               if args.stylesheet is not None else None, args.lang[0])

    # start the static site generator
    rwar.start(args.input[0])
