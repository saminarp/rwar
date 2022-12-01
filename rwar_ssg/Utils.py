from clint.textui import puts, colored, indent
from pyfiglet import Figlet


def greeting():
    f = Figlet(font="slant")
    puts(colored.magenta(f.renderText("rwar")))
    puts(
        colored.green(
            "Static site generator to create a website from a directory of text files"
        )
    )
    puts(colored.green("Version 0.1"))


def errLog(msg):
    with indent(4, quote=">>>"):
        puts(colored.red(msg))


def checkIfOutFlag(output):
    if output == "./dist":
        return True
    return False


def writeCSSToFile(file):
    # directory list styles
    file.write("""ul { list-style-type: " →  "; }\n""")
