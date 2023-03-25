from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from unittest import TestCase

import polars as pl
from typer.testing import CliRunner

from json_to_csv_lol.main import app

runner = CliRunner()


class ConvertCommandTest(TestCase):
    def test_command(self):
        self.input_path = Path("test.json")
        self.output_path = Path("test-converted.csv")
        self.df = pl.DataFrame({"A": [1, 2, 3], "B": ["foo", "bar", "baz"]})
        self.df.write_json(self.input_path)

        result = runner.invoke(app, ['test.json'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn('Successfuly converted!', result.stdout)
        df_result = pl.read_csv(self.output_path)
        self.assertTrue(self.df.frame_equal(df_result))

    def test_check_input(self):
        @dataclass
        class TestCaseScenario:
            input_path: Path
            expected_exit_code: int
            expected_error_message: Optional[str]
            touch_file: Optional[bool] = False
            output_path: Optional[Path] = None

        test_cases = [
            TestCaseScenario(
                input_path=Path("test.json"),
                expected_exit_code=1,
                expected_error_message='File does not exist',
            ),
            TestCaseScenario(
                input_path=Path("."),
                expected_exit_code=1,
                expected_error_message='It is not a file',
            ),
            TestCaseScenario(
                input_path=Path("test.pdf"),
                expected_exit_code=1,
                expected_error_message='It is not a json file',
                output_path=Path('.'),
                touch_file=True,
            ),
            TestCaseScenario(
                input_path=Path("test.json"),
                expected_exit_code=1,
                expected_error_message='Output path is not a dir',
                output_path=Path('test.csv'),
                touch_file=True,
            ),
        ]

        for test_case in test_cases:
            if test_case.touch_file:
                test_case.input_path.touch()
                test_case.output_path.touch()

            args = [
                test_case.input_path.name,
            ]
            if test_case.output_path:
                args.append('--output-path')
                args.append(test_case.output_path.name)

            result = runner.invoke(app, args)
            self.assertEqual(result.exit_code, test_case.expected_exit_code)
            self.assertIn(test_case.expected_error_message, result.stdout)

            if test_case.touch_file:
                test_case.input_path.unlink()
                test_case.output_path.touch()
