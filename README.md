==================
PacBio Sample Data
==================

This repository contains small, self-contained example datasets and related
files produced by PacBio instruments and software.  These are primarily
intended for developers, especially for writing unit tests, and are not
meant to be used for scientific benchmarks.  All files that
are intended to be accessed directly (i.e. not indices such as .pbi or .fai)
should be listed in data/files.json, including an alphanumerical ID,
plain-English description, and file "meta-type" string as defined in our
core libraries.


Valid file metatypes
--------------------

These are the metatype strings currently encoded in the pbcommand library.
Note that some of these, in particular PacBio.Index.\*, should probably not
be included in data/files.json.

  PacBio.AlignmentFile.AlignmentBamFile
  PacBio.AlignmentFile.ConsensusAlignmentBamFile
  PacBio.BarcodeFile.BarcodeFastaFile
  PacBio.ConsensusReadFile.ConsensusReadBamFile
  PacBio.ContigFile.ContigFastaFile
  PacBio.DataSet.AlignmentSet
  PacBio.DataSet.BarcodeSet
  PacBio.DataSet.ConsensusAlignmentSet
  PacBio.DataSet.ConsensusReadSet
  PacBio.DataSet.ContigSet
  PacBio.DataSet.HdfSubreadSet
  PacBio.DataSet.ReferenceSet
  PacBio.DataSet.SubreadSet
  PacBio.FileTypes.CHUNK
  PacBio.FileTypes.COND_RESEQ
  PacBio.FileTypes.Fasta
  PacBio.FileTypes.Fastq
  PacBio.FileTypes.GCHUNK
  PacBio.FileTypes.JsonReport
  PacBio.FileTypes.SCHUNK
  PacBio.FileTypes.alignment_cmp_h5
  PacBio.FileTypes.bam
  PacBio.FileTypes.bam_bai
  PacBio.FileTypes.bed
  PacBio.FileTypes.blasr_file
  PacBio.FileTypes.cfg
  PacBio.FileTypes.csv
  PacBio.FileTypes.generic_fofn
  PacBio.FileTypes.gff
  PacBio.FileTypes.gzip
  PacBio.FileTypes.h5
  PacBio.FileTypes.input_xml
  PacBio.FileTypes.json
  PacBio.FileTypes.log
  PacBio.FileTypes.movie_fofn
  PacBio.FileTypes.pickle
  PacBio.FileTypes.reference_info_xml
  PacBio.FileTypes.rgn_fofn
  PacBio.FileTypes.rs_movie_metadata
  PacBio.FileTypes.sam
  PacBio.FileTypes.txt
  PacBio.FileTypes.vcf
  PacBio.FileTypes.xml
  PacBio.Index.BamIndex
  PacBio.Index.FastaContigIndex
  PacBio.Index.Indexer
  PacBio.Index.PacBioIndex
  PacBio.Index.SaWriterIndex
  PacBio.Index.SamIndex
  PacBio.ReadFile.BazFile
  PacBio.ReadFile.PulseFile
  PacBio.ReadFile.TraceFile
  PacBio.ReferenceFile.ReferenceFastaFile
  PacBio.SubreadFile.BaxFile
  PacBio.SubreadFile.ChipStatsFile
  PacBio.SubreadFile.SubreadBamFile
