# src/scheduler.py
import schedule
import time
from typing import Callable

class Scheduler:
    def __init__(self):
        self.jobs = []

    def _schedule_job(self, day: str, time_str: str, job_func: Callable):
        time_parts = time_str.split(":")
        hour = int(time_parts[0])
        minute = int(time_parts[1])

        if day == "monday":
            job = schedule.every().monday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "tuesday":
            job = schedule.every().tuesday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "wednesday":
            job = schedule.every().wednesday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "thursday":
            job = schedule.every().thursday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "friday":
            job = schedule.every().friday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "saturday":
            job = schedule.every().saturday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "sunday":
            job = schedule.every().sunday.at(f"{hour:02d}:{minute:02d}").do(job_func)

        self.jobs.append(job)

    def schedule_weekly(self, days: list, time_str: str, job_func: Callable):
        for day in days:
            self._schedule_job(day.lower(), time_str, job_func)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(60)