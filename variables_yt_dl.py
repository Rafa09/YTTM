path_to_music = '/home/admin_telegram_bot/Music/'
ydl_opts = {
    'video': 'no-playlist',
    'outtmpl': path_to_music + '%(title)s.mp3',
    'extract-audio': 'mp3',
    'format': 'bestaudio/best',
    'postprocessors':
        [{'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192'}]
}
update_id_last = 434233504

