import unittest
import tempfile
import os
from rwar_ssg.Parser import get_parser_args


class CLIParser(unittest.TestCase):
    def test_without_input(self):
        with self.assertRaises(SystemExit) as err:
            get_parser_args([])
        self.assertEqual(err.exception.code, 2, "No input directory provided")

    def test_input_directory_with_other_defaults(self):
        args = get_parser_args(["-i", "./input_dir"])
        self.assertEqual(args.input[0], "./input_dir")
        args = get_parser_args(["--input", "./input_dir"])
        self.assertEqual(args.input[0], "./input_dir")

        self.assertEqual(args.output[0], "./dist")
        self.assertEqual(
            args.stylesheet[0], "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"
        )
        self.assertEqual(args.lang[0], "en-CA")

    def test_output_directory(self):
        args = get_parser_args(["-i", "./input_dir", "-o", "./output"])
        self.assertEqual(args.output[0], "./output")
        args = get_parser_args(
            [
                "--output",
                "./output",
                "-i",
                "./input_dir",
            ]
        )
        self.assertEqual(args.output[0], "./output")

    def test_config_file_unavailable(self):
        with self.assertRaises(SystemExit) as err:
            get_parser_args(["-c", "./config_file.json"])
        self.assertEqual(err.exception.code, 3)

    def test_config_file_default(self):
        with tempfile.TemporaryDirectory() as tempdir:
            # you can e.g. create a file here:
            configfilepath = os.path.join(tempdir, "config_temp.json")
            print(configfilepath)
            with open(configfilepath, "w") as configfile:
                configfile.write('{"input" : "./input_dir"}')
            args = get_parser_args(["--config", configfilepath])
            self.assertEqual(args.input[0], "./input_dir")
            self.assertEqual(args.output[0], "./dist")
            self.assertEqual(
                args.stylesheet[0],
                "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css",
            )
            self.assertEqual(args.lang[0], "en-CA")
            os.remove(configfilepath)

    def test_config_file_other(self):
        with tempfile.TemporaryDirectory() as tempdir:
            # you can e.g. create a file here:
            configfilepath = os.path.join(tempdir, "config_temp.json")
            print(configfilepath)
            with open(configfilepath, "w") as configfile:
                configfile.write(
                    '{"input" : "./input_dir", "output": "./output", "lang": "en-UK"}'
                )
            args = get_parser_args(["--config", configfilepath])
            self.assertEqual(args.input[0], "./input_dir")
            self.assertEqual(args.output[0], "./output")
            self.assertEqual(
                args.stylesheet[0],
                "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css",
            )
            self.assertEqual(args.lang[0], "en-UK")
            os.remove(configfilepath)

    def test_config_file_undefined(self):
        with tempfile.TemporaryDirectory() as tempdir:
            # you can e.g. create a file here:
            configfilepath = os.path.join(tempdir, "config_temp.json")
            print(configfilepath)
            with open(configfilepath, "w") as configfile:
                configfile.write(
                    '{"input" : "./input_dir", "output": "./output", "language": "en-UK"}'
                )
            args = get_parser_args(["--config", configfilepath])
            self.assertEqual(args.input[0], "./input_dir")
            self.assertEqual(args.output[0], "./output")
            self.assertEqual(
                args.stylesheet[0],
                "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css",
            )
            self.assertEqual(args.lang[0], "en-CA")
            os.remove(configfilepath)


if __name__ == "__main__":
    unittest.main()
