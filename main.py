import os.path

from pytube import YouTube


#Let's get the URL.

video = YouTube(str(input("Enter the URL: \n")))

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