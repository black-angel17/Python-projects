
#RE module

'''

# REFER PYTHEX----Website
-For Pattern matching of only on _+++ strings +++,

\ - for escape speical char \. refer the dot  \@ refer the @

. = only dot means any thing it refer

^ at start of str , $ at end of str

[0-9,a-z] = it defines like this  [^] this ^ tells other than that

\A = it return first word of string if it was on 1st

\b -  it represent empty space at word boundary   \bword\b - it match the words if in has spaces between
before and after the word

\B - match a word not located between spaces it match words inbetween words  let___me like this it matchh

\d -  matches only digits
\D -  matches everything othern than digits inclue special chara

\s - mathes only whitespaces
\S - matches any non whitespace-characters -just everything


this module has five function



re.match - return only if it was begining of string
re.search -  return as a object   //this search function return a object ->  .group(index ) to acces inside it

re.findall -  return as list that ahas many occurance
re.finditer -  return as iterable object we directly uses on for loop
re.sun -  for replce words with other words











pip is the packet manager in python

pip install pack == version for specifired version here
create a requirement.txt  then  save these thing on it

pip install -r requuirement.txt will proint everythin on it

#python virtual environments

if you need to  diffrent version of the same module on different programs
will create a problem on it so  create a virtual environent for specific version of module

creating virtual environment

python3 -m venv env  -- execute venv - it create a new virtual environment on env directory

-m tells tell me module name i execute the scipt on it directly form init main

source env/bin/activate  --- to activate the virtaul environment use this
deactivate -- just it deactivate th venv

Once the virtual environment is activated,
 any Python packages you install will be isolated to that environment



'''
from pwn import *


def add(x):
    print(x)


