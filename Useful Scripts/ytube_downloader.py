from pytube import YouTube
from tqdm import tqdm

def download_video(url, save_path):
    youtube = YouTube(url)
    video_stream = youtube.streams.get_highest_resolution()

    total_size = video_stream.filesize
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

    def on_progress(chunk, file_handle, remaining):
        progress_bar.update(chunk)

    video_stream.download(output_path=save_path, filename=video_stream.default_filename, 
                          skip_existing=False, on_progress_callback=on_progress)
    progress_bar.close()

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    save_directory = input("Enter the directory to save the video in: ")

    download_video(video_url, save_directory)

