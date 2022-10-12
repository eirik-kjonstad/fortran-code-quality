# -*- coding: UTF-8 -*-

import sys
from argparse import ArgumentParser

sys.path.insert(0, "./src")  # to import FortranQuality

from FortranQualityClass import FortranQuality
from pathlib import Path


def parse_input():

    inputParser = ArgumentParser()

    inputParser.add_argument(
        "--path",
        help=(
            "Path to source directory containing Fortran files. Default is current directory."
        ),
    )

    return inputParser.parse_args()


def setUpPath(args):

    if args.path:

        path = Path(args.path).resolve()

    else:

        path = Path().resolve()

    if not path.is_dir():
        raise NotADirectoryError(str(path))

    return path


def main():

    args = parse_input()
    path = setUpPath(args)
    program = FortranQuality(path)
    program.run()


if __name__ == "__main__":

    main()
