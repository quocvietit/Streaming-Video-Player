import threading as th
from Handle import Video_Processing

class Video_File:
    def __init__(self):
        self.videoFile = Video_Processing("File name")

    def start(self):
        th.Thread(target=self.update, args=()).start()
        return self

    def update(self):
        self.videoFile.start()
