import os
import sys
import random
from multiprocessing import cpu_count
from multiprocessing import Process
import hashlib
import time
from io import StringIO
from pyray.shapes.cube import *

#CPU测试

def ranstr(num):
    rans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(num):
        salt += random.choice(rans)
    return salt
cpucore = cpu_count()
#cpu单核测试
def cputest():
    for i in range(1000000):
        ran = ranstr(7)
        ran = str(ran)
        ran = ran.encode('utf8')
        md5hash = hashlib.md5(ran)
        md5 = md5hash.hexdigest()
#cpu多核测试
def mcputest():
    p_lst = []
    for i in range(cpucore):
        p = Process(target = cputest)
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()
#硬盘测试
def disktest(size):
    f = open('D:\\test.txt','w')
    for j in range(size):
        for i in range(1024):
            f.write('01'*1024)
    f.close()
#内存测试
def ramtest(size):
    f = StringIO()
    for j in range(size):
        for i in range(1024):
            f.write('01'*512)
    f.close()
#单核测试
time_start = time.time()
cputest()
time_end = time.time()   
time_sum = time_end - time_start
time_sum = round(time_sum,3)
time_sum = time_sum * 1000
time_sum = int(time_sum)
time_sum = str(time_sum)
print(time_sum)
#多核测试
time_start = time.time()
mcputest()
time_end = time.time()
time_msum = time_end - time_start
time_msum = round(time_msum,3)
time_msum = time_msum * 1000
time_msum = int(time_msum)
time_msum = str(time_msum)
print(time_msum)
time_sum = int(time_sum)
time_msum = int(time_msum)
cpuscore = time_sum + time_msum
cpuscore = int(cpuscore)
cpuscore = str(cpuscore)
#硬盘测试
dtimes = time.time()
disktest(2048)
dtimee = time.time()
dtimes = round(dtimes,3)
dtimes = dtimes * 1000
dtimee = round(dtimee,3)
dtimee = dtimee * 1000
dtimes = int(dtimes)
dtimee = int(dtimee)
diskscore = dtimee - dtimes
diskscore = str(diskscore)
os.remove('D:\\test.txt')
#内存测试
rtimes = time.time()
ramtest(2048)
rtimee = time.time()
rtimes = round(rtimes,3)
rtimes = rtimes * 1000
rtimee = round(rtimee,3)
rtimee = rtimee * 1000
rtimes = int(rtimes)
rtimee = int(rtimee)
ramscore = rtimee - rtimes
ramscore = str(ramscore)
f = open('score.txt','w')

f.write(cpuscore+'\n')
f.write(ramscore+'\n')
f.write(diskscore+'\n')
f.close()