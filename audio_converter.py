from pydub import AudioSegment
import youtube_dl
import variables_yt_dl
import telegram_management

def audio_converter(link, ydl_opts):
    # link contains the YT-link, ydl-opts your preferred download settings.
    # See https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme for options
    # Careful! Not all have the same description or function in Python.
    # output e.g. is outtempl

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(link, download=False)
            if 'entries' in result:
            # doesnt work
                return False
            else:
                ydl.download([link])
                return True
        except :
            return False

        # We just want to extract the info
        # Error message to be added if it is not a video link




def return_name(link):
    with youtube_dl.YoutubeDL(variables_yt_dl.ydl_opts) as ydl:
        try:
            result = ydl.extract_info(link, download=False)
            #print(result['title'])
        except:
            return False


def supported(url):
    ies = youtube_dl.extractor.gen_extractors()
    for ie in ies:
        if ie.suitable(url) and ie.IE_NAME != 'generic':
            # Site has dedicated extractor
            return True
    return False

