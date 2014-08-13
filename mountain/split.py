# -*- coding: utf-8 -*-

import codecs
import os
import re


def write_file(path, contents):
    with codecs.open(path, "w", "utf-8") as f:
        f.write(contents)
        print("Wrote `%s`." % path)

def split_combined_document(manifest_path, combined_document_path):

    with codecs.open(combined_document_path, "r", "utf-8") as f:
        combined_document = f.read()

    base_path = os.path.dirname(os.path.abspath(manifest_path))

    references = re.findall(
        "\[\[#reference\s+(.*?)\]\](.*?)\[\[#reference-end\]\]",
        combined_document,
        re.DOTALL)

    manifest = combined_document

    for file_name, file_contents in references:
        file_name = file_name.strip()
        file_path = os.path.join(base_path, file_name)
        file_contents = file_contents.strip()

        # Add the trailing newline that was just stripped away.
        file_contents = file_contents + "\n"

        write_file(file_path, file_contents)

        manifest = re.sub(
            "\[\[#reference\s+%s\]\].*?\[\[#reference-end\]\]" % re.escape(file_name),
            "[[#include %s]]" % file_name,
            manifest,
            0,
            re.DOTALL
        )

    write_file(manifest_path, manifest)

    return manifest
