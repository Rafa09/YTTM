import audio_converter
import telegram_management

#link = 'https://youtu.be/9lzZqz5PImo'
link = "https://www.youtube.com/watch?v=eFursscG_Oc"
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
