from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from ranklist.models import College

def start():
    scheduler = BackgroundScheduler()
    colleges = College.objects.all()
    for college in colleges:
        scheduler.add_job(college.get_results, 'interval', minutes=30)
    scheduler.start()
