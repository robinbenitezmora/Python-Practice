from tkinter import *
from tkinter import filedialog as tk
from tkinter import messagebox as tk2
try:
    import pygame
except ImportError:
    print("Please make sure pygame is installed.")

playlist = []

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.b1 = Button(self, text="Play", command=self.play_music)
        self.b1.grid(row=0, column=0)

        self.b2 = Button(self, text="Pause", command=self.pause_music)
        self.b2.grid(row=0, column=1)

        self.b3 = Button(self, text="Stop", command=self.stop_music)
        self.b3.grid(row=0, column=2)

        self.b4 = Button(self, text="Resume", command=self.resume_music)
        self.b4.grid(row=0, column=3)

        self.b5 = Button(self, text="Add to Playlist", command=self.add_to_playlist)
        self.b5.grid(row=0, column=4)

        self.b6 = Button(self, text="Exit", command=self.exit)
        self.b6.grid(row=0, column=5)

    def play_music(self):
        try:
            pygame.init()
            pygame.mixer.music.load(playlist[0])
            pygame.mixer.music.play()
        except:
            tk2.showinfo("Notice", "Please add a song first")

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def add_to_playlist(self):
        file = tk.askopenfilenames()
        songs = list(file)
        for s in songs:
            playlist.append(s)

    def exit(self):
        exit()

app = Application()

app.master.title("Music Player")
app.mainloop()

