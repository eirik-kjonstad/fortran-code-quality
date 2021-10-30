# -*- coding: UTF-8 -*-

import sys

sys.path.insert(0, "./src")  # to import FortranQuality

from FortranQualityClass import FortranQuality

def main():

    program = FortranQuality()
    program.run()

if __name__ == "__main__":

    main()
