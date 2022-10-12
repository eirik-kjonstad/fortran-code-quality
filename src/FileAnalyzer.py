# -*- coding: UTF-8 -*-
import re
from Routine import Routine
from IndentationChecker import IndentationChecker
import ntpath


class FileAnalyzer:
    def __init__(self, filepath):

        self.name = ntpath.basename(filepath)
        self.file = open(filepath)
        self.lines = self.file.readlines()
        self.indenter = IndentationChecker()

    def analyze(self):

        lineNumber = 0
        print(f"File: {self.name}\n")

        for line in self.lines:

            self.indenter.check(line)

            routineDeclaration = re.match(
                r".*\s*(subroutine|function)\s+(\w+)\s*\(", line
            )

            if routineDeclaration:
                self.analyzeRoutine(routineDeclaration, lineNumber)

            lineNumber = lineNumber + 1

        print("")

    def analyzeRoutine(self, routineDeclaration, lineNumber):

        kind = routineDeclaration.group(1)
        name = routineDeclaration.group(2)
        routine = Routine(self.lines[lineNumber:], name, kind)
        routine.runQualityChecks()
