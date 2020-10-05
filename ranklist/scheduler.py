from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from ranklist.models import College

def start_job():
    scheduler = BackgroundScheduler()
    colleges = College.objects.all()
    for college in colleges:
        scheduler.add_job(college.get_results, 'interval', minutes=20)
    scheduler.start()
