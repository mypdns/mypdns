import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypdns",
    version="0.0.1.dev2",
    author="spirillen",
    author_email="pdns@protonmail.com",
    description="Name space reservation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.mypdns.org/",
    project_urls={
        'Tracker': 'https://www.mypdns.org/tag/matrix/',
        'Source': 'https://github.com/pypa/sampleproject/',
        },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.7',
)
