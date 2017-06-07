import threading as th

from Servers.Handle.VideoProcessing import Video_Processing

class Camera:
    def __init__(self):
        self.camera = Video_Processing(0)

    def start(self):
        self.thread = th.Thread(target=self.update, args=()).start()
        return self.thread

    def update(self):
        self.camera.start()

    def stop(self):
        pass

    def stringData(self):
        return self.camera.stringData()



