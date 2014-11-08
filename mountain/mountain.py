# -*- coding: utf-8 -*-

__version__ = "0.3.0"


import sys

from .join import expand_manifest
from .split import split_combined_document
from .utils import write_files


def join(manifest_path, combined_document_path):
    write_files(expand_manifest(manifest_path, combined_document_path))
    print(u"\u2713 Join complete. Expanded manifest into single combined document.")

def split(manifest_path, combined_document_path):
    write_files(split_combined_document(manifest_path, combined_document_path))
    print(u"\u2713 Split complete. Updated manifest and wrote all referenced files.")

def help():
    version()
    print("""
Usage:

    $ mountain join <manifest-path> <combined-document-path>

Combine all files referenced from <manifest-path> into the document at
<combined-document-path>. The file at <combined-document-path> will be
overwritten if it already exists.

The files referenced from <manifest-path> must be referenced with the
[[include: file-path]] directive.

    $ mountain split <manifest-path> <combined-document-path>

Write all included files from <combined-document-path> into standalone files.
Produce an updated manifest file and write to <manifest-path>. In all cases,
files will be overwritten if they already exist.

All included files in <combined-document-path> must be indicated with the
[[reference: file-path]] ... [[/reference]] directive.

    $ mountain --version

Print version number and exit.

    $ mountain --help

Print this help text and exit.

Note:

For more details, see https://github.com/mjrusso/mountain.

""")

def version():
    print("Mountain v%s." % __version__)

def main():
    args = sys.argv[1:]

    if sys.version_info[0] == 2 and sys.version_info[1] < 7:
        raise Exception("Python >= 2.7 required. Aborting.")

    if not len(args):
        help()
    elif args[0] == "join":
        join(args[1], args[2])
    elif args[0] == "split":
        split(args[1], args[2])
    elif args[0] in ("--version", "version"):
        version()
    elif args[0] in ("--help", "help"):
        help()
    else:
        print("Invalid option specified.")
        help()
