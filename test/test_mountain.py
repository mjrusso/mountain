# -*- coding: utf-8 -*-

import codecs
import os

from mountain.join import expand_manifest
from mountain.split import split_combined_document


class TestExpandManifest(object):

    def test_expand_manifest_simple(self):

        actual = expand_manifest(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "example",
                "manifest.fountain"),
            "test-path")

        expected_contents = codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "example",
                "screenplay.fountain"),
            "r",
            "utf-8"
        ).read()

        expected = [{"path": "test-path", "contents": expected_contents}]

        assert actual == expected

    def test_expand_manifest_complex(self):

        actual = expand_manifest(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "join",
                "manifest.fountain"),
            "test-path")

        expected_contents = codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "join",
                "screenplay.fountain"),
            "r",
            "utf-8"
        ).read()

        expected = [{"path": "test-path", "contents": expected_contents}]

        assert actual == expected


class TestSplitCombinedDocument(object):

    def test_split_combined_document(self):

        actual = split_combined_document(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "example",
                "manifest.fountain"),
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "example",
                "screenplay.fountain"))

        expected = list()

        for path in ["fixtures/example/intro.fountain",
                     "fixtures/example/inciting-incident.fountain",
                     "fixtures/example/the-end.fountain",
                     "fixtures/example/manifest.fountain"]:

            path = os.path.join(
                       os.path.dirname(os.path.realpath(__file__)),
                       path)

            expected.append(
                {"path": path,
                 "contents": codecs.open(path, "r", "utf-8").read()})

        assert actual == expected
