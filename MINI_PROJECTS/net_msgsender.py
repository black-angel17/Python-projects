import requests
import usb_detector as u
# createing  a telegram bot using the python

token = "https://api.telegram.org/bot6400127187:AAEjwyYz_zzAvkZDLzDRPEA5ZCniMB1wkcU/getUpdates"

respose = requests.get(token)

def send_msg_to_bot(forma):
    format = forma

    baseurl = f'https://api.telegram.org/bot6400127187:AAEjwyYz_zzAvkZDLzDRPEA5ZCniMB1wkcU/sendMessage?chat_id=-964504599&text={format}'
    print(baseurl)
    requests.get(baseurl)


x = u.start()
print('-----------')
send_msg_to_bot('USB Detected')
for i in range(4):
    send_msg_to_bot(x[i])



'''text_values = [item["message"]["text"] for item in data["result"] if "message" in item and "text" in item["message"]]

# Print the 'text' values
for text in text_values:
    print(text)'''