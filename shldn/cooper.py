"""Sheldon helps you find the divisions in your Python code.

"""
import sys
import ast

try:
    from visitors.divisitor import DivVisitor
except:
    from .visitors.divisitor import DivVisitor

# based on div tuple in divisitor module
LINENO = 0
NUMERATOR = 1
DENOMINATOR = 2

# Constant for readable output
TABSIZE = 4

class Sheldon:
    """Main code analyzer."""

    def __init__(self, source, sourcepath):
        """Initialize the main code analyzer.

        :param source: Source code.
        :type source: str
        """
        self._source = source
        self._sourcepath = sourcepath
        self._analyzed = False
        self._divisions = None

    def analyze(self):
        """Run source analysis."""
        if not self._analyzed:
            visitor = DivVisitor()
            try:
                visitor.visit(ast.parse(self._source))
                self._divisions = visitor.divisions
            except SyntaxError:
                _, _, exc_tb = sys.exc_info()
                self._divisions = [(exc_tb.tb_lineno, "SyntaxError")]
            self._analyzed = True

    @property
    def divisions(self):
        """return divisions found in the source code"""
        self.analyze()
        return self._divisions

    def printdivs(self, readable):
        """print the divisions found in the source code"""
        divisions = self.divisions
        if divisions:

            if readable:
                print(f"{self._sourcepath}")

            for d in divisions:
                if not readable:
                    print(f"{self._sourcepath}", end="")
                else:
                    print(" " * TABSIZE, end="")

                if(d[NUMERATOR] != "SyntaxError"):
                    print(f" {d[LINENO]} {d[NUMERATOR]:5} / {d[DENOMINATOR]}")
                else:
                    print(f" {d[LINENO]} {d[NUMERATOR]:5}")
                    
if __name__ == "__main__":
    print("Leonard always drives Sheldon around")
    print("execute the leonard driver instead")
