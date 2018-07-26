import unittest
import os

from shldn.cooper import Sheldon
from shldn.leonard import get_files

TEST_FILES_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "test-data/")

FIRST_LINE_NESTED_DIVISION = [(1, "Num", "BinOp"), (1, "Num", "Num")]
FIRST_LINE_DIVISION = [(1, "Num", "Num")]
SYNTAX_ERROR = [(1, "SyntaxError")]
EMPTY_DIVISION = []
EXT_FILES = ["div.py", "monte.mpy"]

TEST_FILES = ["more-test-data/nested_div.py",
              "div.py",
              "empty.py",
              "monte.mpy",
              "printdiv.py",
              "py2print.py"]

NESTED_DIV_FILE = 0
DIV_FILE = 1
EMPTY_FILE = 2
MPY_FILE = 3
PRINT_DIV_FILE = 4
PY2_PRINT_FILE = 5


class TestSheldon(unittest.TestCase):
    def _check(self, testdatapath, expected):
        with open(testdatapath) as f:
            obj = Sheldon(f.read(), testdatapath)
            obj.analyze()
            self.assertEqual(len(expected), len(obj.divisions))
            for x, y in zip(expected, obj.divisions):
                self.assertEqual(x, y)

    def test_division(self):
        my_data_path = os.path.join(TEST_FILES_DIR, TEST_FILES[DIV_FILE])
        self._check(my_data_path, FIRST_LINE_DIVISION)

    def test_nested_division(self):
        my_data_path = os.path.join(TEST_FILES_DIR,
                                    TEST_FILES[NESTED_DIV_FILE])
        self._check(my_data_path, FIRST_LINE_NESTED_DIVISION)

    def test_empty(self):
        my_data_path = os.path.join(TEST_FILES_DIR, TEST_FILES[EMPTY_FILE])
        self._check(my_data_path, EMPTY_DIVISION)

    def test_SyntaxError(self):
        my_data_path = os.path.join(TEST_FILES_DIR, TEST_FILES[PY2_PRINT_FILE])
        self._check(my_data_path, SYNTAX_ERROR)

    def test_division_in_print(self):
        my_data_path = os.path.join(TEST_FILES_DIR, TEST_FILES[PRINT_DIV_FILE])
        self._check(my_data_path, FIRST_LINE_DIVISION)

    def test_file_extension(self):

        self.assertEqual(len(EXT_FILES), len(Sheldon.DEFAULT_EXTENSIONS))

        for f in EXT_FILES:
            self._check(os.path.join(TEST_FILES_DIR, f), FIRST_LINE_DIVISION)


class TestLeonard(unittest.TestCase):
    def test_recursion(self):
        leonard_files = get_files(
            TEST_FILES_DIR, True, Sheldon.DEFAULT_EXTENSIONS)
        expected = []
        for f in TEST_FILES:
            expected.append(os.path.join(TEST_FILES_DIR, f))
        self.assertEqual(sorted(leonard_files), sorted(expected))


if __name__ == "__main__":
    unittest.main()
