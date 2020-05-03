from pytube import YouTube


url_file = open('/Users/xstar/PycharmProjects/Youtube_downloader/videos.txt', 'r+')
url_list = url_file.readlines()
url_file.truncate(0)
url_file.close()

for url in url_list:
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    video.download('/Users/xstar/Music')
    print(youtube.title, "downloaded")

print("Successfully downloaded ", len(url_list), "songs.")