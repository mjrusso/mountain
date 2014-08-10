# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import codecs
import sys

from .join import expand_manifest


def foo(a, b):
    return a + b + 2


def join(manifest_path, output_path):
    print("Reading manifest from `%s`." % manifest_path)
    with codecs.open(output_path, "w", "utf-8") as f:
        manifest = expand_manifest(manifest_path)
        f.write(manifest)
    print("Wrote expanded manifest to `%s`." % output_path)

def split(manifest_path, output_path):
    pass

def help():
    version()

def version():
    print("Mountain v%s." % __version__)

def main():
    args = sys.argv[1:]

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
