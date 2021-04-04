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
#Bullshit variable to keep the program going on indefinitely
update_id_counter = variables_yt_dl.update_id_last
#start at a certain point (tbd) in the history of the chat
while (eternal > 0):
    text = telegram_management.telegram_connector(values_DONOTUPLOAD.app_id, values_DONOTUPLOAD.app_hash)
    # get back the complete currently saved updates
    result_all = telegram_management.message_dict(text)
    # filter out the results
    print('outer loop start')
    result_number_counter = 0
    #reset the counter; result_all contains result from 0 to end; once all are analyzed, a new update is received

    while result_number_counter < len(result_all):
    # ensure only existing result entries are analyzed
        print('inner loop start')
        result = result_all[result_number_counter]
        # individual message
        if result['update_id'] <= update_id_counter:
            result_number_counter = result_number_counter + 1
            # go to the next result entry
        else:

            try:

                audio_converter.audio_converter(result['message']['text'], variables_yt_dl.ydl_opts)
                # attempt conversion of link
                result_short = result['message']['from']['id']
                # assistance to make lines shorter
                link_of = result['message']['text']
                # assistance to make lines shorter
                name_of_song = audio_converter.return_name(link_of)
                # return name of file/music
                telegram_management.telegram_send(result_short, name_of_song)
                # send file to sender
                #print(str(audio_converter.return_name(result['message']['text'])) + 'nonsense')

            except:
                telegram_management.telegram_send_error_msg(str(result['message']['from']['id']), 1)
                # if try doesnt work, send an error message
            result_number_counter = result_number_counter + 1
            # go to the next result entry
            update_id_counter = update_id_counter + 1
            # update id so that earlier messages are not considered
        print('inner loop end')






    print('outer end of loop')