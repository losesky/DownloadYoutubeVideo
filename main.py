import streamlit as st
import pytube


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
            # st.write(video_file)
            st.write("Click the link below to download the video:")
            st.markdown("[Download Video](" + video_file + ")", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
