import requests
import values_DONOTUPLOAD
import variables_yt_dl

def telegram_connector(app_id, app_hash):
    requestURL = "https://api.telegram.org/bot" + app_id + ":" + app_hash + "/getUpdates"

    update_raw_direct = requests.get(requestURL)
    update_raw = update_raw_direct.json()

    return update_raw


def message_dict(dict):
    result_array = dict['result']
    return result_array


def telegram_send(chat_id, name_of_song):
    print(chat_id)
    print(name_of_song)
    with open(variables_yt_dl.path_to_music + name_of_song + '.mp3', 'rb') as audio:
        payload = {
            'chat_id': chat_id,
            'title': name_of_song,
            'parse_mode': 'HTML'
        }
        files = {
            'audio': audio.read(),
        }
        resp = requests.post(
            "https://api.telegram.org/bot{token}/sendAudio".format(
                token=values_DONOTUPLOAD.app_id + ':' + values_DONOTUPLOAD.app_hash),
            data=payload,
            files=files).json()


def telegram_send_error_msg(chat_id, number):
    if number == 1:
        text = 'please send a youtube link. Currently a message containing other content or symbols beyond the link cannot be processed. It is also possible that the video in question is DRM- or age-protected. The file-size can alo contain issues. Telegram caps at 20 mb'
    else:
        text = 'unclear error'

    requests.get('https://api.telegram.org/bot' + values_DONOTUPLOAD.app_id + ':' + values_DONOTUPLOAD.app_hash + '/sendMessage?chat_id=' + chat_id + '&text=' + text)
