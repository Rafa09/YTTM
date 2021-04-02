import requests
import values_DONOTUPLOAD


def telegram_connector(app_id, app_hash):
    requestURL = "https://api.telegram.org/bot" + app_id + ":" + app_hash + "/getUpdates"
    print(requestURL)
    update_raw_direct = requests.get(requestURL)
    update_raw = update_raw_direct.json()
    print(update_raw)
    return update_raw

def message_dict(dict):
    result_array = dict['result']
    return result_array

def telegram_send(chat_id, name_of_song):
    with open('/home/development/Music/American Psycho • Hip to Be Square • Huey Lewis and the News.mp3', 'rb') as audio:
        payload = {
            'chat_id': chat_id,
            'title': 'American Psycho • Hip to Be Square • Huey Lewis and the News.pdf',
                     'parse_mode': 'HTML'
        }
        files = {
            'audio': audio.read(),
        }
        resp = requests.post(
            "https://api.telegram.org/bot{token}/sendAudio".format(token=values_DONOTUPLOAD.app_id + ':' + values_DONOTUPLOAD.app_hash),
            data=payload,
            files=files).json()
    #send_text = 'https://api.telegram.org/bot' + values_DONOTUPLOAD.app_id + ':' + values_DONOTUPLOAD.app_hash + '/sendDocument?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + '/home/development/Music/American Psycho • Hip to Be Square • Huey Lewis and the News.pdf'
  #  response = requests.get(send_text)