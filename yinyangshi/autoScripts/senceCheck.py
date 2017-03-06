#coding=utf-8
from datetime import datetime
import time
import identifySimilarImage
import heapq
import globalFacts
import os

from apscheduler.schedulers.background import BackgroundScheduler
senceList = [
    {"sence":"tingYuan","path":"prePic/tingYuan_no_juanZhou.png"},
    {"sence":"tanSuo","path":"prePic/tanSuo.png"}
]


#返回当前的场景值
def tick(screenShotPath):
    rmslist = {}
    for sence in senceList:
        rmslist[identifySimilarImage.compare_and_return_rms(sence["path"],screenShotPath)] = sence["sence"]
    smallest =  heapq.nsmallest(1, rmslist.keys())
    print('now in sence ' % rmslist[smallest])
    globalFacts.SENCE = rmslist[smallest]
    return rmslist[smallest]


def sence_check(screenShotPath):
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick(screenShotPath), 'interval', seconds=3)
    #在指定的时间，只执行一次
    scheduler.start()