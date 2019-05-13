import schedule,time

def job():
    print("'I'm working....")

#schedule.every(10).minutes.do(job)  #部署每10分钟执行一次job()函数的任务
schedule.every(1).seconds.do(job)   #部署每1秒钟执行一次job()函数的任务
#schedule.every().hour.do(job) #部署每个小时执行一次job()函数的任务
#schedule.every().day.at("10:30").do(job) #部署在每天的10：30执行一次job()函数的任务
#schedule.every().monday.do(job) #部署每个星期一执行一次job()函数的任务
#schedule.every().wednesday.at("13:15").do(job) #部署每周三的13:15执行函数的任务

a = 0 
while a < 5:
    a = a + 1
    schedule.run_pending()
    time.sleep(1)