from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="file_publisher",
    version="0.1.0",
    author="Taiseem Dadwal",
    author_email="taiseem.dadwal@gmail.com",
    description="A backend library for publishing files to a database with metadata.",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=1.4.0",
    ],
    extras_require={
        "test":["pytest"]
    },
    python_requires=">=3.7",
)
