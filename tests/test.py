import unittest
import os

from shldn.cooper import Sheldon
from shldn.leonard import EXTENSIONS

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
EXT_FILES = ["div.py", "monte.mpy"]  # add manually


class TestSheldon(unittest.TestCase):
    def _check(self, testdatapath, expected):
        with open(testdatapath) as f:
            obj = Sheldon(f.read(), testdatapath)
            obj.analyze()
            self.assertEqual(len(expected), len(obj.divisions))
            for x, y in zip(expected, obj.divisions):
                self.assertEqual(x, y)

    def test_division(self):
        my_data_path = os.path.join(THIS_DIR, 'test-data/div.py')
        self._check(my_data_path, [(1, "Num", "Num")])

    def test_nested_division(self):
        expected = [(1, "Num", "BinOp"), (1, "Num", "Num")]
        my_data_path = os.path.join(THIS_DIR,
                                    "test-data/more-test-data/nested_div.py")
        self._check(my_data_path, expected)

    def test_empty(self):
        my_data_path = os.path.join(THIS_DIR, "test-data/empty.py")
        self._check(my_data_path, [])

    def test_SyntaxError(self):
        my_data_path = os.path.join(THIS_DIR, "test-data/py2print.py")
        self._check(my_data_path, [(39, "SyntaxError")])

    def test_division_in_print(self):
        my_data_path = os.path.join(THIS_DIR, "test-data/printdiv.py")
        self._check(my_data_path, [(1, "Num", "Num")])

    def test_file_extension(self):
        my_data_dir = os.path.join(THIS_DIR, "test-data/")

        self.assertEqual(len(EXT_FILES), len(EXTENSIONS))

        for f in EXT_FILES:
            self._check(os.path.join(my_data_dir, f), [(1, "Num", "Num")])


if __name__ == "__main__":
    unittest.main()
