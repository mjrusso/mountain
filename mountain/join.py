# -*- coding: utf-8 -*-

import codecs
import os
import re


# The extensions that we will automatically try in the event that the user
# does not supply an extension when referencing a file in an `#include`
# directive.
KNOWN_EXTENSIONS = (
    ".fountain",
    ".txt",
    ".md",
    ".mdown",
    ".markdown",
)


def expand_manifest(manifest_path):

    with codecs.open(manifest_path, "r", "utf-8") as f:
        manifest = f.read()

    base_path = os.path.dirname(os.path.abspath(manifest_path))

    referenced_file_names = (re.compile("\[\[\s*#include\s+(.*)\s*\]\]")
                               .findall(manifest))

    for file_name in referenced_file_names:

        file_name = file_name.strip()

        for extension in ("",) + KNOWN_EXTENSIONS:

            file_path = os.path.join(base_path, file_name + extension)

            if os.path.exists(file_path):

                with codecs.open(file_path, "r", "utf-8") as f:
                    referenced_file = f.read()

                manifest = re.sub(
                    "\[\[\s*#include\s+%s\s*\]\]" % file_name,
                    "".join([
                        "[[#reference %s]]" % file_name,
                        "\n" if referenced_file.startswith("\n") else "\n\n",
                        referenced_file,
                        "\n" if referenced_file.endswith("\n") else "\n\n",
                        "[[#reference-end]]"
                    ]),
                    manifest)

                break

    return manifest
