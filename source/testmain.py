#!/usr/bin/env python

from datetime import datetime
import time
from TimeDifference import TimeDifference

if __name__ == "__main__":
    td = TimeDifference()
    dt1 = datetime.now()
    time.sleep(0.004)
    dt2 = datetime.now()
    td.calculate(dt1, dt2)

