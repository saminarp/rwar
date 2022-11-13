import argparse
import sys
import json
from os.path import isfile
from clint.arguments import Args


def get_parser_args(args=Args().all):
    parser = argparse.ArgumentParser(
        prog="rwar", description="Static site generator to create a website from text files"
    )
    parser.add_argument(
        "--input",
        "-i",
        nargs=1,
        required=(not ("--config" in args or "-c" in args)),
        help="Input file/directory",
    )
    parser.add_argument(
        "--output",
        "-o",
        nargs=1,
        required=False,
        help="Output directory (dist by default)",
        default=["./dist"],
    )
    parser.add_argument(
        "--stylesheet",
        "-s",
        nargs=1,
        required=False,
        default=["https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"],
        help="Stylesheet for generated HTML (by default:%(default)s)",
    )
    parser.add_argument("--version", "-v", action="version", version="%(prog)s v0.1")
    parser.add_argument(
        "--lang",
        "-l",
        nargs=1,
        required=False,
        default=["en-CA"],
        help="Language of the generated HTML (by default:%(default)s)",
    )

    parser.add_argument(
        "--config",
        "-c",
        nargs=1,
        required=False,
        help="Configuration JSON file",
        default=None,
    )

    parser_args = parser.parse_args(args=args)

    if parser_args.config is not None:
        if isfile(parser_args.config[0]):
            with open(parser_args.config[0], "r", encoding="utf-8") as f:
                options = json.load(f)
        else:
            print("Config file not found")
            sys.exit(3)

        setattr(parser_args, "input", ["./data"])  # default input directory
        possible_args = list(
            filter(lambda x: not x.startswith("_"), dir(parser_args))
        )
        for key in options:
            if key in possible_args:
                setattr(parser_args, key, [options[key]])

    return parser_args
