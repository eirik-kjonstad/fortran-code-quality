from CodeLine import CodeLine
from ErrorHandling import ErrorMessage


class IndentationChecker:
    def __init__(self):

        self.indentLength = -1
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

        if self.indentation == -1:
            self.indentation = codeline.indentation
        elif self.indentLength == -1:
            self.indentLength = codeline.indentation - self.indentation
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
                error = ErrorMessage(
                    lineNumber,
                    f"'{codeline.lineString}' has unexpected indentation!",
                    f"Indentation: {codeline.indentation}   Expected: {self.indentation}",
                )
                ErrorTracker.addError(error)
