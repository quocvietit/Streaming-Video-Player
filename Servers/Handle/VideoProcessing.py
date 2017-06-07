import threading as th
import numpy as np
import cv2

class Video_Processing:
    def __init__(self, src):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.endeco_params = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

        self.frame = None
        self.stopped = False

    def start(self):
        self.thread = th.Thread(target=self.update, args=())
        return self.thread.start()

    def update(self):
        ret, frame = self.stream.read()

        while not ret:
            if self.stopped:
                break
            ret, frame = self.stream.read()

        while True:
            if self.stopped:
                self.stream.release()
            self.grabbed, self.frame = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

    def stringData(self):
        self.result, self.img_encode = cv2.imencode('.jpg', self.frame, self.endeco_params)
        self.data = np.array(self.img_encode)
        return self.data.tostring()



