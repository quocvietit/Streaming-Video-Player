import threading as th

class TimeRun(th.Thread):
    def __init__(self, callback, tick):
        th.Thread.__init__(self)
        self.callback = callback
        self.stopFlag = th.Event()
        self.tick = tick
        self.iters = 0

    def run(self):
        while not self.stopFlag.wait(self.tick):
            self.iters += 1
            self.callback()

    def stop(self):
        self.stopFlag.set()

    def get(self):
        return self.iters