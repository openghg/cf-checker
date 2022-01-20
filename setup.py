from setuptools import setup, find_packages
import os
import re

with open("src/cfchecker/__init__.py", "r") as f:
    version_line = f.readline()
    clean_str = re.sub(r"\s+", "", version_line, flags=re.UNICODE)
    __version__ = clean_str.split("=")[1].replace("'", "")

# Need to try/except this because pip install unpacks to a different dir and
# relative path lookup fails. Should still work where needed.
try:
    __description__ = "\n" + open(os.path.join(os.path.dirname(__file__), "README.md")).read()
except:
    __description__ = ""

setup(
    name="cfchecker",
    version=__version__,
    description="The NetCDF Climate Forecast Conventions compliance checker",
    long_description=__description__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    keywords="",
    author="Rosalyn Hatcher",
    author_email="r.s.hatcher@reading.ac.uk",
    url="http://cfconventions.org/compliance-checker.html",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    zip_safe=False,
    install_requires=["netCDF4", "numpy>=1.7", "cfunits>=3.0.0", "future"],
    entry_points={"console_scripts": ["cfchecks = cfchecker.cfchecks:main"]},
)
