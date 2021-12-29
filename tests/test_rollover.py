from scrummy.rollover import rollover_todo
from pathlib import Path
from constants import Constants


def compare_files(ref_path: str, target_path: str):
    filename: str = Path(ref_path).stem

    with open(ref_path, 'rt') as fin:
        ref = fin.readlines()
    with open(target_path, 'rt') as fin:
        target = fin.readlines()

    assert len(ref) == len(target), f"Ref and produced files not the same length for {filename}"

    for i, ref_line, target_line in enumerate(zip(ref, target)):
        assert ref_line == target_line, f"{filename} line {i} does not match ref" \
                                        + "\n".join([ref_line, target_line])


def test_rollover():
    rollover_todo('tomorrow')
    compare_files(Constants.christmas_2021_ref, Constants.christmas_2021_scrum)
    compare_files(Constants.smart_apartment_ref, Constants.smart_apartment_scrum)
