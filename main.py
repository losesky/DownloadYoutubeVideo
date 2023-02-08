import base64
import os

import streamlit as st
import pytube


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" ' \
           f'download="{os.path.basename(bin_file)}">点击下载 {file_label}</a> '
    return href


def main():
    st.write("Welcome to YouTube Video Downloader")

    url = st.text_input("Enter the URL of the video: ")
    if url:
        yt = pytube.YouTube(url)
        videos = yt.streams.all()
        st.write("Select the video format: ")
        fm = st.selectbox("Format", [v.resolution for v in videos])
        video = yt.streams.get_by_resolution(fm)

        if st.button("Download"):
            video_file = video.download(output_path='dl')
            # st.write("Downloaded Video:")
            # st.write(video_file.title())
            st.write("Click the link below to download the video:")
            st.markdown(get_binary_file_downloader_html(video_file, ""), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
