# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '9/17/15'

import unittest

import ironsmith


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(ironsmith.version(), '0.0.1dev')


if __name__ == '__main__':
    unittest.main()
