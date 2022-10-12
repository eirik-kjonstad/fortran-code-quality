# -*- coding: UTF-8 -*-
import re
from Routine import Routine
from IndentationChecker import IndentationChecker


class FileAnalyzer:
    def __init__(self, filepath):

        self.name = filepath.name
        with open(filepath) as file:
            self.lines = file.readlines()
        self.indenter = IndentationChecker()

    def analyze(self):

        print(f"File: {self.name}\n")

        for lineNumber, line in enumerate(self.lines):

            self.indenter.check(line)

            routineDeclaration = re.match(
                r".*\s*(subroutine|function)\s+(\w+)\s*\(", line
            )

            if routineDeclaration:
                self.analyzeRoutine(routineDeclaration, lineNumber)

        print("")

    def analyzeRoutine(self, routineDeclaration, lineNumber):

        kind = routineDeclaration.group(1)
        name = routineDeclaration.group(2)
        routine = Routine(self.lines[lineNumber:], name, kind)
        routine.runQualityChecks()
