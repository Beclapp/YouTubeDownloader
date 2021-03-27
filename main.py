from pytube import YouTube
from tkinter import *

values = {
    "Default": "1",
    "Audio-only": "2",
}

resolution = {
    "360p": "360p",
    "720p": "720p",
}


def download(link, option, res):
    yt = YouTube(link)
    ys = None
    if option == '1':
        ys = yt.streams.filter(res=res, progressive='True').first()
    else:
        ys = yt.streams.filter(only_audio=True).get_audio_only()
    print("Downloading " + yt.title + "...")
    print(ys)
    ys.download()
    print("Download Complete!")


window = Tk()
v = StringVar(window, "1")
v1 = StringVar(window, "1")
window.geometry('600x600')
for(text, value) in values.items():
    Radiobutton(window, text=text, value=value, variable=v,
                indicator=0, background="light blue").pack()
Label(
    text="Input link to download"
).pack()
entry = Entry(width=75)
entry.pack()
button = Button(
    text="Download",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=lambda: download(entry.get(), v.get(), v1.get())
).pack()

button1 = Button(
    text="Quit",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: exit(0)
).place(x=240, y=400)

Label(
    text="Resolution: "
).pack()
for(text, value) in resolution.items():
    Radiobutton(window, text=text, value=value, variable=v1,
                indicator=0, background="light blue").pack()

window.mainloop()
