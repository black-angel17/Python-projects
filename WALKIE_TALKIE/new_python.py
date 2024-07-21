
# ALL DASTA structure related things here
rev = "hello"

print(rev[0:4:2])

s1 = "--geeks for geeks what u geeks want here geeks is this boy geeks"
s2= "geeks"

print(ord('a'))
print(chr(97))

print(s2 in s1)

print(s1.index(s2))

print(s1.find("geeks",3))

print(s1.strip('-'))

print(len(s2))
'''

def all_occur(x):
    position = 0
    all =[]
    while position != -1:
        position += 1
        position = x.find("geeks", position)
        if position == -1:
          break
        else:
            all.append(position)
    return  all

s= all_occur(s1)
print(s)

'''

binary = "hellobuddy"

print(binary[0:9:2])