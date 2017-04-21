from Tkinter import *
import cv2
import pyglet
import tkFileDialog

PROGRAM_NAME = "Streaming Video Player"

class View:
    def __init__(self, root):
        self.root = root
        self.player = pyglet.media.Player()
        # self.model = model
        # self.player = player
        self.create_Gui()

    def create_Gui(self):
        self.root.title(PROGRAM_NAME)
        self.root.geometry("1000x600")

        self.create_MenuBar() #create MenuBar
        self.create_Frame() #create Frame video


        # self.create_Top_Display()
        # self.create_Button_Frame()
        # self.create_List_Box()
        # self.create_Bottom_Frame()
        # self.c

    def create_MenuBar(self):
        #set parent
        self.menuBar = Menu(self.root)

        # File
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)

        self.fileMenu.add_command(label="Open File  Ctrl+O", command=self.open_File)
        self.fileMenu.add_command(label="Properties", command=self.open_File)
        self.fileMenu.add_command(label="Exit", command=self.open_File)

        # Play
        self.playMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Play', menu=self.playMenu)

        self.playMenu.add_command(label='Play/Pause', command=self.open_File)
        self.playMenu.add_command(label='Stop', command=self.open_File)

        #Help
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Help', menu=self.helpMenu)

        self.helpMenu.add_command(label="Help", command=self.open_File)
        self.helpMenu.add_command(label="More Information...", command=self.open_File)
        self.helpMenu.add_command(label="About", command=self.open_File)

        #add Menu
        self.root.config(menu=self.menuBar)

    def create_Frame(self):
        #set parent
        self.frame = Frame(self.root)

        self.lblFrame = LabelFrame(root, bg = "#333")
        self.lblFrame.pack(fill="both", expand = "yes", padx=0, pady=0)

        #add button
        self.create_Button()

        self.frame.pack()

    def create_Button(self):
        #Button Play
        self.btnPlay = Button(self.frame, text="Play", command =self.play)
        self.btnPlay.pack(side=LEFT, padx=5)

        #Button Pause
        self.btnPause = Button(self.frame, text="Pause", command=self.play)
        self.btnPause.pack(side=LEFT, padx=5)

        #Button Stop
        self.btnStop = Button(self.frame, text="Stop", command=self.play)
        self.btnStop.pack(side=LEFT, padx=5)

    def play(self):
        self.plays = pyglet.media.Player()
        self.source = pyglet.media.load('demo.mp4')
        self.plays.queue(self.source)
        self.plays.play()



    def start(self):
        pass

    def open_File(self):
        self.fileDir = tkFileDialog.askopenfile()
        if (self.fileDir):
            self.file = self.fileDir
            self.root.destroy()
            return self.file
        else:
            self.root.destroy()
            return None


root = Tk()
View(root)
root.mainloop()
