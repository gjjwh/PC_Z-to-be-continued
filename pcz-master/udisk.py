from urllib.request import AbstractDigestAuthHandler
from psutil import disk_partitions
import time
import tkinter as tk

while True:
    find = tk.Tk()
    find.geometry('200x200')
    time.sleep(0.5)
    for item in disk_partitions():
        disk = str(disk_partitions())
        if 'removable' in disk:
            driver,opts = item.device,item.opts
            break
        else:
            tk.Label(find,text='未找到u盘',font=('Arial',20)).pack()
            find.mainloop()
            continue

cishu = 0  #已检测大小，单位kb

while True:
    try:
        f = open(driver+'test.txt','w')
        f.write('01'*512)
        f.close()
        cishu += 1
    except:
        real = tk.Tk()
        real.geometry('200x200')
        tk.Label(real,text='真实容量为：'+cishu+'kb',font=('Arial',20)).pack()
        real.mainloop()