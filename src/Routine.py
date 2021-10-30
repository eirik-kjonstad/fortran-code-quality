# -*- coding: UTF-8 -*-
import re, sys
from CodeLine import CodeLine


class Routine:
    def __init__(self, lines, name, kind):

        self.maxLength = 30
        self.maxParameters = 5

        self.name = name
        self.kind = kind

        self.setUpLines(lines)
        self.calculateLength()
        self.calculateParameters()

    def setUpLines(self, lines):

        # Sets up self.lines, which is an array of all the code
        # lines from "subroutine sub(...)" to "end subroutine sub"

        endLine = 0
        regex = r"^\s*end\s+" + self.kind

        for line in lines:
            if not re.match(regex, line):
                endLine = endLine + 1
            else:
                self.lines = lines[0:endLine]
                break

    def runQualityChecks(self):

        self.testLength()
        self.testImplicitNone()
        self.testNumParameters()
        self.testParameterIntents()

    def calculateLength(self):

        self.length = 0

        for line in self.lines:

            codeLine = CodeLine(line)

            if (
                not codeLine.isComment()
                and not codeLine.isImport()
                and not codeLine.isDeclaration()
            ):

                self.length = self.length + 1

        self.length = self.length - 2  # do not count "subroutine"
        # and "end subroutine"

    def testLength(self):

        if self.length > self.maxLength:
            print(
                "      {} {} {}{}{}{}{}".format(
                    self.kind.capitalize(),
                    self.name,
                    "is too long (",
                    self.length,
                    "/",
                    self.maxLength,
                    ")",
                )
            )

    def testImplicitNone(self):

        if not self.hasImplicitNone():
            print(
                "      Error: {} {} {}".format(
                    self.kind.capitalize(),
                    self.name,
                    "does not have an 'implicit none' statement!",
                )
            )
            sys.exit(1)

    def hasImplicitNone(self):

        for line in self.lines:

            codeLine = CodeLine(line)
            if codeLine.isImplicitNone():
                return True

        return False

    def calculateParameters(self):

        self.parameters = []

        for line in self.lines:

            codeLine = CodeLine(line)
            if codeLine.isComment():
                break

            parameters = re.findall(r"\w+(?=\s*\,|\))", line)

            for parameter in parameters:

                self.parameters.append(parameter)

            if re.search(r"\)\s*", line):
                break

    def testNumParameters(self):

        numParameters = len(self.parameters)

        if numParameters > self.maxParameters:
            print(
                "      {} {} {}{}{}{}{} {}".format(
                    self.kind.capitalize(),
                    self.name,
                    "has too many arguments (",
                    numParameters,
                    "/",
                    self.maxParameters,
                    ")",
                    self.parameters,
                )
            )

    def testParameterIntents(self):

        parametersMissingIntent = []

        for line in self.lines:
            for parameter in self.parameters:

                regex = r"::\s*(" + parameter + ")"
                parameterMatch = re.search(regex, line)

                if parameterMatch and not line.startswith("import"):

                    intentMatch = re.search(r"intent\s*(\s*in|out|inout\s*)", line)

                    if not intentMatch:

                        parametersMissingIntent.append(parameter)

        if parametersMissingIntent:
            print(
                "      {} {} has parameters with no intent: {}".format(
                    self.kind.capitalize(), self.name, parametersMissingIntent
                )
            )
