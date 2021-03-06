from setuptools import setup, find_packages

VERSION = '1.1.76'
DESCRIPTION = 'A wrapper allowing users to get specific state-based COVID statistics from the Covid Act Now database.'

def get_read_me():
    with open('README.md', 'r') as f:
        return f.read()

# Setting up
setup(
    name="covidactnow",
    version=VERSION,
    author="Prerit Das",
    author_email="<preritdas@gmail.com>",
    description=DESCRIPTION,
    long_description = get_read_me(),
    long_description_content_type = "text/markdown",
    packages=find_packages(),
    install_requires=['requests==2.27.1'],
    keywords=['python', 'covid', 'rest', 'information', 'wrapper'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)