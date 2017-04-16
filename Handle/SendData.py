import threading as th

class Send_Data:
    def __init__(self, connec, camera):
        self.connec = connec
        self.camera = camera
        self.stopped = False

    def start(self):
        th.Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                break
            data = self.camera.stringData()
            self.connec.send(str(len(data)).ljust(16))
            self.connec.send(data)

            reply = self.connec.recv(1024)
            if reply =='Quit':
                self.stop()

        self.connec.close()

    def stop(self):
        self.stopped = False