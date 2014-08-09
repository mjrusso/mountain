# -*- coding: utf-8 -*-

from mountain.mountain import foo

class TestMountainFoo(object):

    def test_simple(self):
        assert foo(1,2) == 5
