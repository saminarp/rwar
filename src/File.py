import shutil
from os import listdir, mkdir
from os.path import isfile, join, isdir
from src import Utils


class SSG:
    def __init__(self, output, stylesheet, language):
        self.output = output
        self.language = language
        self.stylesheets = ["/style.css"]
        if stylesheet is not None:
            self.stylesheets.append(stylesheet)
        try:
            if Utils.checkIfOutFlag(self.output):
                mkdir(self.output)
            else:
                mkdir(self.output + "/dist")
        except FileExistsError:
            if Utils.checkIfOutFlag(self.output):  # default
                shutil.rmtree(self.output)
                mkdir(self.output)
            else:
                shutil.rmtree(self.output + "/dist")
                mkdir(self.output + "/dist")
        except FileNotFoundError:
            Utils.errLog("Specified output directory not found")
        self.write_stylesheet_file(self.stylesheets[0])

    def write_stylesheet_file(self, stylesheet):
        if Utils.checkIfOutFlag(self.output):
            with open(self.output + stylesheet, "w", encoding="utf-8") as file:
                # directory list styles
                Utils.writeCSSToFile(file)
        else:
            with open(
                self.output + "/dist" + stylesheet, "w", encoding="utf-8"
            ) as file:
                # directory list styles
                Utils.writeCSSToFile(file)

    def start(self, input, output=None):
        if Utils.checkIfOutFlag(self.output):
            output = self.output if output is None else output
        else:
            output = self.output + "/dist" if output is None else output
        if isfile(input) and input.endswith(".txt"):
            # single file, index of the static site
            self.process_txt_file(input, output.rstrip("/") + "/index.txt")
        elif isfile(input) and input.endswith(".md"):
            # single file, index of the static site
            self.process_md_file(input, output.rstrip("/") + "/index.md")
        elif isdir(input):
            self.process_dir(input, output)
        else:
            Utils.errLog("Invalid input file")

    def before_content(self, html_file, html_title):
        html_file.write("""<!DOCTYPE html>\n""")
        html_file.write(f"""<html lang="{self.language}">\n""")

        html_file.write("""<head>\n""")
        html_file.write("""<meta charset="UTF-8">\n""")
        html_file.write(
            """<meta name="viewport" content="width=device-width, initial-scale=1.0">\n"""
        )
        html_file.write("""<meta http-equiv="X-UA-Compatible" content="ie=edge">\n""")
        html_file.write(f"""<title>{html_title}</title>\n""")

        html_file.write(
            "\n".join(
                [
                    f"""<link rel="stylesheet" href="{stylesheet}">"""
                    for stylesheet in self.stylesheets
                ]
            )
        )

        html_file.write("""\n</head>\n""")

        html_file.write("""<body>\n""")
        html_file.write(f"""<h1>{html_title}</h1>\n""")
        html_file.write("""<div class="content">\n""")

    def after_content(self, html_file):
        html_file.write("""</div>\n""")
        html_file.write("""</body>\n""")
        html_file.write("""</html>\n""")

    def process_txt_file(self, input_path, output_path):
        with open(input_path, "r", encoding="utf-8") as txt_file:
            lines = txt_file.readlines()
        title = output_path.split("/")[-1][:-4]  # filename
        title = title if title != "index" else output_path.split("/")[-2]
        try:
            title = lines[0].strip()
            lines = lines[3:]
            print(">> ", output_path.split("/")[-1][:-4])
        except IndexError:
            if len(lines) == 0 and input_path.endswith(".txt"):
                Utils.errLog(f"Empty file passed: {title}.txt")

        with open(output_path[:-4] + ".html", "w", encoding="utf-8") as html_file:
            self.before_content(html_file, title)

            last_paragrph_index = 0
            for i in range(len(lines)):
                if lines[i] == "\n":
                    html_file.write("""<p>\n""")
                    html_file.write(" ".join(lines[last_paragrph_index:i]))
                    html_file.write("""</p>\n""")
                    last_paragrph_index = i + 1
            # If there is no empty line at the end of the file
            if last_paragrph_index < len(lines):
                html_file.write("""<p>\n""")
                html_file.write(" ".join(lines[last_paragrph_index:]))
                html_file.write("""</p>\n""")

            self.after_content(html_file)

    def process_md_file(self, input_path, output_path):
        with open(input_path, "r", encoding="utf-8") as md_file:
            lines = md_file.readlines()

        title = output_path.split("/")[-1][:-3]  # index
        title = title if title != "index" else output_path.split("/")[-2]
        print(">> ", title)

        for i in range(len(lines)):
            if lines[i].endswith("  \n"):
                lines[i] = lines[i][:-3] + "<br>\n"

        with open(output_path[:-3] + ".html", "w", encoding="utf-8") as html_file:
            self.before_content(html_file, title)

            last_paragraph_index = 0
            for i in range(len(lines)):
                if lines[i] == "\n" and last_paragraph_index < i:
                    html_file.write("""<p>\n""")
                    html_file.write(" ".join(lines[last_paragraph_index:i]))
                    html_file.write("""</p>\n""")
                    last_paragraph_index = i + 1
                elif lines[i] == "---\n" or lines[i] == "___\n" or lines[i] == "***\n":
                    # Print if pending text exists
                    if last_paragraph_index < i:
                        html_file.write("""<p>\n""")
                        html_file.write(" ".join(lines[last_paragraph_index:i]))
                        html_file.write("""</p>\n""")
                    # Print the hr
                    html_file.write("""<hr>\n""")
                    last_paragraph_index = i + 1
                elif lines[i].startswith("#"):
                    tag = "h" + str(lines[i].count("#"))

                    # Print if pending text exists
                    if last_paragraph_index < i:
                        html_file.write("""<p>\n""")
                        html_file.write(" ".join(lines[last_paragraph_index:i]))
                        html_file.write("""</p>\n""")
                    # check if hashtag
                    if lines[i].startswith("#"):
                        html_file.write(
                            f"""\n<{tag}>""" + lines[i].strip("# ") + f"""</{tag}>\n"""
                        )
                    last_paragraph_index = i + 1
            # If there is no empty line at the end of the file
            if last_paragraph_index < len(lines):
                html_file.write("""<p>\n""")
                html_file.write(" ".join(lines[last_paragraph_index:]))
                html_file.write("""</p>\n""")

            self.after_content(html_file)

    def process_dir(self, input_path, output_path):
        # directories in input folder
        directories = sorted(
            [f for f in listdir(input_path) if isdir(join(input_path, f))]
        )

        # files in input folder
        txt_files = sorted(
            [
                f
                for f in listdir(input_path)
                if isfile(join(input_path, f)) and f.endswith(".txt")
            ]
        )
        md_files = sorted(
            [
                f
                for f in listdir(input_path)
                if isfile(join(input_path, f)) and f.endswith(".md")
            ]
        )
        # recursively process directories
        for directory in directories:
            mkdir(join(output_path, directory))
            self.process_dir(join(input_path, directory), join(output_path, directory))

        # process txt files
        for txt_file in txt_files:
            self.process_txt_file(
                join(input_path, txt_file), join(output_path, txt_file)
            )

        # process md files
        for md_file in md_files:
            self.process_md_file(join(input_path, md_file), join(output_path, md_file))

        # title excluding the destination directory path
        title = output_path[len(self.output) :]
        title = title if title != "" else "RWAR"
        # exclude the first slash
        title = title[1:] if title.startswith("/") else title

        # create index.html file
        with open(join(output_path, "index.html"), "w", encoding="utf-8") as html_file:

            self.before_content(html_file, title)

            html_file.write("""<ul>\n""")
            # List directories at first
            html_file.write(
                "\n".join(
                    [
                        f"""<li><a href="{directory}/index.html">{directory}</a></li>"""
                        for directory in directories
                    ]
                )
            )
            html_file.write("\n")
            # List files afterwards
            html_file.write(
                "\n".join(
                    [
                        f"""<li><a href="{txtfile[:-4]+'.html'}">{txtfile[:-4]}</a></li>"""
                        for txtfile in txt_files
                    ]
                )
            )

            html_file.write(
                "\n".join(
                    [
                        f"""<li><a href="{mdfile[:-3]+'.html'}">{mdfile[:-3]}</a></li>"""
                        for mdfile in md_files
                    ]
                )
            )
            html_file.write("""\n</ul>\n""")

            self.after_content(html_file)
