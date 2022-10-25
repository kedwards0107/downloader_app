from tkinter import *
from tkinter import ttk
from pytube import YouTube
from sys import argv

def download_item():    
    link = url_text.get()
    print(link)
    yt = YouTube(str(link))
    yd = yt.streams.get_highest_resolution()
    yd.download("/Users/mack/Desktop/Programming/Python/YouTube_downloads")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
url_text = StringVar()
ttk.Label(frm, text="URL Address").grid(column=0, row=0)
ttk.Entry(frm, textvariable=url_text).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)
ttk.Button(frm, text="Submit", command=download_item).grid(column=1, row=3)
root.title('YouTube Downloader')
root.geometry('375x75')
root.mainloop()
