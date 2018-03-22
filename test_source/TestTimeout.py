from time import sleep
import threading


class TimeoutTest:
    def __init__(self, timeout: float):
        self.timeout = timeout
        self.timer = threading.Timer(timeout, self.__on_timeout)
        self.timer.start()

    def __on_timeout(self):
        print("Oops, I timed out")
        print("My timeout was {} seconds.".format(self.timeout))

    def stop(self):
        self.timer.cancel()


def progress_sleep(duration: int):
    for i in range(0, duration):
        print(".")
        sleep(1)


if __name__ == "__main__":
    t1 = TimeoutTest(timeout=2.1)
    t1.stop()
    progress_sleep(4)
    print("Nothing happened")
    t2 = TimeoutTest(timeout=2.1)
    progress_sleep(4)
    t2.stop()
