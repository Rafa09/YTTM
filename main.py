import audio_converter
import telegram_management

link = 'https://www.youtube.com/watch?v=hnXD6FRZtn0'
ydl_opts = {
        'video': 'no-playlist',
        'outtmpl': '~/Music/%(title)s.%(ext)s',
        'extract-audio': 'mp3',
        'format': 'bestaudio/best',
        'postprocessors':
            [{'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'}]
        }
audio_converter.audio_converter(link, ydl_opts)
