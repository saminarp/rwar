<!-- PROJECT LOGO -->
<br />
<div align="center">

  <img src="./logo/lion.png" alt="Logo" width="200" height="200">

<h3 align="center">rwar</h3>
  <p align="center">
    A Simple Static Site Generator  <br> Written in Python
    <br />
    </a>
  </p>
</div>

## Usage

Please ensure Python 3 is installed.\
The `requirements.txt` file lists all the dependencies needed for `rwar`

To satisfy these requirements run the following command `pip install -r requirements.txt`
 You can then run the program by running the following command:

```bash
python3 rwar.py -i <input> # (For input either put .txt file or specify the directory containing txt files)
```

If you are in a Unix environment, you can use the following commands to run:

```bash
chmod +x rwar.py # This will make the file executable
./rwar.py -i <input> #works in macOS or Unix based systems
```

> **Note:** If you are not using bash, you may need to use `python` instead of `python3`.

- The program will generate a static site in the `./dist` directory within the project by default. You can change this behavior by using the `-o` flag. If you choose to specify your desired directory, it will create dist as a sub-folder within the directory you specify.
- You can also provide a custom stylesheet by using the `-s` flag.
- To see all available options, run the following command: `./rwar -h` or `python3 rwar.py -h`
