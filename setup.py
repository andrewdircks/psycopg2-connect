from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="psycopg2-connect",
    version="0.0.1",
    author="Andrew Dircks",
    author_email="abd93@cornell.edu",
    description="A lightweight package for connecting to postgres servers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewdircks/psycopg2-connect",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    install_requires=['psycopg2'],
    packages=['connect'],
    python_requires=">=3.7",
)