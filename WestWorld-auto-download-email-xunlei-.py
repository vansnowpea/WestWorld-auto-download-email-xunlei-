# -*- coding: utf-8 -*-
# python 3.5.2
# 测试系统，Win10
# Author:Van
# 实现《西部世界》有更新后自动下载，以及邮件通知
# V1.0
# 欢迎各种改进意见
# 请把对应的帐号密码修改成自己的


# from selenium import webdriver
import requests
from lxml import etree
import time
import os
from win32com.client import Dispatch
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import copy

# hints
print('请确保电脑安装了迅雷')
print('如果你用的是破解版的迅雷，请先开启再运行程序')
print()
# requests
url = 'http://www.btbtdy.com/btdy/dy7280.html'
html = requests.get(url).content.decode('utf-8')

# lxml
selector = etree.HTML(html)
real_link = []

# to be easy, try 'starts-with' , very useful in this case :)
HDTV = selector.xpath('//a[starts-with(@title, "HDTV-1080P")]/text()')
for each in HDTV:
    print(each)


href = selector.xpath('//a[starts-with(@title, "HDTV-1080P")]/@href')
print()
print('目前有 %d 集西部世界' %len(href))
print()

for each in href:
    # split to get the right magnet link
    each = 'magnet' + each.split('magnet')[-1]
    # print(each)
    real_link.append(each)

print('他们的磁链接是 :\n', real_link)
# define a temp_link in deepcopy to compare for new series
temp_link = copy.deepcopy(real_link)
print('temp_link is :', temp_link)


def addTasktoXunlei(down_url,course_infos):
    flag = False
    o = Dispatch("ThunderAgent.Agent.1")
    if down_url:
        course_path = os.getcwd()
        try:
            #AddTask("下载地址", "另存文件名", "保存目录","任务注释","引用地址","开始模式", "只从原始地址下载","从原始地址下载线程数")
            o.AddTask(down_url, '', course_path, "", "", -1, 0, 5)
            o.CommitTasks()
            flag = True
        except Exception:

            print(Exception.message)
            print(" AddTask is fail!")
    return flag

def new_href():
    # to judge if there is a new series of WestWorld
    time.sleep(2)
    if len(real_link) > len(temp_link):
        print('西部世界1080P有更新!')
        print('现在一共有 %d 集了。' %len(real_link))
        return True
    else:
        return False

def send_email(htm):
    # send email to notice new WestWorld is coming
    sender = 'xxxxx@163.com'
    receiver = 'xxxxx@qq.com,xxxxx@163.com'
    subject = '西部世界 1080P有更新！'
    smtpserver = 'smtp.163.com'
    username = 'xxxxx@163.com'
    password = 'xxxxx'
    msg = MIMEText(htm, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'UTF-8')
    msg['From'] = sender
    msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def new_download():
    # only download the new WestWorld series
    if len(real_link) > len(temp_link):
        # 2个地址数据的差集
        new_link = list(set(real_link).difference(set(temp_link)))
        for i in new_link:
            addTasktoXunlei(i, course_infos=None)



if __name__ == '__main__':
    # download the exiting series of WestWorld
    # send_email('最新更新磁链接：'+ str(real_link))
    for i in real_link:
        addTasktoXunlei(i, course_infos=None)

    # to get the later WestWorld for each hour
    while 1:
        if new_href():
            send_email('所有的下载地址（磁链接）：'+ str(real_link))
            new_download()
            time.sleep(15)
            # wait for an hour
            temp_link = real_link
            print(temp_link)
            print('神剧很好看吧，亲，耐心等下一集！~！')





