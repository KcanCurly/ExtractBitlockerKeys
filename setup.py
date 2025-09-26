from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="ExtractBitlockerKeys",
    version="1.0.0",
    author="KcanCurly",
    description="A system administration or post-exploitation script to automatically extract the bitlocker recovery keys from a domain.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/ExtractBitlockerKeys",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ExtractBitlockerKeys=python.ExtractBitlockerKeys:main",
        ],
    },
)