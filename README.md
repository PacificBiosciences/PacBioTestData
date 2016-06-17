# PacBioTestData
Small datasets for testing

Usage
-----

This repository requires the Git Large File Support extension
(https://git-lfs.github.com/) to fetch binary data files.  To download and
install as a Python module/cmdline tool:

  $ git clone https://github.com/PacificBiosciences/PacBioTestData.git
  $ cd PacBioTestData
  $ git lfs pull
  $ make python

You can then access the `pbtestdata` Python module programatically::

  $ python
  >>> import pbtestdata
  >>> pbtestdata.get_file("subreads_bam")
  '/path/to/movie.subreads.bam'

Or use the command-line tool::

  $ pbdata --help
  usage: pbdata [-h] [-v] {show,get,validate} ...

  Utility and API for accessing representative PacBio data files for testing.
  Run 'pbdata show [--verbose]' to display a list of files sorted by type.

  positional arguments:
    {show,get,validate}

  optional arguments:
    -h, --help           show this help message and exit
    -v, --version        show program's version number and exit
  $ pbtestdata get subreads-bam
  /path/to/movie.subreads.bam
