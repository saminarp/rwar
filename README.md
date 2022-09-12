# Simple Static Site Generator (rwar)

This is a simple static site generator written in Python.

## Usage

To use this program, you must have Python 3 installed. You can then run the program by running the following command:

```python rwar.py -i <input directory>```

> **Note:** Unix users may need to use `python3` instead of `python`.
> If you are using bash, you can use the following command to run the program:
```./rwar.py -i <input directory>```

The program will then generate a static site in the `./dist` directory by default. You can change this by using the `-o` flag.

You can also provide a custom stylesheet by using the `-s` flag.

To see all available options, run the following command:

    python rwar.py -h
