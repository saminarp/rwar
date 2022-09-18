<!-- PROJECT LOGO -->
<br />
<div align="center">

  <img src="https://i.imgur.com/wWF6kL8.png" alt="Logo" width="200" height="200">

<h3 align="center">rwar</h3>
  <p align="center">
    A Simple Static Site Generator  <br> Written in Python
    <br />
    </a>
  </p>
   <a href="https://rwarr.netlify.app">Demo</a> . <a href="https://dev.to/saminarp/rwar-a-simple-static-site-generator-2b5a">Blog</a>
</div>

## Overview

__rwar__ - A simple bare-bones Static Site Generator (SSG) with minimal features. An SSG allows a user to generate a complete HTML website from raw data and files, without having to write out the HTML. Rwar is a command line tool that takes .txt files as input and generates .html files as output.

## Usage

Please ensure Python 3 is installed.

The `requirements.txt` file lists all the dependencies needed for `rwar`

To satisfy these requirements run the following command `pip install -r requirements.txt`
 You can then run the program by running the following command:

```bash
# satisfy the dependencies listed in requirements.txt
pip install -r requirements.txt
# (For input either put .txt file or specify the directory containing txt files)
python3 rwar.py -i <input> 
```

If you are in a Unix environment, you can use the following commands to run:

```bash
# make it executable
chmod +x rwar.py 
# run
./rwar.py -i <input> 
```

> **Note:** If you are not in Unix env, you may need to use `python` instead of `python3`.

- The program will generate a static site in the `./dist` directory within the project by default. You can change this behavior by using the `-o` flag. If you choose to specify your desired directory, it will create dist as a sub-folder within the directory you specify.
- You can also provide a custom stylesheet by using the `-s` flag.
- To see all available options, run the following command: `./rwar -h` or `python3 rwar.py -h`

### Flags
| Flag | Description | Required / Optional |
| --- | --- | --- |
| `-i` | Specify raw data directory or file e.g. use `data` directory in the repo | Required |
| `-o` | The program will generate a static site in the `./dist` directory within the project by default. You can change this behavior by using the `-o` flag. If you choose to specify your desired directory, it will create dist as a sub-folder within the directory you specify. | Optional |
| `-s` | Provide a custom stylesheet by using the `-s` flag<br> By default it uses [water.css](https://cdn.jsdelivr.net/npm/water.css@2/out/water.css)| Optional|
| `-h` | This will display all the available options and usage of `rwar` | Optional |