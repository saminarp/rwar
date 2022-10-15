from clint.textui import puts, colored, indent
from pyfiglet import Figlet


def greeting():

    figlet = Figlet(font="slant")
    puts(colored.magenta(figlet.renderText("rwar")))

    puts(
        colored.green(
            "Static site generator to create a website from a directory of text files"
        )
    )
    puts(colored.green("Version 0.1"))


def err_log(message):
    with indent(4, quote=">>>"):
        puts(colored.red(message))


def check_if_out_flag(output):

    if output == "./dist":
        return True
    return False


def write_css_to_file(css_file):
    # directory list styles
    css_file.write("""ul { list-style-type: " →  "; }\n""")
