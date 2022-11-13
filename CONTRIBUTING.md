# Contributing

Prior to contributing to this repository, please reach out to the owner of this repository to discuss the changes you wish to make either through creating an issue, emailing the owner, or any other preferred method of communication. 

## Built With 
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

Using the legacy release of [Python 3.9.0](https://www.python.org/downloads/release/python-390/) 

## Installation
rwar uses `requirements.txt` to keep track of modules used. To install the modules listed in this file, run the following command:

```bash
pip3 install -r requirements.txt
```
> **Note:** If your changes require additional modules, please add them to the `requirements.txt` file before raising PR. This can be done with the command `pip3 freeze > requirements.txt`


## Formatting
As the source code formatter, rwar uses [black](https://pypi.org/project/black/). Ensure you run the following command after your changes have been implemented.
```sh
black ./rwar.py ./src/
```

## Linting

rwar follows the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide and uses [pylint](https://pypi.org/project/pylint/) to enforce this. To lint your code, run the following command:
```sh
pylint ./rwar.py ./src/
```

## Testing 

rwar uses the [unittest](https://docs.python.org/3/library/unittest.html) framework for testing. To test the code, run the following command: 
```sh
python3 -m unittest discover  
```
