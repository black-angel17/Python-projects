import datetime
import requests
import json
import time


# Get the current date and time
current_datetime = datetime.datetime.now()
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_date = current_datetime.date()
'''print("Current time:", current_datetime)
print("Current hour:", current_hour)
print("Current minute:", current_minute)
print("Current date:", type(current_date))'''




def send_msg_to_bot(forma):
    format = forma
    baseurl = f'https://api.telegram.org/bot6400127187:AAEjwyYz_zzAvkZDLzDRPEA5ZCniMB1wkcU/sendMessage?chat_id=-964504599&text={format}'
    print(baseurl)
    requests.get(baseurl)

while True:
    time.sleep(30)
    current_datetime = datetime.datetime.now()
    current_hour = current_datetime.hour
    current_minute = current_datetime.minute
    current_date = current_datetime.date()

    with open('output.json', 'r') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        parsed_data = data["meeting"]
        for item in parsed_data:
            # Access values within each object
            form = item['msg']
            date = item['date']
            tim = item['time']
            print(tim)


            total = f"{current_hour}:{current_minute}"
            print(total)
            if  str(current_date) == date:


                if total == tim:

                    send_msg_to_bot(form)
                    print("+++Messege has been sended ")



