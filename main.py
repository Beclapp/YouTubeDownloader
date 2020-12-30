# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pytube import YouTube
import tkinter as tk


def download(link):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download()
    print("Download completed")


window = tk.Tk()
label = tk.Label(
    text="input link to download")
entry = tk.Entry()
button = tk.Button(
    text="Download",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=lambda : download(entry.get())
)
label.pack()
entry.pack()
button.pack()
window.mainloop()

