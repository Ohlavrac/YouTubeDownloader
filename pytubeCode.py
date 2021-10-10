from PIL.Image import new
from pytube import YouTube
import os


def CodePyTube(self, Link, Folder):
    self.link = Link
    self.folder = Folder

    try:
        yt=YouTube(f"{self.link}")
        myfile = yt.streams.filter(only_audio=True).first().download(r"{}".format(self.folder))

        base, ext = os.path.splitext(myfile)
        new_file = base + ".mp3"
        os.rename(myfile, new_file)
    except Exception:
        print(Exception)
        return False
