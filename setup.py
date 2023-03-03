import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

VERSION = "1.0.0a1"

setup(
    # General Information
    name="SimpleStorage",
    version=VERSION,
    description="Simple Storage is an easy way to work with data in your Python script. "
                "You can save and load your data without much effort or knowledge about any storage method.\n" 
                "Moreover, it provides the possibilities to use data and variables globally in a script.\n"
                "The library does not reinvent the wheel, but enriches it with not having to deal with it.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/princessmiku/simplestorage",
    author="Miku",
    license="MIT",
    keywords=["storage", "sqlite", "json", "share", "data", "saving"],
    python_requires='>=3.11.0',
    classifiers=[
        "Programming Language :: Python :: 3.11",
    ],
    # Moduls
    packages=[
        "simplestorage",
        "simplestorage.internal_module",
        "simplestorage.json_module",
    ]

)
