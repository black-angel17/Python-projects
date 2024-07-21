'''the sys module in Python provides valuable information about the Python interpreter and
allows you to obtain details about the constants, functions, and methods of the Python interpreter1

.The module provides access to some variables used or maintained by the interpreter and
to functions that interact strongly with the interpreter3
.Here are some of the uses of the sys module in Python:

'''
import sys

# this sys module  have some function which directly interact with python interpreter

# python interpreter itself maintain some  varibles like sys.argv which store commandline
#argumens as a list on it

'''
sys.stdin sys.sterr they are object represent the stream of data happening there
'''


print(sys.version)
print(sys.executable)
print(sys.path)
print(sys.platform)
a = sys.stdin.readline()
print(type(a))
sys.stdout.write(a)
import sys
# Redirect stderr to stdout


print()
print()


