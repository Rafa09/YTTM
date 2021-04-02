import requests


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