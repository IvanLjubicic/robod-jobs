from mongoengine import *
import schedule
import time
from walkthrough.main_subprocess import MainJobs

connect(
    host="mongodb://localhost/robod",
    port=27017
)

def job():
    MainJobs.run()
     
schedule.every(0.1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
