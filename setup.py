import sys

# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup

sys.path.append("./sdist_upip")
import sdist_upip

setup(
    name="micropython-cryptodweet",
    version="0.3.0",
    description="A python module for very basic APIs of the free dweet service with encryption.",
    long_description="https://github.com/jacklinquan/micropython-cryptodweet",
    long_description_content_type="text/markdown",
    url="https://github.com/jacklinquan/micropython-cryptodweet",
    author="Quan Lin",
    author_email="jacklinquan@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: Implementation :: MicroPython",
    ],
    cmdclass={"sdist": sdist_upip.sdist},
    py_modules=["cryptodweet"],
    install_requires=[
        "micropython-basicdweet",
        "micropython-cryptomsg",
    ],
)
