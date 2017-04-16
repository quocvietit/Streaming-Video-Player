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
        th.Thread(target=self.update, args=()).start()
        return self

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
        result, img_encode = cv2.imencode('.jpg', self.frame, self.endeco_params)
        data = np.array(img_encode)
        return data.tostring()



