# -*- coding: utf-8 -*-

import os

from mountain.join import expand_manifest


EXPECTED_EXPANDED_MANIFEST = """
# 1

[[#include one]]

## 1.1

[[#include one-one]]

# 2

[[#include two.fountain]]

## 2.1

[[ #include part ii/one-a.markdown ]]

[[    #include part ii/one-b.mdown]]

[[#include part ii/one-c.md        ]]

[[ #include part ii/one-d.md     ]]

## 2.2

[[#include part ii/two.txt]]

## 2.3

[[#include part ii/subpart iii/a]]

### 2.3.1

[[#include part ii/subpart iii/1]]

### 2.3.2

[[#include part ii/subpart iii/2]]

### 2.3.3

[[#include part ii/subpart iii/3]]

### 2.3.4

[[#include part ii/subpart iii/4]]

## 2.4

[[#include part ii/four.txt]]

# 3

[[#include three]]

## 3.1

[[#include this-file-does-not-exist]]

## 3.2

[[#include three-two-a]]

[[#include three-two-b]]

[[#include three-two-c]]

[[#include three-two-d]]

[[#include three-two-e]]
"""

class TestExpandManifest(object):

    def test_expand_manifest(self):

        actual = expand_manifest(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "fixture",
                "manifest.fountain"))

        assert actual == EXPECTED_EXPANDED_MANIFEST
