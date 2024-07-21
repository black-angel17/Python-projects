import requests

# this help to interact with web services


url = "http://192.168.136.128"


response = requests.get(url) # this request is just a normal module get is funcion not oops
# the get function return a object so that is storing on response
#it has some buil in class Request it gives a objects of it to response


#   response ==  return_object  responese >>point at a address


#so we access the data and methods using response varible


#this response varible is not a oops object rather it stores an  instance(object ) of Response class
#so it behave like a  REAL OBJECT


'''
Apologies for any confusion caused. In the context of the code snippet response = requests.get(url), the response variable is not an object in the object-oriented programming (OOP) sense. It is simply a variable that holds the response returned by the requests.get() function.

The requests.get() function is invoked from the requests module, and it returns a Response object that encapsulates the response received from the server. The Response object is not a user-defined class but rather an instance of a built-in class provided by the requests library.

In Python, objects are instances of classes, and they encapsulate both data and behavior. While the Response object returned by requests.get() has attributes and methods that allow you to access and process the response data, it is not something you define or create using traditional OOP principles.

You can interact with the response object and access its attributes and methods to retrieve information about the response, such as the status code, headers, or response content. However, it's important to note that the response object itself is an instance of the Response class provided by the requests library.

So, to clarify, the response variable in this context is not an object in the OOP sense, but rather an instance of the Response class that the requests library provides. It allows you to access the properties and methods of the Response class to process the HTTP response data.

Regenerate response
Send a message.

Free Research Preview. ChatGPT may produce inaccurate information about people, places, or facts. ChatGPT May 24 Version

'''
print(response.text) # this gives us all html content of the page


print(dir(response)) # by this i can able to find the attributes and methods
# accessible by this object here

'''apparent_encoding', 'close', 'connection',
 'content', 'cookies', 'elapsed', 'encoding', 
 'headers', 'history', 'is_permanent_redirect',
 'is_redirect', 'iter_content', 'iter_lines', 
 'json', 'links', 'next', 'ok', 'raise_for_status',
 'raw', 'reason', 'request', 'status_code', 'text', 'url']'''

print(response.raw) # this is this object mem address value stores on __str

print(response.headers) # this contain the response header values
# this header is dictionary

for i,j in response.headers.items(): # this iterables like dict

    print(i + "::"+ j)


print(response.status_code)


#hello this is for testing

