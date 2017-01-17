# PacBioTestData
Small datasets for testing

Usage
-----

This repository provides a selection of small-ish representative files
produced by PacBio systems and software, suitable for running simple tests.
To download and install as a Python module/cmdline tool:

```
  $ git clone https://github.com/PacificBiosciences/PacBioTestData.git
  $ cd PacBioTestData
  $ make install
```

You can then access the `pbtestdata` Python module programatically:

```
  $ python
  >>> import pbtestdata
  >>> pbtestdata.get_file("subreads_bam")
  '/path/to/movie.subreads.bam'
```

Or use the command-line tool:

```
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
```

Other codebases may implement their own accessors by reading `files.json`,
which can be captured in an environment variable:

```
  export PB_TEST_DATA_FILES="`pbdata path`"
```

Adding data
-----------

This repo should only be used for relatively compact (< 100KB), commonly used
files in officially supported formats.  When adding files, please follow these
guidelines:

  - Any file that needs to be accessed directly should have an entry in
    `data/files.json`.  This should *not* include index files; however in some
    cases both the DataSet XML and the underlying BAM or FASTA files may be
    retrievable.
  - Accessor IDs should be simple and hyphen-separated; see `data/files.json`
    for examples.
  - All BAM, FASTA, and DataSet XML files should be compliant with the PacBio
    file format specifications; use `pbvalidate` to check compliance.
  - PacBio DataSet XML should always be generated with relative paths.
  - The dataset name should match the accessor ID in `files.json`.
  - BAM files should always have an accompanying PacBio index (.pbi file).
  - BAM indices created by samtools (.bai files) are optional.
  - FASTA files should always have an accompanying .fai index (from samtools).
