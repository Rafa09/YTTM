import telegram_management
import values_DONOTUPLOAD
import audio_converter
# this file only contains app id and app hash needed to connect to the bot.
# Create your own file and enter the values received from Telegram

text = telegram_management.telegram_connector(values_DONOTUPLOAD.app_id,values_DONOTUPLOAD.app_hash)
#print(text[28])

text_test = telegram_management.message_dict(text)

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


print(text_test)
print('alpha')
print(type(text_test))
i=0
while (i<len(text_test)):
    print(text_test[i])
    print(type(text_test[i]))
    print(text_test[i]['update_id'])

    if (text_test[i]['update_id']==434233490):
        print(text_test[i]['message']['text'])
        telegram_management.telegram_send('739621619', 'ugh')
        audio_converter.audio_converter(text_test[i]['message']['text'], ydl_opts)
        i=i+1
    else:
        print(i)
        i=i+1



print(type(text_test))