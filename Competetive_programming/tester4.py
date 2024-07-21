
import subprocess

import ctypes
import time
from plyer import notification,gps
import time






def ping():
    z= 1
    while z:
        try:
            # Use the ping command to ping the host
            output = subprocess.check_output(['ping','1.1.1.1'])
            print(output.decode())
            x = output.decode().find('Reply from 1.1.1.1')
            print(x)
            if x != -1:
                print("The internet is  available.")
                notification.notify(
                    title='Error',
                    message='-------NETWORK----CAME--------',
                    app_name='Pycharm'
                )

                z = 0

            else:
                print("The internet is not available.")
                print('master')
        except Exception as e:
            print(f"An error occurred: {e}")




# Call the function to show the error box
#show_error_box()

ping()