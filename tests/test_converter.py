from json_to_csv_lol.converter import convert
from pathlib import Path
import polars as pl

from unittest import TestCase


class ConverterTest(TestCase):
    def setUp(self):
        self.input_path = Path("test.json")
        self.output_path = Path("test.csv")
        self.df = pl.DataFrame({"A": [1, 2, 3], "B": ["foo", "bar", "baz"]})
        self.df.write_json(self.input_path)

    def test_convert(self):
        convert(self.input_path, self.output_path)
        df_result = pl.read_csv(self.output_path)
        self.assertTrue(self.df.frame_equal(df_result))

    def tearDown(self):
        self.input_path.unlink()
        self.output_path.unlink()
