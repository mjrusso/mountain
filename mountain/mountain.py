# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import sys


def foo(a, b):
    return a + b + 2


def main():
    args = sys.argv[1:]
    print("Executing mountain version %s." % __version__)
    print("List of argument strings: %s" % args)
    print("Hi, this is Mountain!")
    print("Foo %s" % foo(1,3))
