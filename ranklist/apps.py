from django.apps import AppConfig


class RanklistConfig(AppConfig):
    name = 'ranklist'
    def ready(self):
        from ranklist import scheduler
        scheduler.start_job()
        print("Started")
