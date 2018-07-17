"""
Sheldon
"""
import ast
import argparse

from visitors.divisitor import DivVisitor

# based on div tuple in divisitor module
LINENO = 0
NUMERATOR = 1
DENOMINATOR = 2

class Sheldon:
    """This master class uses the DivVisitor class
    to analyses the source code.

    :param source: source code
    :type source: str

    """
    def __init__(self, source):
        self._source = source
        self._divs = DivVisitor()
        self._analyzed = False
        self._ast = None

    def analyze(self):
        """analyze the python source code"""
        # analyze once
        if not self._analyzed:
            self._ast = ast.parse(self._source)
            # visit AST
            self._divs.visit(self._ast)
            self._analyzed = True

    @property
    def line_count(self):
        """Returns the number of newlines in the code"""
        return self._source.count("\n")

    @property
    def divisions(self):
        """Returns the divisions"""
        self.analyze()
        return self._divs.divs

def printdivs(sourcefile, arr, readable):
    """print the divisions found in the source code"""
    if arr:
        if readable:
            print(f"{sourcefile}")
        for div in arr:
            if not readable:
                print(f"{sourcefile}", end="")
            else: print("\t", end="")
            print(f"{div[LINENO]:4d} {div[NUMERATOR]:5} / {div[DENOMINATOR]}")


def parseargs():
    """parse the command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-hr", "--human_readable", help="set for friendlier output",
                        action="store_true")
    parser.add_argument("-r", "--recursive", help="recursively check python files in path",
                        action="store_true")
    parser.add_argument("dirpath", type=str, help="path to dir containing python source file(s)")
    return parser.parse_args()

if __name__ == "__main__":
    ARGS = parseargs()

    import os
    files_checked = 0
    divs_found = 0

    if os.path.isdir(ARGS.dirpath):
        for dirpath, dirs, files in os.walk(ARGS.dirpath):
            files = [f for f in os.listdir(dirpath) if f.endswith('.py')]
            files_checked += len(files)
            for filename in files:
                fname = os.path.join(dirpath, filename)
                with open(fname) as f:
                    pysource = f.read()
                    sheldon = Sheldon(pysource)
                    try:
                        sheldon.analyze()
                    except SyntaxError as e_e:
                        print(f"Syntax Error in {filename}: {e_e}")
                        continue
                    divs_found += len(sheldon.divisions)
                    printdivs(fname, sheldon.divisions, ARGS.human_readable)
            if not ARGS.recursive:
                exit(0)
        if ARGS.human_readable:
            print(f"{files_checked} files checked")
            print(f"{divs_found} divisions found")
    else:
        import sys
        sys.exit(f"{ARGS.dirpath} doesn't exist!")
