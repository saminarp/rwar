from clint.textui import puts, colored, indent
from pyfiglet import Figlet


def greeting():
    f = Figlet(font='slant')
    puts(colored.magenta(f.renderText('rwar')))
    puts(colored.green(
        'Static site generator to create a website from a directory of text files'))
    puts(colored.green('Version 0.1'))


def errLog(msg):
    with indent(4, quote='>>>'):
        puts(colored.red(msg))


def checkIfOutFlag(output):
    if output == './dist':
        return True
    return False


def writeCSSToFile(file):
    # directory list styles
    file.write('''ul { list-style-type: "→"; color: orange }\n''')
    file.write('''li { padding-left: 10px; margin-bottom: 5px;}\n''')
    file.write(
        '''a { text-decoration: none; color: #008080; }\na:hover
        { text-decoration: dotted underline; }\n''')
    file.write('''body { background-color: #000000; }\n''')

    # title style
    file.write(
        '''h1 { text-align: center;
        font-family: 'Times New Roman', serif; font-style: bold; color: green; }\n''')
    # main content style
    file.write(
        '''div.content { max-width: 920px; font-family: Arial, sans-serif; padding: 20px;
        border: 1px solid #111; background-color: #ffffff; margin: 20px auto; }\n''')
