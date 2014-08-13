# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import codecs
import sys

from .join import expand_manifest
from .split import split_combined_document


def join(manifest_path, output_path):
    print("Reading manifest from `%s`." % manifest_path)
    with codecs.open(output_path, "w", "utf-8") as f:
        manifest = expand_manifest(manifest_path)
        f.write(manifest)
    print("Wrote expanded manifest to `%s`." % output_path)

def split(manifest_path, combined_document_path):
    print("Reading manifest from `%s`." % manifest_path)
    print("Reading combined document from `%s`." % combined_document_path)
    split_combined_document(manifest_path, combined_document_path)
    print("Updated manifest and all referenced files.")

def help():
    version()

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
    elif args[0] == "--version":
        version()
    elif args[0] == "--help":
        help()
    else:
        print("Invalid option specified.")
        help()
