#!/bin/bash -ex
# very minimal script to test this module in Bamboo

mkdir -p tmp
/opt/python-2.7.9/bin/python /mnt/software/v/virtualenv/13.0.1/virtualenv.py tmp/venv
source tmp/venv/bin/activate
alias pbvalidate='/pbi/dept/secondary/builds/links/current_develop_smrttools-incremental_installdir/smrtcmds/bin/pbvalidate'
make test
make install
pbdata show
pbdata path
pbdata get subreads-sequel
