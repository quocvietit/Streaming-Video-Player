import os
import sys
import ttk
import vlc
import time
import platform
import tkFileDialog
import pathlib as pl
import Tkinter as tk
import tkMessageBox

from Clients.GUI.TimesRun import TimeRun
from Clients.GUI.ViewSockets import ViewSocket

PROGRAM_NAME = "Streaming Video Player"


class ViewPlay():
    def __init__(self, root):
        self.root = root
        self.create_Gui()

    def create_Gui(self):
        self.root.title(PROGRAM_NAME)
        self.root.geometry("1000x700")
        self.create_MenuBar()
        self.create_Frame()
        self.create_Button()

        self.create_Item()
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.timer = TimeRun(self.OnTimer, 1.0)
        self.timer.start()
        self.root.update()

    def create_MenuBar(self):
        self.menuBar = tk.Menu(self.root)

        self.Media = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Media', menu=self.Media)
        self.Media.add_command(label="Open File  Ctrl+O", command=self.open_File)
        self.Media.add_command(label="Connect Server", command=self.connect_Server)
        self.Media.add_command(label="Properties", command=self.err)
        self.Media.add_command(label="Exit", command=self.exit)

        self.playMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Play', menu=self.playMenu)
        self.playMenu.add_command(label='Pause', command=self.play)
        self.playMenu.add_command(label='Pause', command=self.pause)
        self.playMenu.add_command(label='Stop', command=self.stop)

        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Help', menu=self.helpMenu)
        self.helpMenu.add_command(label="Help", command=self.help)
        self.helpMenu.add_command(label="More Information...", command=self.information)
        self.helpMenu.add_command(label="About", command=self.exit)

        self.root.config(menu=self.menuBar)

    def create_Frame(self):
        self.player = None
        self.videopanel = tk.LabelFrame(self.root, bg="#333")
        self.videopanel.pack(fill=tk.BOTH, expand=1)

    def create_Button(self):
        ctrlpanel = ttk.Frame(self.root)
        self.btnPlay = ttk.Button(ctrlpanel, text="Play", command=self.play)
        self.btnPlay.pack(side=tk.LEFT, padx=5)

        self.btnPause = ttk.Button(ctrlpanel, text="Pause", command=self.pause)
        self.btnPause.pack(side=tk.LEFT, padx=5)

        self.btnStop = ttk.Button(ctrlpanel, text="Stop", command=self.stop)
        self.btnStop.pack(side=tk.LEFT, padx=5)

        self.volume_var = tk.IntVar()
        self.volslider = tk.Scale(ctrlpanel, variable=self.volume_var, command=self.volume_sel,
                                  from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        self.volslider.pack(side=tk.LEFT)

        ctrlpanel.pack(side=tk.BOTTOM)

    def create_Item(self):
        ctrlpanel = ttk.Frame(self.root)
        self.scale_var = tk.DoubleVar()
        self.timeslider_last_val = ""
        self.timeslider = tk.Scale(ctrlpanel, variable=self.scale_var, command=self.scale_sel,
                                   from_=0, to=1000, orient=tk.HORIZONTAL, length=500)
        self.timeslider.pack(side=tk.BOTTOM, fill=tk.X, expand=1)
        self.timeslider_last_update = time.time()
        ctrlpanel.pack(side=tk.TOP, fill=tk.X)

    def open_File(self):
        self.stop()

        p = pl.Path(os.path.expanduser("~"))
        fullname = tkFileDialog.askopenfilename(title="Please select a video file: ",
                                                filetypes=[('AVI Files', '.avi'),
                                                           ('MP4 Files', '.mp4'),
                                                           ('MKV Files', '.mkv'),
                                                           ('All Files', '.*')],
                                                initialdir=p)
        if os.path.isfile(fullname):
            dirname = os.path.dirname(fullname)
            filename = os.path.basename(fullname)

            self.Media = self.Instance.media_new(str(os.path.join(dirname, filename)))
            self.player.set_media(self.Media)

            if platform.system() == 'Windows':
                self.player.set_hwnd(self.GetHandle())
            else:
                self.player.set_xwindow(self.GetHandle())

            self.play()

    def GetHandle(self):
        return self.videopanel.winfo_id()

    def play(self):
        if not self.player.get_media():
            self.open_File()
        else:
            if self.player.play() == -1:
                pass

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
        self.timeslider.set(0)

    def OnTimer(self):
        if self.player == None:
            return
        length = self.player.get_length()
        dbl = length * 0.001
        self.timeslider.config(to=dbl)

        tyme = self.player.get_time()
        if tyme == -1:
            tyme = 0
        dbl = tyme * 0.001
        self.timeslider_last_val = ("%.0f" % dbl) + ".0"
        if time.time() > (self.timeslider_last_update + 2.0):
            self.timeslider.set(dbl)

    def scale_sel(self, evt):
        if self.player == None:
            return
        nval = self.scale_var.get()
        sval = str(nval)
        if self.timeslider_last_val != sval:
            self.timeslider_last_update = time.time()
            mval = "%.0f" % (nval * 1000)
            self.player.set_time(int(mval))

    def volume_sel(self, evt):
        if self.player == None:
            return
        volume = self.volume_var.get()
        if volume > 100:
            volume = 100
        if self.player.audio_set_volume(volume) == -1:
            pass

    def connect_Server(self):
        panel = tk.Label(self.videopanel)
        panel.pack(fill=tk.BOTH, expand=1)
        ViewSocket(panel)

    def properties(self):
        pass

    def help(self):
        pass

    def information(self):
        pass

    def about(self):
        pass

    def exit(self):
        sys.exit(0)

    def err(self):
        print "Chuc nang chua hoan thien"
        pass
