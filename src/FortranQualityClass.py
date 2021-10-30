# -*- coding: UTF-8 -*-

from argparse import ArgumentParser, HelpFormatter
from FileAnalyzer import FileAnalyzer

import os
import re
import pathlib


class FortranQuality:
    def __init__(self):

        self.name = "FortranQuality: a code-health tester for Fortran"
        self.author = "Eirik F. Kjønstad"
        self.year = 2021

        self.setUpInputParser()
        self.setUpPath()

        self.printHeader()
        self.printPath()

    def run(self):

        self.analyzeFiles()

    def analyzeFiles(self):

        for root, directories, files in os.walk(self.path):

            for file in files:

                filepath = root + "/" + file

                if re.search(r".F90$", filepath):

                    fileAnalyzer = FileAnalyzer(filepath)
                    fileAnalyzer.analyze()

    def setUpInputParser(self):

        inputParser = ArgumentParser()

        inputParser.add_argument(
            "--path",
            help=(
                "Path to source directory containing Fortran files. Default is current directory."
            ),
        )

        self.args = inputParser.parse_args()

    def printHeader(self):

        print("\n{}\n(C) {}, {}".format(self.name, self.author, self.year))

    def setUpPath(self):

        if self.args.path:

            self.path = self.args.path

        else:

            self.path = pathlib.Path().absolute()

    def printPath(self):

        print("\n{} {}\n".format("Will analyze Fortran files in directory", self.path))
