"""Sheldon helps you find the divisions in your Python code.

"""
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

    def __init__(self, source):
        """Initialize the main code analyzer.

        :param source: Source code.
        :type source: str
        """
        self._source = source
        self._analyzed = False

    def analyze(self):
        """Run source analysis."""
        if not self._analyzed:
            visitor = DivVisitor()
            visitor.visit(ast.parse(self._source))
            self._divs = visitor.divs
            self._analyzed = True

    @property
    def divisions(self):
        """Returns the divisions"""
        self.analyze()
        return self._divs

    def printdivs(self, filename, divs, readable):
        """print the divisions found in the source code"""
        if divs:
            if readable:
                print(f"{filename}")
            for div in divs:
                if not readable:
                    print(f"{filename}", end="")
                else: print(" " * TABSIZE, end="")
                print(f" {div[LINENO]} {div[NUMERATOR]:5} / {div[DENOMINATOR]}")

if __name__ == "__main__":
    print("Leonard always drives Sheldon around")
    print("execute the leonard driver instead")
