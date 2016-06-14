
"""
Utility and API for accessing representative PacBio data files for testing.
Run 'pbdata show [--verbose]' to display a list of files sorted by type.
"""

from collections import defaultdict
import pkg_resources
import argparse
import json
import re
import os.path as op
import sys

VERSION = (0,0,1)
RAW_DICTS = None
DATA_DICT = None


def _load_data():
    global DATA_DICT
    global RAW_DICTS
    if DATA_DICT is None:
        RAW_DICTS = json.loads(pkg_resources.resource_string("pbtestdata",
                                                             "data/files.json"))
        DATA_DICT = {f["id"]:f for f in RAW_DICTS}
    return DATA_DICT


def get_file(id_):
    d = _load_data()
    try:
        return pkg_resources.resource_filename("pbtestdata",
            op.join("data", d[id_]['path']))
    except KeyError:
        raise KeyError("No data file with ID '{i}' exists".format(i=id_))


def validate():
    global RAW_DICTS
    d = _load_data()
    have_keys = set()
    have_files = set()
    for f in RAW_DICTS:
        file_path = pkg_resources.resource_filename("pbtestdata",
            op.join("data", f['path']))
        if f['id'] in have_keys:
            raise KeyError("ID '{i}' occurs more than once".format(i=f['id']))
        elif re.search("[^0-9A-Za-z_-]{1,}", f['id']):
            raise ValueError("ID '{i}' contains non-alphanumeric characters".format(i=f['id']))
        elif f['path'] in have_files:
            raise ValueError("Path '{p}' occurs more than once".format(
                             p=f['path']))
        elif not op.exists(file_path):
            raise OSError("The path {p} does not exist".format(p=f['path']))
        elif not "description" in f or not "filetype" in f:
            raise ValueError(
                "File {i} is missing description or filetype".format(i=f['id']))
        have_keys.add(f['id'])
        have_files.add(f['path'])
    return 0


def show_all(verbose=False):
    global RAW_DICTS
    d = _load_data()
    by_type = defaultdict(list)
    for f in RAW_DICTS:
        by_type[f['filetype']].append(f)
    filetypes = sorted(by_type.keys())
    def _show_files_by_type(file_type):
        file_ids = sorted([f['id'] for f in by_type[file_type]])
        if not verbose:
            print "{t}:".format(t=file_type)
            print "  {i}".format(i=", ".join(file_ids))
        else:
            print "{t}:".format(t=file_type)
            for file_id in file_ids:
                print "  {i} - {d}".format(i=file_id,
                                           d=d[file_id]['description'])
                print "    data/{p}".format(p=d[file_id]['path'])
    # DataSet XML first
    for file_type in sorted(by_type.keys()):
        if file_type.startswith("PacBio.DataSet"):
            _show_files_by_type(file_type)
    # other files
    for file_type in sorted(by_type.keys()):
        if not file_type.startswith("PacBio.DataSet"):
            _show_files_by_type(file_type)
    return 0


def main(argv=sys.argv):
    p = argparse.ArgumentParser(description=__doc__, version=VERSION)
    sp = p.add_subparsers(dest="command")
    p1 = sp.add_parser("show")
    p1.add_argument("--verbose", action="store_true")
    p2 = sp.add_parser("get")
    p2.add_argument("file_id")
    p3 = sp.add_parser("validate")
    args = p.parse_args(argv[1:])
    if args.command == "show":
        return show_all(args.verbose)
    elif args.command == "validate":
        return validate()
    elif args.command == "get":
        print get_file(args.file_id)
        return 0
    else:
        raise ValueError("Unrecognized command '{c}'".format(c=args.command))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
