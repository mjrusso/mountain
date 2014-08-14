# -*- coding: utf-8 -*-

# Python project structure reference:
#
# - http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
# - http://gehrcke.de/2014/02/distributing-a-python-command-line-application/

import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('mountain/mountain.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "mountain",
    packages = ["mountain"],
    entry_points = {
        "console_scripts": ['mountain = mountain.mountain:main']
        },
    version = version,
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={'test': PyTest},
    extras_require={
        'testing': ['pytest'],
        },
    description = "A tool for splitting and combining files in the Fountain screenplay format.",
    long_description = long_descr,
    author = "Michael Russo",
    author_email = "mjrusso@gmail.com",
    url = "http://github.com/mjrusso/mountain",
    )
