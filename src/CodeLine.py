import re


class CodeLine:
    def __init__(self, lineString):

        self.indentation = len(lineString) - len(lineString.lstrip(' '))

        self.lineString = lineString.strip()

    def isComment(self):

        if re.match(r"^!", self.lineString):

            return True

        else:

            return False

    def isImport(self):

        # True if use and import keywords

        if re.match(r"^use", self.lineString) or re.match(r"^import", self.lineString):

            return True

        else:

            return False

    def isDeclaration(self):

        regexString = r"^class|type|real|integer|complex|logical"

        if re.match(regexString, self.lineString):

            return True

        else:

            return False

    def isImplicitNone(self):

        if re.match(r"^implicit\s+none", self.lineString):

            return True

        else:

            return False

    def hasContinuation(self):

        rstrippedLine = self.lineString.rstrip()

        if self.isComment() or self.isEmpty():
            return False 
        elif re.search('&', self.lineString): 
            return True
        else:
            return False   

    def isEmpty(self):
        if len(self.lineString.strip()) == 0:
            return True 
        else: 
            return False 

