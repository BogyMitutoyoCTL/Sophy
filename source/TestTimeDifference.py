#!/usr/bin/env python

import unittest
from datetime import datetime
from TimeDifference import TimeDifference

"""""
class NameInput(unittest.TestCase):

    def test_1(self):
        MyApp().run()
        self.assertEqual(True, True)
"""""


class TestTimeDifference(unittest.TestCase):

    def test_timedifference_calculate_diff_in_microseconds1(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 19, 11, 0, 0, 100)
        timediff = td.calculate(dt1, dt2)
        print(timediff.microseconds)
        self.assertEqual(timediff.microseconds, 100)

    def test_timedifference_calculate_diff_in_microseconds2(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 19, 11, 0, 0, 0)
        timediff = td.calculate(dt1, dt2)
        self.assertEqual(timediff.microseconds, 0)

    def test_timedifference_calculate_diff_in_days1(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 11, 11, 0, 0, 0)
        timediff = td.calculate(dt1, dt2)
        self.assertEqual(timediff.days, -8)

    def test_timedifference_calculate_diff_in_hours1(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 19, 14, 0, 0, 0)
        timediff = td.calculate(dt1, dt2)
        self.assertEqual(timediff.seconds, 3 * 60 * 60)

    def test_timedifference_calculate_diff_in_minutes(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 19, 11, 15, 0, 0)
        timediff = td.calculate(dt1, dt2)
        self.assertEqual(timediff.seconds, 15 * 60)

    def test_timedifference_calculate_diff_in_seconds(self):
        td = TimeDifference()
        dt1 = datetime(2018, 3, 19, 11, 0, 0, 0)
        dt2 = datetime(2018, 3, 19, 11, 0, 21, 0)
        timediff = td.calculate(dt1, dt2)
        self.assertEqual(timediff.seconds, 21)


if __name__ == '__main__':
    unittest.main()
