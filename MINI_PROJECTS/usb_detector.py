import wmi
import tkinter as tk
from tkinter import messagebox

'''# Create a root window
root = tk.Tk()

# Hide the root window
root.withdraw()root.mainloop()
'''
print("start")
def start():
    c = wmi.WMI()

    #def detector():
    while True:
        usb_devices = c.Win32_USBControllerDevice()

        for usb_device in usb_devices:
            device = usb_device.Dependent
            if device.Description == "Disk drive":

                print("USB device detected:")
                print(f"  Device ID: {device.DeviceID}")
                print(f"  Description: {device.Description}")
                print(f"  Manufacturer: {device.Manufacturer}")
                print(f"  Caption: {device.Caption}")
                first_id = device.DeviceID
               #messagebox.showinfo("Alert", "-----USB---Detected-----")
                return  device.DeviceID,device.Description,device.Manufacturer,device.Caption

            else:
                continue


