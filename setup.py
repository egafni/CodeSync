#from distutils.core import setup
from setuptools import find_packages, setup

setup(
    # Metadata
    name="codesync",
    version="0.1",
    description="code synchronizer",
    url="",
    author="Erik Gafni",
    author_email="egafni@gmail.com",
    maintainer="Erik Gafni",
    maintainer_email="egafni@gmail.com",
    license="GPLv2",
    install_requires=["watchdog", ],
    scripts=["bin/csync"],
    data_files=[('etc', ['etc/example_excludes'])],
    # Packaging Instructions
    packages=find_packages(),
    include_package_data=True
)


