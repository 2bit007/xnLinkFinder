#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="xnLinkFinder",
    packages=find_packages(),
    version=__import__('xnLinkFinder').__version__,
    description="A python script to find endpoints from a URL, a file of URLs, a directory of files, a Burp XML file or a ZAP ASCII message file. It also gets potential parameters and a target specific wordlist.",
    long_description=open("README.md").read(),
    author="2bit007",
    url="https://github.com/2bit007/xnlLinkFinder",
    py_modules=["xnLinkFinder"],
    install_requires=["argparse","requests","psutil","pyyaml","termcolor","urlparse3","beautifulsoup4","lxml","html5lib","urllib3"],
    entry_points={
    'console_scripts': [
        'xnLinkFinder = xnLinkFinder.xnLinkFinder:main',
)
