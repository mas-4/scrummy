import os
from pathlib import Path

import pytest

from scrummy import config

HERE: Path = Path(__file__).parent


@pytest.fixture(scope="session", autouse=True)
def setup():
    scrummyrc: str = os.path.join(HERE, 'scrummyrc')
    config.conf = config.init_config(scrummyrc)
    config.conf.home = os.path.join(HERE, 'sample_data')