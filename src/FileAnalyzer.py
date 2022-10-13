# -*- coding: UTF-8 -*-
import re
from ErrorHandling import ErrorMessage
from Routine import Routine
from IndentationChecker import IndentationChecker


class FileAnalyzer:
    def __init__(self, filepath):

        self.name = filepath.name
        with open(filepath) as file:
            self.lines = file.readlines()
        self.indenter = IndentationChecker()

    def analyze(self, ErrorTracker):

        print(f"File: {self.name}")

        for lineNumber, line in enumerate(self.lines):

            self.indenter.check(line, lineNumber + 1, ErrorTracker)

            routineDeclaration = re.match(
                r".*\s*(subroutine|function)\s+(\w+)\s*\(", line
            )

            if routineDeclaration:
                self.analyzeRoutine(routineDeclaration, lineNumber, ErrorTracker)

        print("")

    def analyzeRoutine(self, routineDeclaration, lineNumber, ErrorTracker):

        kind = routineDeclaration.group(1)
        name = routineDeclaration.group(2)

        if self.lines[lineNumber].strip().startswith("!"):
            error = ErrorMessage(
                lineNumber,
                f"{kind.capitalize()} '{name}' appears to be commented out.",
            )
            ErrorTracker.addError(error)
            return

        routine = Routine(self.lines[lineNumber:], name, kind, lineNumber)
        routine.runQualityChecks(ErrorTracker)
