import subprocess
import re
lister = []
def get_ssid():
    command = 'netsh wlan show profiles'
    output=subprocess.check_output(['cmd.exe', '/c', command])

    # Use regular expression to extract profile names
    pattern = re.compile(r'All User Profile\s+:\s+(.*)')
    matches = pattern.findall(output.decode('utf-8'))


     # Print the extracted profile names
    for match in matches:
        lister.append(match.rstrip('\r'))



def get_passwd():
    for y in lister:
        x = f'netsh wlan show profile name="{y}" key=clear'
        outputt=subprocess.check_output(['cmd.exe', '/c', x])

        pattern = re.compile(r'Key Content\s+:\s+(.*)')
        match = pattern.search(outputt.decode('utf-8'))

        if match:
            key_content_value = match.group(1)
            print(y + "====" + key_content_value)
        else:
            print("Key Content not found in the input text.")


get_ssid()
get_passwd()