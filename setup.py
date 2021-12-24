from setuptools import setup, find_packages
from scrummy import __version__

setup(
    name='scrummy',
    __version__=__version__.__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click', 'python-dateutil', 'xdg'],
    entry_points={
        'console_scripts': [
            'scrummy = scrummy.main:cli',
        ]
    }
)
