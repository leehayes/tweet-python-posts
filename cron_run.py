"""
This is the module called by the cron task which will decide which sources to run and produce a tweet for
"""
import random
import Config
job_times = Config.job_times

#Cron will run x times a day, and will providing a different parameter to indicate time


def start(runtime):
    if runtime not in job_times:
        runtime = random.choice(list(job_times)) # handles in runtime == None or missing from job_times
    tasks = job_times.get(runtime)
    for x in tasks:
        x()


start("9am")
