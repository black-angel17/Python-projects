
import socket
import time
import requests

# createing  a telegram bot using the python

token = "https://api.telegram.org/bot6400127187:AAEjwyYz_zzAvkZDLzDRPEA5ZCniMB1wkcU/getUpdates"

chatid = "-964504599"




format = "INTERNET ------ Connection came"
def send_msg_to_bot():
    baseurl = f'https://api.telegram.org/bot6400127187:AAEjwyYz_zzAvkZDLzDRPEA5ZCniMB1wkcU/sendMessage?chat_id=-964504599&text={format}'
    print(baseurl)
    requests.get(baseurl)
def is_internet_available():
    try:
        # Attempt to resolve a well-known host (e.g., Google's DNS server)
        host = "8.8.8.8"
        socket.create_connection((host, 53), 2)
        return True
    except OSError:
        pass
    return False

x =True
while x:
    if is_internet_available():
        print("Internet connection is available.")
        send_msg_to_bot()
        time.sleep(5)
        x = False

    else:
        print("No internet connection.")
        time.sleep(5)


