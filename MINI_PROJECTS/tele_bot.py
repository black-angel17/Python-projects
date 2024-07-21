import time
import requests
import json

art =""" 

  _____    _          ____       _                  ____   ___ _____ 
 |_   _|__| |    ___ / ___|_ __ / \   _ __ ___     | __ ) / _ \_   _|
   | |/ _ \ |   / _ \ |  _| '__/ _ \ | '_ ` _ \    |  _ \| | | || |  
   | |  __/ |__|  __/ |_| | | / ___ \| | | | | |   | |_) | |_| || |  
   |_|\___|_____\___|\____|_|/_/   \_\_| |_| |_|___|____/ \___/ |_|  
                                              |_____|                

"""
print(art)
b ="""
+++++++    show - to show the current meetings  +++++++   
+++++++    add - this add new meetings          +++++++   
+++++++    del - this delete meet after time    +++++++   
"""
print(b)


token = "https://api.telegram.org/bot6400127187:AAEjwyYz_zzAvkZDLzDRPEA5ZCniMB1wkcU/getUpdates"
chatid = "-964504599"



#Here we need to create an object for each thing and del the object when needed
# so everytime you save something ir deletes after everytime  when you run a program so create a file like json


def add_meeting():

    id = input('enter the meeting id::')
    msg = input('enter the msg::')
    date = input('enter the time- in this format[YEAR-MONTH-DATE]::')
    time = input('enter the Hour:Minute::')

    with open(r'C:\Users\ADMIN\PycharmProjects\pythonProject\output\output.json', 'r') as json_file:
        json_data = json_file.read()
    data = json.loads(json_data)
    #parsed_data = data["meeting"]
    data["meeting"].append(dict( id=id, msg=msg,date= date ,time=time))
    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)


def clear_metting():
    pid = input("enter the id of the meeting to delete::")
    with open(r'C:\Users\ADMIN\PycharmProjects\pythonProject\output\output.json', 'r') as json_file:
        json_data = json_file.read()
    data = json.loads(json_data)
    # Find the element with "id": "1" in the "meeting" array and remove it
    meeting_array = data["meeting"]
    meeting_to_delete = next((item for item in meeting_array if item["id"] == pid), None)
    print(meeting_to_delete)
    if meeting_to_delete:
        meeting_array.remove(meeting_to_delete)

    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)
        print("meeting has been cleared+++++")

def show_metting():
    with open(r'C:\Users\ADMIN\PycharmProjects\pythonProject\output\output.json', 'r') as json_file:
        json_data = json_file.read()
    data = json.loads(json_data)
    parsed_data = data["meeting"]
    for item in parsed_data:
        # Access values within each object
        value = item
        print(value)

while True:
    tic = input(">>> Enter the Command >>:::")
    if tic == 'add':
        add_meeting()
    elif tic == 'show':
        show_metting()
    elif tic == 'del':
        clear_metting()
    elif tic == 'exit':
        exit()
    else:
        print('error in command')
