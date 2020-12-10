import schedule
import time

def job():
    Py manage.py runserver 192.168.0.21:8000

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)