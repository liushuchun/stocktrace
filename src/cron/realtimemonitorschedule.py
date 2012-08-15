'''
Created on 2012-8-15

@author: Simon
'''
def periodic(scheduler, interval, action, actionargs=()):
  scheduler.enter(interval, 1, periodic,
                  (scheduler, interval, action, actionargs))
  action(*actionargs)
  #scheduler.run( )
  
  
if __name__ =="__main__":    
    import time, os, sys, sched
    from parse.sinaparser import getMyStock
    schedule = sched.scheduler(time.time, time.sleep)
#    schedule.enter(0, 0, getMyStock, ())   # 0==right now
#    schedule.run( )
    periodic(schedule, 30, getMyStock)
    schedule.run( )
  