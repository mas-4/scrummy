import os
from pathlib import Path


class Constants:
    test_dir: Path = Path(__file__).parent
    sample_data_dir: str = os.path.join(test_dir, 'sample_data')
    test_data_dir: str = os.path.join(test_dir, 'test_data')
    ref_data_dir: str = os.path.join(test_dir, 'reference_data')

    # files
    scrummyrc: str = os.path.join(sample_data_dir, 'scrummyrc')
    christmas_2021_scrum: str = os.path.join(test_data_dir, 'scrum', '101-christmas-2021.md')
    smart_apartment_scrum: str = os.path.join(test_data_dir, 'scrum', '102-smart-apartment.md')
    scrummy_scrum: str = os.path.join(test_data_dir, 'scrum', '105-scrummy.md')

    christmas_2021_ref: str = os.path.join(ref_data_dir, 'scrum', '101-christmas-2021.md')
    smart_apartment_ref: str = os.path.join(ref_data_dir, 'scrum', '102-smart-apartment.md')
    scrummy_ref: str = os.path.join(ref_data_dir, 'scrum', '105-scrummy.md')
