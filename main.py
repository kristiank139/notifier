import os
import time

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

while True:
    notify("Reminder", "Alert")
    time.sleep(10)