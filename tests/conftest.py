import os
import shutil

import pytest

from scrummy import config
from constants import Constants


@pytest.fixture(scope="session", autouse=True)
def session_level_setup():
    config.conf = config.init_config(Constants.scrummyrc)
    config.conf.home = Constants.test_data_dir


@pytest.fixture(scope="function", autouse=True)
def test_level_setup():
    if not os.path.exists(Constants.test_data_dir):
        shutil.copytree(Constants.sample_data_dir, Constants.test_data_dir)
    else:
        shutil.rmtree(Constants.test_data_dir)
        shutil.copytree(Constants.sample_data_dir, Constants.test_data_dir)
    yield
    shutil.rmtree(Constants.test_data_dir)
