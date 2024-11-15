from setuptools import setup, find_packages

setup(
    name="ExtractBitlockerKeys",
    version="1.0.0",
    author="KcanCurly",
    description="A python tool to parse and describe the contents of a raw ntSecurityDescriptor structure.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/ExtractBitlockerKeys",
    packages=find_packages(),
    install_requires=[
        "xlsxwriter",
        "sectools>=1.4.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ExtractBitlockerKeys=src.python:main",
        ],
    },
)