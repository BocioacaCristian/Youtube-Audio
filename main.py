import os.path
from pytube import YouTube
import tkinter

def youtube_audio():
    #Let's get the URL.
    url = url_entry.get()
    video = YouTube(url)

    #Extract the audio.
    audio_streams = video.streams.filter(only_audio=True).first()

    #Download the stream to my computer

    output_path = "C:/Users/Acasa/Desktop/TEST FOLDER"
    out_file = audio_streams.download(output_path= output_path)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file,new_file)

    #If the file has been downloaded

    print(video.title + " - Download successfull.")

window = tkinter.Tk()
window.title("YOUTUBE AUDIO DOWNLOADER!")
url_label = tkinter.Label(window, text="Enter URL:")
url_label.pack()

window.geometry('800x600')

url_entry = tkinter.Entry(window)
url_entry.pack()

download_button = tkinter.Button(window, text="Download", command=youtube_audio)
download_button.pack()

window.mainloop()