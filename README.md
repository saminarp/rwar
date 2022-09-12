# Rwar Static Site Generator 🦁

Simple static site generator written in Python.

## Usage

To use this program, you must have Python 3 installed. The `requirements.txt` file is listing all the dependencies for `rwar`. To satisfy these requirements run the following command `pip3 install -r requirements.txt`
 You can then run the program by running the following command:

```python
python3 rwar.py -i <input directory>
```

If you are in in Unix environment, you can use the following command to run:

```bash
./rwar.py -i <input directory> #works in macOS
```

> **Note:** If you are not using bash you may need to use `python` instead of `python3`.

- The program will then generate a static site in the `./dist` directory by default. You can change this by using the `-o` flag.
- You can also provide a custom stylesheet by using the `-s` flag.
- To see all available options, run the following command:
- To see all available options, run the following command: `./rwar -h`
