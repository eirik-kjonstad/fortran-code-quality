# -*- coding: UTF-8 -*-

from FileAnalyzer import FileAnalyzer
from pathlib import Path


class FortranQuality:
    def __init__(self, path: Path):

        self.name = "FortranQuality: a code-health tester for Fortran"
        self.author = "Eirik F. Kjønstad"
        self.year = 2021

        self.path = path

        self.printHeader()
        self.printPath()

    def run(self):

        self.analyzeFiles()

    def analyzeFiles(self):
        # TODO python>=3.10; glob supports a root_dir argument
        lowercase_suffixes = ["f90", "f95", "f03", "f08", "f18"]
        suffixes = [suffix.upper() for suffix in lowercase_suffixes]
        suffixes.extend(lowercase_suffixes)

        for suffix in suffixes:
            for filepath in self.path.glob(f"**/*.{suffix}"):
                fileAnalyzer = FileAnalyzer(filepath)
                fileAnalyzer.analyze()

    def printHeader(self):

        print(f"\n{self.name}\n(C) {self.author}, {self.year}")

    def printPath(self):

        print(f"\nWill analyze Fortran files in directory {self.path}\n")
