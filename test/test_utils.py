import unittest
import tempfile
import os
from src.Utils import writeCSSToFile

class UtilsTest(unittest.TestCase):

    def test_writeCSSToFile(self):
        with tempfile.TemporaryDirectory() as tempdir:
            # you can e.g. create a file here:
            cssfilepath = os.path.join(tempdir, 'styles.css')
            print(cssfilepath)
            with open(cssfilepath, 'w', encoding='utf-8') as cssfile:
                writeCSSToFile(cssfile)
            with open(cssfilepath, 'r', encoding='utf-8') as cssfile:
                self.assertEqual(cssfile.read(), """ul { list-style-type: " →  "; }\n""")
            os.remove(cssfilepath)
    