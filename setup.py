from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-celesteg",
    version="0.3",
    author="Celeste Griffin",
    author_email="celestebgriff@gmail.com",
    description="helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/celestebgriff/lambdata-celesteg",
    keywords="Lambda School",
    packages=find_packages() # ["lambdata-celesteg"]
)