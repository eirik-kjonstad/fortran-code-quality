from CodeLine import CodeLine
from ErrorHandling import ErrorMessage


class IndentationChecker:
    def __init__(self, indent):

        self.indentLength = indent
        self.indentation = -1
        self.continuedLine = False

    def check(self, line, lineNumber, ErrorTracker):

        codeline = CodeLine(line)

        if codeline.isComment() or len(line.lstrip()) == 0:
            return

        if self.continuedLine:
            if not codeline.hasContinuation():
                self.continuedLine = False
            return

        if codeline.hasContinuation():
            self.continuedLine = True

        if self.indentation == -1:
            self.indentation = codeline.indentation
        else:
            if codeline.indentation == self.indentation:
                self.indentation = codeline.indentation
            elif codeline.indentation == self.indentation + self.indentLength:
                self.indentation = self.indentation + self.indentLength
            elif codeline.indentation == self.indentation - self.indentLength:
                self.indentation = self.indentation - self.indentLength
            elif codeline.indentation == self.indentation + 2 * self.indentLength:
                self.indentation = self.indentation + self.indentLength
            elif codeline.indentation == self.indentation - 2 * self.indentLength:
                self.indentation = self.indentation - self.indentLength
            else:
                expectation = [
                    self.indentation + i * self.indentLength
                    for i in range(-2, 2)
                    if self.indentation + i * self.indentLength >= 0
                ]
                error = ErrorMessage(
                    lineNumber,
                    f"'{codeline.lineString}' has unexpected indentation!",
                    f"Indentation: {codeline.indentation}   Expected: {expectation}",
                )
                ErrorTracker.addError(error)
