from setuptools import setup
from scrummy import __version__

setup(
    name='scrummy',
    __version__=__version__.__version__,
    py_modules=['scrummy', 'main'],
    install_requires=['click', 'python-dateutil', 'xdg'],
    entry_points={
        'console_scripts': [
            'scrummy = main:cli',
        ]
    }
)
