import requests
from urllib.parse import quote


# path = "/c38b7510 e085b975/dfcc3551 6854aa55"
# path_en= quote(path)

url = 'http://localhost/'
head = {'Host':"461cd835df27ca1eaf63c4237b32c3a6",'content-type': 'application/json'}
#we need to write every headers as dictionary here

#get parameters
payload = {'a':'54532107a89c08a7b5e50fbd2df2905','b':{'c':'0d9c764b','d':['cbda4fed','aa5ae74e a20921f0&13e954ae#bac7fe5c']}}

#pay = {}

r = requests.get(url,headers=head)
'''this is for get request now see post
data = payload for sending data in post body
params = payload for send data in get url body
json = in json format sending data 

must modify the content-typ[re header before sending the data

r = requests.post(url,headers=head,json=payload)

'''

print(r.cookies)



#in this function the parameter=argument we supply
print(r.text)
print(r.url +f"{r.history}")