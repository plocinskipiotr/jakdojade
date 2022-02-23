import pytest

from backend.src.validate_path import validate_path_file

CSV_PATH = '../testdata/data.csv'
invalid_path = 'invalid'


class TestValidatePath:

    def test_valid_path(self):
        assert validate_path_file(CSV_PATH) == CSV_PATH

    def test_invalid_path(self):
        with pytest.raises(FileNotFoundError):
            validate_path_file(invalid_path)
