# -*- coding: utf-8 -*-

import os

from mountain.join import expand_manifest


class TestExpandManifest(object):

    def test_expand_manifest(self):

        actual = expand_manifest(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "join",
                "manifest.fountain"))

        expected = open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixtures",
                "join",
                "screenplay.fountain")).read()

        assert actual == expected
