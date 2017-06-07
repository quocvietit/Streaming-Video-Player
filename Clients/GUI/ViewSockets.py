import cv2
import socket
import numpy as np
from PIL import Image, ImageTk

class ViewSocket:
    def __init__(self, panel):
        self.panel = panel
        self.con = socket.socket()
        self.connect_Socket()

    def connect_Socket(self):
        IP = 'localhost'
        PORT = 5555

        try:
            self.con.connect((IP, PORT))
            print self.con.getsockname()

            while True:
                lenght = self.recvall(self.con, 16)
                if lenght == None:
                    break

                buf = self.recvall(self.con, int(lenght))
                data = np.fromstring(buf, dtype='uint8')
                decimg = cv2.imdecode(data, 1)

                cv2image = cv2.cvtColor(decimg, cv2.COLOR_BGR2RGBA)
                current_image = Image.fromarray(cv2image)
                current_image = current_image.resize([1000, 610], Image.ANTIALIAS)
                imgtk = ImageTk.PhotoImage(image=current_image)

                self.panel.imgtk = imgtk
                self.panel.config(image=imgtk)
                self.panel.update()

                if (cv2.waitKey(30) & 0xFF == ord('q')):
                    self.con.send('Quit')
                    break
                else:
                    self.con.send('OK')

            cv2.release()
            self.con.close()
            cv2.destroyAllWindows()
        except:
            pass

    def recvall(self, connec, count):
        buf = b''
        while count:
            newbuf = connec.recv(count)
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf