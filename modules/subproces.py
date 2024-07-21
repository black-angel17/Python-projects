
import subprocess

#subprocess
''' 
this subprocess module main thing is create a new process  on RAM like a active shell --
--run commands or run other program from it then control std input output error stream from python
--i can control another program from python script

subprocess.run()(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, 
text=None, shell=False, timeout=None, check=False, encoding=None, errors=None, env=None)

.call()- IT  Return the Return code(0 - executed succesfully _NEG value means not runned )
 and command itself -- simipler form of run() function

just subprocess.call() -  itself print the output no need of  p rint if we save this on variable and print
it we see the return code get saveed on the varibale itself++++

subprocess.check_output = retunr   the output as a byte stirng

check_call() = it return the  return code (0 - executed succesfully)instead of output
+++++
.popen() more Advance than run() has more parameter it consider that new created process as a objec


'''

#os module
'''
this for interacting with os funciotn like files manaagement sinple commands without new process creation
-Direactory manipulation, os doing certain task we  manage it from this module
, process management uid euid



'''


# Execute the "ls" command
result = subprocess.run(['ls' , '-la'],  text=True, stdout=subprocess.PIPE) # we need to give commands as
# a list of  element with ''  comma also
print(result)

# this run return a object


print(result.stdout)
# Separate standard output and standard error
result = subprocess.run(['ls', 'file.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output = result.stdout
# this arugument subprocess.PIPE ===== only for std out and err it tells that the executedd  program to
#pipe the output to its attributes of them, we redirect the ouput from the program to respective values or files
#PIPE -  tells capture the OUTPUT


'''text=True -  tells the output as a string,
 shell=False- command exe with out shell,\
  timeout=2 - maximum time limit of 2 sec for command execuition if command take more sec then program expire, 
  check=True - ensure return is 0  not 1 , 
  encoding='utf-8' -  this specify the output is encoded wiht this form, 
  errors= ignore - tells ignore if any decode errors occuires there '''

error = result.stderr
print(result)
print("Output:", output)
print("Error:", error) # we access each  output in different stream

