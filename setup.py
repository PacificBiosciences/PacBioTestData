
import shutil
import os.path
import json
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

VERSION = "0.2.2"
DATA = os.path.join("pbtestdata", "data")

with open(os.path.join("pbtestdata", "version.py"), "w") as version_py:
    version_py.write("VERSION = \"{v}\"".format(v=VERSION))

if sys.argv[1] == "install":
    if os.path.exists(DATA):
        print "Removing old pbtestdata/data..."
        shutil.rmtree(DATA)
    print "Copying over pbtestdata/data..."
    shutil.copytree(os.path.abspath("data"), DATA)
package_data = []
for dirname, dirnames, filenames in os.walk(DATA):
    for file_name in filenames:
        if not file_name.startswith("."):
            path_name = os.path.relpath(dirname, "pbtestdata")
            package_data.append(os.path.join(path_name, file_name))

setup(
    name="pbtestdata",
    version=VERSION,
    license="BSD",
    author="natechols",
    url="https://github.com/PacificBiosciences/PacBioTestData",
    keywords="pacbio".split(),
    packages=find_packages(),
    package_data={"pbtestdata": package_data},
    include_package_data=True,
    entry_points={"console_scripts": ["pbdata = pbtestdata.core:main"]},
    zip_safe=False)
