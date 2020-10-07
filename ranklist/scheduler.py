from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from ranklist.models import College
import datetime

def start_job():
    scheduler = BackgroundScheduler()
    colleges = College.objects.all()
    print("Number of jobs = ", len(colleges))
    i = 0
    for college in colleges:
        now = datetime.datetime.now() + datetime.timedelta(i*10)
        scheduler.add_job(college.get_results, 'interval', start_date = str(now)[:-7] minutes=2)
    scheduler.start()
