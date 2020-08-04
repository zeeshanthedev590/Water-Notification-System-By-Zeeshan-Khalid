import time
from plyer import notification
if __name__ == "__main__":
  while True:
    notification.notify(
        title = 'Please Drink Water Zeeshan',
        message = 'Drink Some Water',
        app_icon = 'E:\My projects\Python Projects\Water Notifications\water.ico',
        timeout= 12
    )
    time.sleep(60*60)