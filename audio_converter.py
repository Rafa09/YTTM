from pydub import AudioSegment
import youtube_dl

def audio_converter(link, ydl_opts):
    # link contains the YT-link, ydl-opts your preferred download settings.
    # See https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme for options
    # Careful! Not all have the same description or function in Python.
    # output e.g. is outtempl

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(link, download=False)
        # We just want to extract the info
        # Error message to be added if it is not a video link

    if 'entries' in result:
        #doesnt work
        print('error')
    else:
        ydl.download([link])
