class ErrorMessage:
    def __init__(self, lineNumber, messageCore, *additionalLines):
        self.indent = 2
        self.lineNumber = lineNumber
        self.message = messageCore
        for i in additionalLines:
            self.message += f"\n{(self.indent+2)*' '}{i}"

    def __str__(self):
        return f"{(self.indent)*' '}- Error in {self.lineNumber}: {self.message}"


class ErrorTracker:
    def __init__(self):
        self.currentFile = ""
        self.errorsInFile = dict()

    def addFile(self, filename):
        if self.currentFile and not self.errorsInFile[self.currentFile]:
            self.errorsInFile.pop(self.currentFile)
        self.errorsInFile[filename] = []
        self.currentFile = filename

    def addError(self, error):
        self.errorsInFile[self.currentFile].append(error)

    def printSummary(self):
        print(f"Summary of errors:\n{18*'-'}")

        counter = 0
        for filename in self.errorsInFile:

            if not self.errorsInFile[filename]:
                continue

            print(f"File: {filename}")
            counter += 1

            for error in self.errorsInFile[filename]:

                print(error)

        if counter == 0:
            print("No errors found!")
