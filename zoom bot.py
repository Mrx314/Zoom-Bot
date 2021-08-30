import schedule
import time
import webbrowser






def open_link(link):
    webbrowser.open(link)



def click():
    open_link("Enter link here")


    



schedule.every().day.at("Enter time here").do(click)


while 1:
    schedule.run_pending()
    time.sleep(1)




