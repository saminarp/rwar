import shutil
from os import mkdir
from os.path import isfile, isdir


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

    def write_stylesheet_file(self, stylesheet):
        with open(self.output + stylesheet, 'w', encoding='utf-8') as file:
            # directory list styles
            file.write('''ul { list-style-type: "→"; }\n''')
            file.write('''li { padding-left: 10px; margin-bottom: 5px;}\n''')
            file.write(
                '''a { text-decoration: none; color: #008080; }\na:hover
                { text-decoration: dotted underline; }\n''')

            file.write('''body { background-color: #bbb; }\n''')

            # title style
            file.write(
                '''h1 { text-align: center;
                font-family: 'Times New Roman', serif; font-style: italic; }\n''')

            # main content style
            file.write(
                '''div.content { max-width: 920px; font-family: Arial, sans-serif; padding: 20px;
                border: 1px solid #111; background-color: #fff; margin: 20px auto; }\n''')

    def start(self, input, output=None):
        output = self.output if output is None else output

        if isfile(input) and input.endswith('.txt'):
            # single file, index of the static site
            self.process_file(input, output.rstrip('/') + '/index.txt')
        elif isdir(input):
            self.process_dir(input, output)

    def process_file(self, input, output):
        with open(input, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        title = output.split('/')[-1][:-4]  # index

        if len(lines) >= 3 and lines[1] == lines[2] == '\n':
            title = lines[0].strip()
            lines = lines[3:]
            print(title)
        with open(output[:-4]+'.html', 'w', encoding='utf-8') as file:
            file.write('''<!DOCTYPE html>\n''')
            file.write('''<html lang="en">\n''')

            file.write('''<head>\n''')
            file.write('''<meta charset="UTF-8">\n''')
            file.write(
                '''<meta name="viewport" content="width=device-width, initial-scale=1.0">\n''')
            file.write(
                '''<meta http-equiv="X-UA-Compatible" content="ie=edge">\n''')
            file.write(f'''<title>{title}</title>\n''')

            file.write('\n'.join(
                [f'''<link rel="stylesheet" href="{stylesheet}">'''
                 for stylesheet in self.stylesheets]))

            file.write('''\n</head>\n''')

            file.write('''<body>\n''')
            file.write(f'''<h1>{title}</h1>\n''')

            file.write('''<div class="content">\n''')
            last_i = 0
            for i, line in enumerate(lines[last_i:]):
                if line == '\n':
                    file.write('''<p>\n''')
                    file.write(' '.join(lines[last_i:last_i+i]))
                    file.write('''</p>\n''')
                    last_i = last_i + i + 1
            # If there is no empty line at the end of the file
            if last_i < len(lines):
                file.write('''<p>\n''')
                file.write(' '.join(lines[last_i:]))
                file.write('''</p>\n''')

            file.write('''</div>\n''')
            file.write('''</body>\n''')

            file.write('''</html>''')
