import time
import unittest
import tempfile
import os
from os.path import join
from src.File import SSG


def write_txt(path):
    with open(path, "w") as wo_title:
        wo_title.writelines(
            [
                "Page Title\n\n\n",
                "This is a paragraph\n",
                "which is continued until we find two newline chars\n\n",
                "This is another paragraph",
            ]
        )


def write_md(path):
    with open(path, "w") as wo_title:
        wo_title.writelines(
            [
                "# This is heading 1\n",
                "## This is heading 2\n",
                "### This is heading 3\n",
                "---\n",
                "This is a paragraph with __bold__ , _italic_ and `code` text ",
                "with [Google](https://www.google.com) and an Image",
                " ![Arsenal](https://ssl.gstatic.com/onebox/media/sports/logos/4us2nCgl6kgZc0t3hpW75Q_96x96.png)\n\n",
                "This is another paragraph\n\n",
                "- list item 1\n",
                "- list item 2\n",
            ]
        )


class SSGTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()

        self.output = self.tempdir.name
        self.input = os.path.join(self.output, "input")
        os.mkdir(self.input)
        self.stylesheet = "test-stylesheet-link"

    def tearDown(self):
        self.tempdir.cleanup()

    def test_stylesheet_write(self):
        SSG(self.output, self.stylesheet, language="en-UK")

        with open(
            os.path.join(self.output, "dist", "style.css"), "r", encoding="utf-8"
        ) as css:
            self.assertEqual(css.readline(), """ul { list-style-type: " →  "; }\n""")

    def test_text_file(self):
        ssg = SSG(self.output, self.stylesheet, language="en-US")

        write_txt(join(self.input, "Text File.txt"))
        ssg.start(self.input)
        expected = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Page Title</title>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="test-stylesheet-link">
</head>
<body>
<h1>Page Title</h1>
<div class="content">
<p>
This is a paragraph
 which is continued until we find two newline chars
</p>
<p>
This is another paragraph</p>
</div>
</body>
</html>"""

        with open(
            join(self.output, "dist", "Text File.html"), "r", encoding="utf-8"
        ) as html:
            lines = html.readlines()
            actual = "".join(lines)

        self.assertEqual(actual, expected)

    def test_markdown(self):
        ssg = SSG(self.output, self.stylesheet, language="en-US")

        write_md(join(self.input, "Markdown File.md"))
        ssg.start(self.input)

        expected = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Markdown File</title>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="test-stylesheet-link">
</head>
<body>
<h1>Markdown File</h1>
<div class="content">
<h1>This is heading 1</h1>

<h2>This is heading 2</h2>

<h2>### This is heading 3</h2>

<p>This is a paragraph with <strong>bold</strong> , <em>italic</em> and <code>code</code> text with <a href="https://www.google.com">Google</a> and an Image <img src="https://ssl.gstatic.com/onebox/media/sports/logos/4us2nCgl6kgZc0t3hpW75Q_96x96.png" alt="Arsenal" /></p>

<p>This is another paragraph</p>

<ul>
<li>list item 1</li>
<li>list item 2</li>
</ul>
</div>
</body>
</html>"""

        with open(
            join(self.output, "dist", "Markdown File.html"), "r", encoding="utf-8"
        ) as html:
            lines = html.readlines()
            actual = "".join(lines)

        self.assertEqual(actual, expected)

    def test_index_simple(self):
        ssg = SSG(self.output, self.stylesheet, language="en-US")

        write_txt(join(self.input, "Text File.txt"))
        write_md(join(self.input, "Markdown File.md"))

        ssg.start(self.input)

        expected = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>dist</title>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="test-stylesheet-link">
</head>
<body>
<h1>dist</h1>
<div class="content">
<ul>

<li><a href="Text File.html">Text File</a></li><li><a href="Markdown File.html">Markdown File</a></li>
</ul>
</div>
</body>
</html>"""

        with open(
            join(self.output, "dist", "index.html"), "r", encoding="utf-8"
        ) as html:
            lines = html.readlines()
            actual = "".join(lines)

        self.assertEqual(actual, expected)

    def test_index_nested(self):
        ssg = SSG(self.output, self.stylesheet, language="en-US")

        write_txt(join(self.input, "Text File.txt"))
        os.mkdir(join(self.input, "nested-folder"))
        write_md(join(self.input, "nested-folder", "Markdown File.md"))

        ssg.start(self.input)

        expected = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>dist</title>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="test-stylesheet-link">
</head>
<body>
<h1>dist</h1>
<div class="content">
<ul>
<li><a href="nested-folder/index.html">nested-folder</a></li>
<li><a href="Text File.html">Text File</a></li>
</ul>
</div>
</body>
</html>"""

        with open(
            join(self.output, "dist", "index.html"), "r", encoding="utf-8"
        ) as html:
            lines = html.readlines()
            actual = "".join(lines)

        self.assertEqual(actual, expected)

        expected = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>dist/nested-folder</title>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="test-stylesheet-link">
</head>
<body>
<h1>dist/nested-folder</h1>
<div class="content">
<ul>

<li><a href="Markdown File.html">Markdown File</a></li>
</ul>
</div>
</body>
</html>"""

        with open(
            join(self.output, "dist", "nested-folder", "index.html"),
            "r",
            encoding="utf-8",
        ) as html:
            lines = html.readlines()
            actual = "".join(lines)

        self.assertEqual(actual, expected)
