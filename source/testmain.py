#!/usr/bin/env python

import unittest
from datetime import datetime
import time
from TimeDifference import TimeDifference


class TestTimeDifference(unittest.TestCase):

    def test_timedifference_in_microseconds1(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 19, 11, 0, 0, 100)
        timediff = td.calculate(dt1, dt2)
        self.assertEqual(timediff.microseconds, 100)

    def test_timedifference_in_microseconds2(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 19, 11, 0, 0, 0)
        timediff = td.calculate(dt1, dt2)
        self.assertEqual(timediff.microseconds, 0)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
