#!/usr/bin/env python
import unittest
from datetime import timedelta
from datetime import date
from HighScoreEntry import HighScoreEntry


class TestHighScoreEntry(unittest.TestCase):

    def test_entry(self):
        entry = HighScoreEntry("John", timedelta(seconds=3, milliseconds=450), 34.8, date(2018, 3, 2))

        self.assertEqual(entry.name, "John")
        self.assertEqual(entry.duration, timedelta(0, 3, 0, 450, 0, 0, 0))
        self.assertEqual(entry.record_date, date(2018, 3, 2))
        self.assertEqual(entry.speed, 34.8)


if __name__ == '__main__':
    unittest.main()
