import unittest
import tempfile
import os

from rwar_ssg.Utils import writeCSSToFile


class UtilsTest(unittest.TestCase):
    def test_writeCSSToFile(self):
        with tempfile.TemporaryDirectory() as tempdir:
            cssfilepath = os.path.join(tempdir, "styles.css")
            print(cssfilepath)
            with open(cssfilepath, "w", encoding="utf-8") as cssfile:
                writeCSSToFile(cssfile)
            with open(cssfilepath, "r", encoding="utf-8") as cssfile:
                self.assertEqual(
                    cssfile.read(), """ul { list-style-type: " →  "; }\n"""
                )
            os.remove(cssfilepath)
