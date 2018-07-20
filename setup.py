import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

about = {}
with open(os.path.join(here, "sheldon", "__version__.py")) as v:
    exec(v.read(), about)

required = [
    "setuptools>=36.2.1",
]

setup(
    name="sheldon",
    version=about["__version__"],
    author="Pablo Ordorica-Wiener",
    author_email="pablo.ordorica@nablazerolabs.com",
    description="Find divisions in Python code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NablaZeroLabs/sheldon",
    packages=find_packages(),
    entry_points = {
        "console_scripts": ["sheldon=sheldon.leonard:main"]
    },
    python_requires=">=3.7",
    install_requires=required,
    license="MIT",
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
