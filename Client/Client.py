import numpy as np
import socket as sk
import cv2

IP = 'localhost'
PORT = 5555

def recvall(connec, count):
    buf = b''
    while count:
        newbuf = connec.recv(count)
        if not newbuf:
            return None
        buf+=newbuf
        count-=len(newbuf)
    return buf

try:
    socket = sk.socket()
    socket.connect((IP, PORT))
    print socket.getsockname()

    while True:
        lenght = recvall(socket, 16)
        if lenght == None:
            break

        buf = recvall(socket, int(lenght))
        data = np.fromstring(buf, dtype='uint8')

        decimg = cv2.imdecode(data, 1)
        cv2.imshow('Client', decimg)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            socket.send('Quit')
            break
        else:
            socket.send('OK')

    socket.close()
    cv2.destroyAllWindows()

except:
    pass



