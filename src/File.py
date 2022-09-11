import shutil
from os import mkdir


class SSG:
    def __init__(self, output, stylesheet):
        self.output = output
        self.stylesheets = ['/style.css']
        if stylesheet is not None:
            self.stylesheets.append(stylesheet)
        # existing destination directory is deleted
        shutil.rmtree(self.output, ignore_errors=True)
        # create destination directory
        mkdir(self.output)
        # create stylesheet file
        self.write_stylesheet_file(self.stylesheets[0])
