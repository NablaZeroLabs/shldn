import os
import io

from setuptools import setup, find_packages

import shldn

# Package meta-data.
NAME = 'shldn'
DESCRIPTION = 'Find divisions in Python code'
URL = 'https://github.com/NablaZeroLabs/shldn'
AUTHOR = 'Nabla Zero Labs'
AUTHOR_EMAIL = 'pablo.ordorica@nablazerolabs.com'
MAINTAINER = 'Pablo Ordorica Wiener'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))
# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=shldn.__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": ["shldn=shldn.leonard:main"]
    },
    python_requires=REQUIRES_PYTHON,
    license="MIT",
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
