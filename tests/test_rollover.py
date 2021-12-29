from pathlib import Path

from constants import Constants
from scrummy.rollover import rollover_todo


def compare_files(actual_path: str, expected_path: str):
    filename: str = Path(actual_path).stem

    with open(actual_path, 'rt') as fin:
        actual: list[str] = fin.readlines()
    with open(expected_path, 'rt') as fin:
        expected: list[str] = fin.readlines()

    assert len(actual) == len(expected), f"Ref and produced files not the same length for {filename}"

    for i, (actual_line, expected_line) in enumerate(zip(actual, expected)):
        assert actual_line == expected_line, f"{filename} line {i} does not match actual" \
                                        + "\n".join([actual_line, expected_line])


def test_rollover():
    rollover_todo('tomorrow')
    compare_files(Constants.christmas_2021_actual, Constants.christmas_2021_expected)
    compare_files(Constants.smart_apartment_actual, Constants.smart_apartment_expected)
