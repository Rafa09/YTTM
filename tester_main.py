import telegram_management
import values_DONOTUPLOAD

text = telegram_management.telegram_connector(values_DONOTUPLOAD.app_id,values_DONOTUPLOAD.app_hash)
telegram_management.message_dict(text)