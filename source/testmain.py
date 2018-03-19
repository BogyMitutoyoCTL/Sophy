#!/usr/bin/env python

import unittest
from datetime import datetime
import time
from TimeDifference import TimeDifference


class TestTimeDifference(unittest.TestCase):

    def test_tbd(self):
        td = TimeDifference()
        dt1 = datetime.now()
        time.sleep(5)
        dt2 = datetime.now()
        td.calculate(dt1, dt2)
        self.assertEqual(True, True)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
