import shutil
from os import listdir, mkdir
from os.path import isfile, join, isdir
from src import Utils

#


class SSG:
    def __init__(self, output, stylesheet, language):
        self.output = output
        self.language = language
        self.stylesheets = ['/style.css']
        if stylesheet is not None:
            self.stylesheets.append(stylesheet)
        try:
            if Utils.checkIfOutFlag(self.output):
                mkdir(self.output)
            else:
                mkdir(self.output + '/dist')
        except FileExistsError:
            if Utils.checkIfOutFlag(self.output):  # default
                shutil.rmtree(self.output)
                mkdir(self.output)
            else:
                shutil.rmtree(self.output + '/dist')
                mkdir(self.output + '/dist')
        except FileNotFoundError:
            Utils.errLog('Specified output directory not found')
        self.write_stylesheet_file(self.stylesheets[0])

    def write_stylesheet_file(self, stylesheet):
        if Utils.checkIfOutFlag(self.output):
            with open(self.output + stylesheet, 'w', encoding='utf-8') as file:
                # directory list styles
                Utils.writeCSSToFile(file)
        else:
            with open(self.output + '/dist' + stylesheet, 'w', encoding='utf-8') as file:
                # directory list styles
                Utils.writeCSSToFile(file)

    def start(self, input, output=None):
        if Utils.checkIfOutFlag(self.output):
            output = self.output if output is None else output
        else:
            output = self.output + '/dist' if output is None else output
        if isfile(input) and input.endswith('.txt'):
            # single file, index of the static site
            self.process_file(input, output.rstrip('/') + '/index.txt')
        elif isfile(input) and input.endswith('.md'):
            # single file, index of the static site
            self.process_md_file(input, output.rstrip('/') + '/index.md')
        elif isdir(input):
            self.process_dir(input, output)
        else:
            Utils.errLog('Invalid input file')

    def process_file(self, input, output):
        with open(input, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        title = output.split('/')[-1][:-4]  # filename
        title = title if title != 'index' else output.split('/')[-2]
        try:
            title = lines[0].strip()
            lines = lines[3:]
            print(">> ", output.split('/')[-1][:-4])
        except IndexError:
            if len(lines) == 0 and input.endswith('.txt'):
                Utils.errLog(f'Empty file passed: {title}.txt')

        with open(output[:-4]+'.html', 'w', encoding='utf-8') as file:
            file.write('''<!DOCTYPE html>\n''')
            file.write(f'''<html lang="{self.language}">\n''')

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
            for i in range(len(lines)):
                if lines[i] == '\n':
                    file.write('''<p>\n''')
                    file.write(' '.join(lines[last_i:i]))
                    file.write('''</p>\n''')
                    last_i = i + 1
            # If there is no empty line at the end of the file
            if last_i < len(lines):
                file.write('''<p>\n''')
                file.write(' '.join(lines[last_i:]))
                file.write('''</p>\n''')

            file.write('''</div>\n''')
            file.write('''</body>\n''')

            file.write('''</html>''')

    def process_md_file(self, input, output):
        with open(input, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        title = output.split('/')[-1][:-3]  # index
        title = title if title != 'index' else output.split('/')[-2]
        print(">> ", title)
        for i in range(len(lines)):
            if (lines[i].endswith('  \n')):
                lines[i] = lines[i][:-3] + '<br>\n'

        with open(output[:-3]+'.html', 'w', encoding='utf-8') as file:
            file.write('''<!DOCTYPE html>\n''')
            file.write(f'''<html lang="{self.language}">\n''')

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
            for i in range(len(lines)):
                if lines[i] == '\n' and last_i < i:
                    file.write('''<p>\n''')
                    file.write(' '.join(lines[last_i:i]))
                    file.write('''</p>\n''')
                    last_i = i + 1
                elif lines[i] == '---\n' or lines[i] == '___\n' or lines[i] == '***\n':
                    # Print if pending text exists
                    if (last_i < i):
                        file.write('''<p>\n''')
                        file.write(' '.join(lines[last_i:i]))
                        file.write('''</p>\n''')
                    # Print the hr
                    file.write('''<hr>\n''')
                    last_i = i + 1
                elif lines[i].startswith('#'):
                    tag = 'h' + str(lines[i].count('#'))

                    # Print if pending text exists
                    if (last_i < i):
                        file.write('''<p>\n''')
                        file.write(' '.join(lines[last_i:i]))
                        file.write('''</p>\n''')
                    # check if hashtag
                    if (lines[i].startswith('#')):
                        file.write(
                            f'''\n<{tag}>''' + lines[i].strip('# ') + f'''</{tag}>\n''')
                    last_i = i + 1
            # If there is no empty line at the end of the file
            if last_i < len(lines):
                file.write('''<p>\n''')
                file.write(' '.join(lines[last_i:]))
                file.write('''</p>\n''')

            file.write('''</div>\n''')
            file.write('''</body>\n''')

            file.write('''</html>''')

    def process_dir(self, input, output):
        # directories in input folder
        onlydir = sorted([f for f in listdir(input) if isdir(join(input, f))])

        # files in input folder
        onlytxt = sorted([f for f in listdir(input) if isfile(
            join(input, f)) and f.endswith('.txt')])
        onlymd = sorted([f for f in listdir(input) if isfile(
            join(input, f)) and f.endswith('.md')])
        # recursively process directories
        for directory in onlydir:
            mkdir(join(output, directory))
            self.process_dir(join(input, directory), join(output, directory))

        # process txt files
        for txtfile in onlytxt:
            self.process_file(join(input, txtfile), join(output, txtfile))

        # process md files
        for mdfile in onlymd:
            self.process_md_file(join(input, mdfile), join(output, mdfile))

        # title excluding the destination directory path
        title = output[len(self.output):]
        title = title if title != '' else 'RWAR'
        # exclude the first slash
        title = title[1:] if title.startswith('/') else title
        # create index.html file
        with open(join(output, 'index.html'), 'w', encoding='utf-8') as file:

            file.write('''<!DOCTYPE html>\n''')
            file.write(f'''<html lang="{self.language}">\n''')

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

            file.write('''<ul>\n''')
            # List directories at first
            file.write('\n'.join(
                [f'''<li><a href="{directory}/index.html">{directory}</a></li>'''
                 for directory in onlydir]))
            file.write('\n')
            # List files afterwards
            file.write('\n'.join(
                [f'''<li><a href="{txtfile[:-4]+'.html'}">{txtfile[:-4]}</a></li>'''
                 for txtfile in onlytxt]))

            file.write('\n'.join(
                [f'''<li><a href="{mdfile[:-3]+'.html'}">{mdfile[:-3]}</a></li>'''
                 for mdfile in onlymd]))
            file.write('''\n</ul>\n''')

            file.write('''</div>\n''')
            file.write('''</body>\n''')

            file.write('''</html>''')
