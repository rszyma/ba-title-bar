from pytube import YouTube

LINK = "https://www.youtube.com/watch?v=FtutLA63Cp8"
YT_LINK = YouTube(LINK)

highres_stream = YT_LINK.streams.get_highest_resolution()
highres_stream.download()
