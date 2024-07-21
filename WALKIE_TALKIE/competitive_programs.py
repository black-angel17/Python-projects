empty = []

#list(map(lambda x : empty.append(x) , input().split()))

#print(empty)

#A, B, C = map(int, input().split())   # split return the list  1st three values of list assign to thess variab

#print (A, B, C)  # thse three varibale contrain 1st 3 values from the list

'''A, B = map((int, input().split())
C, D, E = map(int, input().split())
F, G, H, I = map((int, input().split()))

print(A, B, C, D, E, F, G, H, I)

Test cases are multiple Inputs - multiple instances of the same problem, all of which have to be solved by your code correctly.
 Consider 5 test cases or 5 inputs 


A,B = input().split()


'''


z = 6

for i in range(z):
    A, C = map(int, input().split())

    avg = (A + C) / 2
    avg = str(avg)
    a =avg[0]
    c =avg[2]
    if c == str(0):

        print(avg)
    else:
        print(-1)





