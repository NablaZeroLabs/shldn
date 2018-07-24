import unittest
from shldn.cooper import Sheldon

class TestSheldon(unittest.TestCase):

    def test_basic(self):
        """Input file with basic integer division"""

        obj = Sheldon("test-data/div.py")
        obj.analyze()

        expected = [(1, "Name", "Attribute")]

        self.assertEqual(len(expected), len(obj.divisions))

        for x, y in zip(expected, obj.divisions):
            self.assertEqual(x, y)

if __name__ == "__main__":
    unittest.main()
