

string = '1 2 3 4'

x = string.split()  #which return a list
x.reverse() # this method not reverse anything it used pass by references
print(x)

stack = []

reverse = []
def append(x):
    stack.append(x)

def poper():
    return stack.pop()


for i in string.split():

    append(i)
    print(len(stack))

print(len(stack))
for i in range(len(stack)):
    reverse.append(poper())


    print(reverse)

# def fibonacci(n):
#     fib_series = [0, 1]
#     if n <= 1:
#         return fib_series[:n]
#     else:
#         for i in range(2, n):
#             fib_series.append(fib_series[-1] + fib_series[-2])
#             print('done')
#         return fib_series
#
# # Example usage:
# num = int(input("Enter the number of Fibonacci numbers to generate: "))
# print(f"The first {num} Fibonacci numbers are: {fibonacci(num)}")

print(chr(98))