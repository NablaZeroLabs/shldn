import ast
import argparse

from divisitor import DivVisitor

LINENO = 0
NUMERATOR = 1
DENOMINATOR = 2

class Sheldon:
    def __init__(self, source):
        self._source = source
        self._divs = DivVisitor()
        self._analyzed = False

    def _analyze(self):
        # analyze once
        if (not self._analyzed):
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
        self._analyze()
        return self._divs.divs

def printdivs(filename, arr, readable):
    if (len(arr) > 0):
        if(readable): print(f"{filename}")
        for div in arr:
            if(not readable):
                print(f"{filename}", end="")
            else: print("\t", end="")
            print(f"{div[LINENO]:4d} {div[NUMERATOR]:5} / {div[DENOMINATOR]}")


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-hr", "--human_readable", help="set for friendlier output",
                        action="store_true")
    parser.add_argument("-r", "--recursive", help="recursively check python files in path",
                        action="store_true")
    parser.add_argument("path", type=str, help="path to python source file(s)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parseargs()
    import os
    files_checked = 0
    divs_found = 0
    for dirpath, dirs, files in os.walk(args.path):
        files = [f for f in os.listdir(dirpath) if f.endswith('.py')]
        files_checked+= len(files)
        for filename in files:
            fname = os.path.join(dirpath, filename)
            with open(fname) as f:
                pysource = f.read()
                sheldon = Sheldon(pysource)
                try:
                    sheldon._analyze()
                except SyntaxError as e:
                    print(f"Syntax Error in {filename}: {e}")
                    continue
                divs_found+= len(sheldon.divisions)
                printdivs(fname, sheldon.divisions, args.human_readable)

        if(not args.recursive):
            exit(0)
    if(args.human_readable):
        print(f"{files_checked} files checked")
        print(f"{divs_found} divisions found")
