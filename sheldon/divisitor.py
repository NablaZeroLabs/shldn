import ast

class DivVisitor(ast.NodeVisitor):
    """
    Class that traverses the AST tree and collects all divisions (numerator, 
    denominator), the line in which they are and if the numerator and 
    denominator are the same type in the accumulator.
    """
    def __init__(self):
        super().__init__()
        self._acc = []

    @property
    def divs(self):
        return self._acc

    class _Decorators(ast.NodeVisitor):
        @classmethod
        def recursive(self, func):
            """ Decorator to make visitor work recursively """
            def wrapper(self, node):
                func(self, node)
                for child in ast.iter_child_nodes(node):
                    self.visit(child)
            return wrapper

    @_Decorators.recursive
    def visit_BinOp(self, node):
        if (type(node.op).__name__ == "Div"):
            # (line number, numerator, denominator)
            self._acc.append((node.lineno, type(node.left).__name__, type(node.right).__name__))
