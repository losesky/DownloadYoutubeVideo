from pytube import YouTube

url = input("输入YouTube视频链接: ")
yt = YouTube(url)

# res 参数可以使用以下值：# 720p # 1080p
stream = yt.streams.filter(res='720p').first()
stream.download(output_path='video')

print("视频下载成功!")
