import threading as th

from Servers.Handle.VideoProcessing import Video_Processing

class Video_File():
    def __init__(self):
        self.videoFile = Video_Processing("demo.mp4")

    def start(self):
        self.thread = th.Thread(target=self.update, args=()).start()
        return self.thread

    def update(self):
        self.videoFile.start()

    def stop(self):
        pass

    def stringData(self):
        return self.videoFile.stringData()
