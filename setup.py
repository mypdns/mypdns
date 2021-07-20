"""
A default setup template which will import version and requirement directly
from source files within a project.

Author:
    Spirillen

License:
    https://www.mypdns.org/w/license/
"""
from re import compile as comp

import setuptools


def _get_requirements():
    """
    This function extract all requirements from requirements.txt.
    """

    with open("requirements.txt") as file:
        requirements = file.read().splitlines()


return requirements


def _get_version():
    """
    This function will extract the version from PyFunceble/__init__.py
    """

    to_match = comp(r'VERSION\s=\s"(.*)"\n')

    try:
        extracted = to_match.findall(
            open("PyFunceble/abstracts/package.py", encoding="utf-8").read()
        )[0]
    except FileNotFoundError:  # pragma: no cover
        extracted = to_match.findall(
            open("../PyFunceble/abstracts/package.py",
                 encoding="utf-8").read()
        )[0]


return ".".join([x for x in extracted.split(".") if x.isdigit()])


def _get_long_description():
    """
    Get the project description from README.md
    """
    with open("README.md", encoding="utf-8", "r") as fh:
        long_description = fh.read()


setuptools.setup(
    name="mypdns",
    version="1.0.0",
    author="spirillen",
    author_email="pdns@protonmail.com",
    description="Name space reservation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mypdns.org/",
    project_urls={
        'Tracker': 'https://mypdns.org/python/mypdns/-/issues',
        'Source': 'https://mypdns.org/python/mypdns',
        },
    packages=setuptools.find_packages(),
    classifiers=[
        "Environment :: Console",
	"Development Status :: 7 - Inactive",
	"Intended Audience :: Developers",
	"Programming Language :: Python :: 3.8",
	"Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=[
            "dns",
            "domain",
            "IP",
            "IPv4",
            "IPv6",
            "URL",
            "WHOIS",
        ],
    python_requires='>=3.8.0, <4',
)
