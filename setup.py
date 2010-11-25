from setuptools import setup, find_packages
setup(
    name = "qucs",
    version = "1.0",
    packages = ['qucs'], 

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        'qucs': ['demo/*.*'],
    },

    # metadata for upload to PyPI
    author = "Andrea Zonca",
    author_email = "code@andreazonca.com",
    description = "Python package for automating QUCS simulations",
    license = "GPL3",
    keywords = "QUCS",
    url = "http://andreazonca.com/software/python-qucs/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
