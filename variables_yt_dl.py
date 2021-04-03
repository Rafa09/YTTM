ydl_opts = {
    'video': 'no-playlist',
    'outtmpl': '~/Music/%(title)s.mp3',
    'extract-audio': 'mp3',
    'format': 'bestaudio/best',
    'postprocessors':
        [{'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192'}]
}
