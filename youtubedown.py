#!/usr/bin/python3
from pytube import YouTube
from termcolor import colored
from os import system,name
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *

# download code:
def info(url):
    video=YouTube(url)
    length=str(int(video.length/60))
    ratings=str(int(video.rating))
    views=str(int(video.views))
    print(colored("\n\t\tTitle: "+video.title+"\n","red"))
    print(colored("\t\t\t\tLength: "+length+"\tViews: "+views+"\tRatings: "+ratings+"\n","green"))
    startDownload(url)

def completeDownload(stream=None, file_path=None):
    print("download completed")
    showinfo("Message", "File has been downloaded...")
    down['text'] = "Download Video"
    down['state'] = "active"
    url.delete(0, END)

def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    down['text'] = "{:00.0f}% downloaded ".format(percent)


def startDownload(url):
    global file_size
    path = askdirectory()
    if path is None:
        return

    try:
        video = YouTube(url)
        st = video.streams.first()

        video.register_on_complete_callback(completeDownload)
        video.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(path)

    except Exception as e:
        print(e)
        print("something went wrong")
    
def capbuttn():
    try:
        down['text']= "Please wait..."
        down['state']='disabled'
        link = url.get()
        if link== ' ':
            return
        t=Thread(target=info,args=(link,))
        t.start()
    except Exception as e:
        print(e)


#GUI
gui=Tk()
gui.title("Youtube video downloader")



file=PhotoImage(file="gui.png")
icon=Label(gui,image=file)
icon.pack(side=TOP,pady=3)
#URL field
url=Entry(gui,justify=CENTER)
url.pack(side=TOP,fill=X,padx=10,pady=20)
url.focus()

#Download button
down=Button(gui,text="Download Video",relief="ridge",command=capbuttn)
down.pack(side=TOP,fill=X,padx=50,pady=10)

#GEometry
gui.geometry("500x600")
gui.mainloop()





