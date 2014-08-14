# -*- coding: utf-8 -*-

import codecs
import os

from mountain.join import expand_manifest
from mountain.split import split_combined_document


class TestExpandManifest(object):

    def test_expand_manifest_simple(self):

        combined_document_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "fixtures",
            "simple",
            "screenplay.fountain")

        actual = expand_manifest(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "simple",
                "manifest.fountain"),
            combined_document_path)

        expected_contents = codecs.open(
            combined_document_path,
            "r",
            "utf-8"
        ).read()

        expected = [{"path": combined_document_path, "contents": expected_contents}]

        assert actual == expected

    def test_expand_manifest_complex(self):

        combined_document_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "fixtures",
            "complex",
            "screenplay.fountain")

        actual = expand_manifest(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "complex",
                "manifest.fountain"),
            combined_document_path)

        expected_contents = codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "complex",
                "screenplay.fountain"),
            "r",
            "utf-8"
        ).read()

        expected = [{"path": combined_document_path, "contents": expected_contents}]

        assert actual == expected


class TestSplitCombinedDocument(object):

    def test_split_combined_document(self):

        actual = split_combined_document(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "simple",
                "manifest.fountain"),
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "simple",
                "screenplay.fountain"))

        expected = list()

        for path in ["fixtures/simple/intro.fountain",
                     "fixtures/simple/inciting-incident.fountain",
                     "fixtures/simple/the-end.fountain",
                     "fixtures/simple/manifest.fountain"]:

            path = os.path.join(
                       os.path.dirname(os.path.realpath(__file__)),
                       path)

            expected.append(
                {"path": path,
                 "contents": codecs.open(path, "r", "utf-8").read()})

        assert actual == expected
