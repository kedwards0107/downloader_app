from logging import PlaceHolder
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from sys import argv
from tkinter import messagebox

def clear_text():
    url_entry.delete(0, END)
   
def download_item():    
    if  url_text.get() == '':
        messagebox.showerror('Required Field', 'Please enter "URL Address"')
        return
    link = url_text.get()
    path = path_text.get()
    print(path)
    print(link)
    yt = YouTube(str(link))
    yd = yt.streams.get_highest_resolution()
    yd.download(str(path))
    clear_text()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
url_text = StringVar()
path_text = StringVar()

ttk.Label(frm, text="URL Address").grid(column=0, row=0)
url_entry = ttk.Entry(frm, textvariable=url_text)
url_entry.grid(column=1, row=0)
ttk.Label(frm, text="Save to").grid(column=0, row=1)
path_entry = ttk.Entry(frm, textvariable=path_text)
path_entry.grid(column=1, row=1)
path_entry.insert(0, "/Users/mack/Desktop/Programming/Python/YouTube_downloads")
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)
ttk.Button(frm, text="Submit", command=download_item).grid(column=1, row=3)
root.title('YouTube Downloader')
root.geometry('375x90')
print(path_text.get())
root.mainloop()


