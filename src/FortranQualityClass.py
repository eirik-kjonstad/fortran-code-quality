# -*- coding: UTF-8 -*-

from argparse import ArgumentParser, HelpFormatter
from FileAnalyzer import FileAnalyzer

import pathlib
import glob

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
        # TODO python>=3.10; glob supports a root_dir argument
        for filepath in glob.iglob(str(self.path)+"/**/*.F90", recursive=True):
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

        print(f"\n{self.name}\n(C) {self.author}, {self.year}")

    def setUpPath(self):

        if self.args.path:

            self.path = self.args.path

        else:

            self.path = pathlib.Path().absolute()

    def printPath(self):

        print(f"\nWill analyze Fortran files in directory {self.path}\n"
