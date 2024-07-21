import pygetwindow as gw
import time
 # what are the things user seeing now we can see it

'''def close_active_window():
    active_window = gw.getActiveWindow()
    if active_window is not None:
        active_window.close()'''


def get_active_window_title():
    active_window = gw.getActiveWindow()
    if active_window is not None:
        return active_window.title
    return None


def get_active_windows():
    active_windows = gw.getAllTitles()

    return active_windows

# Example usage
active_windows = get_active_windows()
if active_windows:
    print("Active Windows:")
    active_windows.close()
    for window in active_windows:
        print(window)
else:
    print("No active windows found.")


'''
for i in range(5):
    time.sleep(2)
    active_window_title = get_active_window_title()
    if active_window_title is not None:
        print("Active window title:", active_window_title)
        time.sleep(2)
        #close_active_window()
    else:
        print("No active window found.")'''


#active_window.close() this will close  current active window