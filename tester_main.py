import telegram_management
import values_DONOTUPLOAD
import audio_converter
import variables_yt_dl
# this file only contains app id and app hash needed to connect to the bot.
# Create your own file and enter the values received from Telegram

text = telegram_management.telegram_connector(values_DONOTUPLOAD.app_id,values_DONOTUPLOAD.app_hash)
#print(text[28])

result_all = telegram_management.message_dict(text)



eternal = 1000
update_id_counter = 434233491
while (eternal > 0):
    print(update_id_counter)
    print('outer loop start')
    result_number_counter = 0
    print(len(result_all))
    while result_number_counter < len(result_all):

        print('inner loop start')
        result = result_all[result_number_counter]
        #print(result)
        print(audio_converter.return_name(result['message']['text']))
        if result['update_id'] <= update_id_counter:
            result_number_counter = result_number_counter + 1
        else:
            #check if its a youtube video link
            try:
                audio_converter.audio_converter(telegram_management.telegram_send(result['message'], variables_yt_dl.ydl_opts))

                telegram_management.telegram_send(result['chat_id'], str(audio_converter.return_name(result['message']['text'])))

            except:
                telegram_management.telegram_send_error_msg(result_all[result_number_counter]['chat_id'], 1)
            result_number_counter = result_number_counter + 1
            update_id_counter = update_id_counter + 1
        print('inner loop end')
        # if (result_all[i]['update_id']==434233491):
        #     print(result_all[i]['message']['text'])
        #     telegram_management.telegram_send('739621619', 'ugh')
            #audio_converter.audio_converter(text_test[i]['message']['text'], ydl_opts)





    print('outer end of loop')