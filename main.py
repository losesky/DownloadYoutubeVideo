import streamlit as st
import pytube
import pyperclip


def main():
    st.set_page_config(page_title="Youtube Video Downloader", page_icon=":video_camera:", layout="centered")
    st.title("欢迎使用YouTube视频下载器\n"
             "Welcome to YouTube Video Downloader")

    url = st.text_input("输入YouTube上复制的视频地址：\n"
                        "Enter the URL of the video: ")
    if url:
        yt = pytube.YouTube(url)
        resolutions = [x.resolution for x in yt.streams.filter(progressive=True) if x.resolution != "144p"]
        if not resolutions:
            st.error("No resolution higher than 144p found.")
        else:
            selected_resolution = st.selectbox("选择视频分辨率：\n"
                                               " Select the video format: ", options=resolutions, index=0)
            video = yt.streams.get_by_resolution(selected_resolution)
            video_link = video.url
            st.write(
                "<video width='100%' controls autoplay><source src='{}' type='video/mp4'>"
                "Your browser does not support the video tag.</video>".format(video_link), unsafe_allow_html=True)
            if st.button("Copy to Clipboard"):
                try:
                    pyperclip.copy(video_link)
                    st.success("视频下载链接已经拷贝在粘贴板，粘贴到浏览器中打开.\n"
                               " The download URL is copied to the clipboard.")
                except pyperclip.PyperclipException as e:
                    st.warning("复制视频下载链接，粘贴到浏览器中打开：\n"
                               " The Pyperclip unsupported，The download URL：\n\n" + video_link)


if __name__ == "__main__":
    main()
