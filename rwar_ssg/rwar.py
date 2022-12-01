#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rwar_ssg.Parser import get_parser_args
from rwar_ssg.File import SSG
from rwar_ssg.Utils import greeting

# options = parser.parse_args()

if __name__ == "__main__":
    greeting()

    parser_args = get_parser_args()
    # take the only argument as input
    rwar = SSG(
        parser_args.output[0],
        parser_args.stylesheet[0] if parser_args.stylesheet is not None else None,
        parser_args.lang[0],
    )

    # start the static site generator
    rwar.start(parser_args.input[0])
