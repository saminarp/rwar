#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from clint.arguments import Args
from clint.textui import puts, colored, indent
from pyfiglet import Figlet

from src import File

args = Args()
parser = argparse.ArgumentParser(
    prog='rwar', description="Static site generator to create a website from a directory of text files")
parser.add_argument('--input', '-i', nargs=1, required=True,
                    help="Input file/directory")
parser.add_argument('--output', '-o', nargs=1, required=False,
                    help="Output directory (dist by default)", default=['./dist'])
parser.add_argument('--stylesheet', '-s', nargs=1, required=False,
                    default=[
                        'https://cdn.jsdelivr.net/gh/kimeiga/bahunya/dist/bahunya.min.css'],
                    help='Stylesheet for generated HTML (by default:%(default)s)')
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s v0.1')

if __name__ == '__main__':
    puts(colored.magenta(Figlet(font='slant').renderText('rwar')))
    with indent(4, quote='>>>'):
        puts(colored.green('rwar v0.1'))
        puts(colored.green(
            'Static site generator'))

    args = parser.parse_args()
    # take the only argument as input
    rwar = File.SSG(args.output[0], args.stylesheet[0]
                    if args.stylesheet is not None else None)

    # start the static site generator
    rwar.start(args.input[0])
