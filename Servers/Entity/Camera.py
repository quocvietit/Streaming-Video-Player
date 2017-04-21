import threading as th

from Servers.Handle import Video_Processing


class Camera:
    def __init__(self):
        self.camera = Video_Processing(0)

    def start(self):
        th.Thread(target=self.update, args=()).start()
        return self

    def update(self):
        self.camera.start()


