import os
import shutil
from pathlib import Path

import pytest

from scrummy import config

HERE: Path = Path(__file__).parent
sample_data_dir: str = os.path.join(HERE, 'sample_data')
test_data_dir: str = os.path.join(HERE, 'test_data')


@pytest.fixture(scope="session", autouse=True)
def session_level_setup():
    scrummyrc: str = os.path.join(HERE, 'scrummyrc')
    config.conf = config.init_config(scrummyrc)
    config.conf.home = test_data_dir


@pytest.fixture(scope="function", autouse=True)
def test_level_setup():
    if not os.path.exists(test_data_dir):
        shutil.copytree(sample_data_dir, test_data_dir)
    else:
        shutil.rmtree(test_data_dir)
        shutil.copytree(sample_data_dir, test_data_dir)
    yield
    shutil.rmtree(test_data_dir)
