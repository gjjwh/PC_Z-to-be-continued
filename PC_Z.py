import wmi
from pynvml import *
import tkinter as tk

from tkinter import *
from PIL import  ImageTk
import os                      # os操作库
import pynvml


import math
true='可以'
false='不可以'
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)# 这里的0是GPU id
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)


nvmlInit()
deviceCount = nvmlDeviceGetCount()#几块显卡
w = wmi.WMI()

global list
list=[]

windows = Tk()
def info():

    for BIOSs in w.Win32_ComputerSystem():
        list.append("电脑名称: %s" %BIOSs.Caption)
        list.append("系统类型: %s" %BIOSs.SystemType)
    for address in w.Win32_NetworkAdapterConfiguration(ServiceName = "e1dexpress"):
        list.append("IP地址: %s" % address.IPAddress[0])
        list.append("MAC地址: %s" % address.MACAddress)
    for BIOS in w.Win32_baseboard():
        list.append("主板型号: %s" %BIOS.Product)
        list.append("主板制造商: %s" %BIOS.Manufacturer)
    for processor in w.Win32_Processor():
        list.append("CPU型号: %s" % processor.Name.strip())
        list.append("CPU当前速度: %s" % processor.CurrentClockSpeed)
    for memModule in w.Win32_PhysicalMemory():
        totalMemSize=int(memModule.Capacity)
        list.append("内存厂商: %s" %memModule.Manufacturer)
        list.append("内存大小: %.2fGB" %(totalMemSize/1024**3))
    for disk in w.Win32_DiskDrive(InterfaceType = "IDE"):
        diskSize=int(disk.size)
        list.append("磁盘型号: %s" %disk.Caption)
        list.append("磁盘大小: %.2fGB" %(diskSize/1024**3))
    for xk in w.Win32_VideoController():
        list.append("显卡名称: %s" %xk.name)
global gb
gb=[]
def start():
    for BIOS in w.Win32_baseboard():
        gb.append(" %s台式电脑" %BIOS.Product)
    for BIOSs in w.Win32_ComputerSystem():
        gb.append("系统位数: %s" %BIOSs.SystemType)
    for BIOSs in w.Win32_OperatingSystem():
        gb.append("系统版本: %s" %BIOSs.BuildNumber)

def main():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg3.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=650, image=bgImg)
    bg.pack()

    global path
    path= "c:/systeminfo"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames=BIOSs.Caption
    fileName=path+os.path.sep+UserNames+".txt"
    info()

    #判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        #创建文件夹（文件路径）
        os.makedirs(path)
        #写入文件信息
        for i in range(len(list)):
            fontPath = "./font/simhei.ttf"
            color = '#c37e00'
            baoc = tk.Label(window, text=(list[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=480, y=25 * (i + 10))
            baoc = tk.Label(window, text=(deviceCount), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 10))
            baoc.place(x=775, y=560)
            baoc = tk.Label(window, text=('您的显卡数量：'), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 10))
            baoc.place(x=680, y=560)
            color = '#CCCCFF'
            baoc = tk.Label(window, text=('做最好的小白守护者，这里的配置绝对真实，无法通过刷配置而改变'), bg=color, font=(fontPath, 10))
            baoc.place(x=900, y=630)
    else:
        print("存在")
        with open(fileName,'w+') as f:
            for i in range(len(list)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(list[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=480, y=25*(i+10))

                baoc = tk.Label(window, text=(deviceCount), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 10))
                baoc.place(x=855, y=530)
                baoc = tk.Label(window, text=('您的显卡数量：'), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 10))
                baoc.place(x=760, y=530)
                color = '#CCCCFF'
                baoc = tk.Label(window, text=('做最好的小白守护者，这里的配置绝对真实，无法通过刷配置而改变'), bg=color, font=(fontPath, 10))
                baoc.place(x=900, y=630)

    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(mn)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(mn[i]),backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 15))
            baoc.place(x=600, y=30 * (i + 3))

    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(mn)):
                fontPath = "./font/simhei.ttf"

                baoc = tk.Label(window, text=(mn[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 15))
                baoc.place(x=600, y=30 * (i + 3))

    vPath = "images/bb.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=179, height=45, command=main)
    v.place(x=950, y=120)

    cPath = "images/w.png"
    cImg = ImageTk.PhotoImage(file=cPath)
    c = tk.Button(window, image=cImg, bd=0, width=180, height=40, command=main)
    c.place(x=1110, y=200)

    gPath = "images/gpu.png"
    gImg = ImageTk.PhotoImage(file=gPath)
    g = tk.Button(window, image=gImg, bd=0,  width=180, height=40, command=gpu_print)
    g.place(x=1110, y=240)

    cPath = "images/cpu.png"
    cImg = ImageTk.PhotoImage(file=cPath)
    c = tk.Button(window, image=cImg, bd=0, width=180, height=40, command=cpu_print)
    c.place(x=1110, y=280)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)

    ypPath = "images/yp.png"
    ypImg = ImageTk.PhotoImage(file=ypPath)
    yp = tk.Button(window, image=ypImg, bd=0,  width=180, height=40, command=yp_print)
    yp.place(x=1110, y=320)

    ncPath = "images/nc.png"
    ncImg = ImageTk.PhotoImage(file=ncPath)
    nc = tk.Button(window, image=ncImg, bd=0,  width=180, height=40, command=nc_print)
    nc.place(x=1110, y=360)

    aPath = "images/zb.png"
    aImg = ImageTk.PhotoImage(file=aPath)
    a = tk.Button(window, image=aImg, bd=0,  width=180, height=40, command=zb_print)
    a.place(x=1110, y=400)
  
   




    window.mainloop()

global b
b=[]
def cpu():
    for processor in w.Win32_Processor():
        b.append("系统名称: %s" % processor.SystemName)
        b.append("CPU品牌: %s" % processor.Manufacturer)
        b.append("CPU架构: %s" % processor.AddressWidth)
        b.append("CPU系列: %s" % processor.OtherFamilyDescription)
        b.append("CPU型号: %s" % processor.Name.strip())
        b.append("CPU核心: %s" % processor.NumberOfCores)
        b.append("CPU线程: %s" % processor.NumberOfLogicalProcessors)
        b.append("CPU频率（MHz）: %s" % processor.CurrentClockSpeed)
        b.append("CPU数量: %s" % processor.UpgradeMethod)
        b.append("CPU编号: %s" % processor.PartNumber)
        b.append("该处理器支持Intel或AMD虚拟机监控器扩展: %s" % processor.VirtualizationFirmwareEnabled)
global ac
ac=[]
def cpu2():
    for processor in w.Win32_Processor():
        ac.append("CPU固件可以虚拟化扩展: %s" % processor.VMMonitorModeExtensions)
        ac.append("CPU可以超频: %s" % processor.PowerManagementSupported)
        ac.append("CPU是使用用户定义的配置: %s" % processor.ConfigManagerUserConfig)
        ac.append("处理器位数: %s" % processor.DataWidth)
        ac.append("处理器安装日期: %s" % processor.InstallDate)
        ac.append("处理器时钟频率（MHz）: %s" % processor.ExtClock)
        ac.append("处理器二级缓存（kb）: %s" % processor.L2CacheSize)
        ac.append("处理器二级缓存速度: %s" % processor.L2CacheSpeed)
        ac.append("处理器三级缓存（kb）: %s" % processor.L3CacheSize)
        ac.append("处理器三级缓存速度: %s" % processor.L3CacheSpeed)
        ac.append("芯片插座的线路上使用的类型: %s" % processor.SocketDesignation)
global cc
cc=[]
def cpu3():
     for processor in w.Win32_Processor():
        cc.append("CPU型号: %s" % processor.Name.strip())
        cc.append("CPU核心: %s" % processor.NumberOfCores)
        cc.append("CPU线程: %s" % processor.NumberOfLogicalProcessors)

def cpu_print():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg9.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=660, image=bgImg)
    bg.pack()
    global path
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    cpu()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(b)):
            fontPath = "./font/simhei.ttf"
            color = '#c37e00'
            baoc = tk.Label(window, text=(b[b]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=680, y=25*(i+10))

       
            baoc = tk.Label(window, text=(deviceCount), bg=color, font=(fontPath, 10))
            baoc.place(x=775, y=550)
            color = '#CCCCFF'
            baoc = tk.Label(window, text=('做最好的小白守护者，这里的配置绝对真实，无法通过刷配置而改变'), bg=color, font=(fontPath, 10))
            baoc.place(x=900, y=630)
    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(b)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(b[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=680, y=25*(i+10))
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    cpu2()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(ac)):
            fontPath = "./font/simhei.ttf"
            color = '#c37e00'
            baoc = tk.Label(window, text=(ac[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=380, y=25*(i+10))

    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(ac)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(ac[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=380, y=25*(i+10))

    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    cpu3()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(cc)):
            fontPath = "./font/simhei.ttf"
            color = '#c37e00'
            baoc = tk.Label(window, text=(cc[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=600, y=30 * (i + 3))

       
            baoc = tk.Label(window, text=(deviceCount), bg=color, font=(fontPath, 10))
            baoc.place(x=775, y=550)
            color = '#CCCCFF'
            baoc = tk.Label(window, text=('做最好的小白守护者，这里的配置绝对真实，无法通过刷配置而改变'), bg=color, font=(fontPath, 10))
            baoc.place(x=900, y=630)
    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(cc)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(cc[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=600, y=30 * (i + 3))

 
    vPath = "images/zh.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=180, height=40, command=main)
    v.place(x=1110, y=200)

    gPath = "images/gpu.png"
    gImg = ImageTk.PhotoImage(file=gPath)
    g = tk.Button(window, image=gImg, bd=0,  width=180, height=40, command=gpu_print)
    g.place(x=1110, y=240)

    cPath = "images/w.png"
    cImg = ImageTk.PhotoImage(file=cPath)
    c = tk.Button(window, image=cImg, bd=0, width=180, height=40, command=cpu_print)
    c.place(x=1110, y=280)

    ypPath = "images/yp.png"
    ypImg = ImageTk.PhotoImage(file=ypPath)
    yp = tk.Button(window, image=ypImg, bd=0,  width=180, height=40, command=yp_print)
    yp.place(x=1110, y=320)

    ncPath = "images/nc.png"
    ncImg = ImageTk.PhotoImage(file=ncPath)
    nc = tk.Button(window, image=ncImg, bd=0,  width=180, height=40, command=nc_print)
    nc.place(x=1110, y=360)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)

    aPath = "images/zb.png"
    aImg = ImageTk.PhotoImage(file=aPath)
    a = tk.Button(window, image=aImg, bd=0,  width=180, height=40, command=zb_print)
    a.place(x=1110, y=400)
  
    window.mainloop()
def st():
    global window
    window = tk.Toplevel()
    window.geometry('300x550')
    window.resizable(0, 0)
    window.title('启动界面')
    bgPath = "./images/img0.jpg"
    bgImg = ImageTk.PhotoImage(file=bgPath)
    bg = tk.Label(window, width=1000, height=600, image=bgImg)
    bg.pack()
    startPath = "./images/start.png"
    startImg = ImageTk.PhotoImage(file=startPath)
    start = tk.Button(window, image=startImg, bd=2, width=150, height=55,relief=RIDGE,
                      command=start_print)
    start.place(x=80, y=400)
    f = tk.Frame(window, height=64, width=64)
    f.pack_propagate(0)
    f.pack()
    b = tk.Button( text="联系我们", command=qq)
    b.pack(fill="both", expand=1)

    f = tk.Frame(window, height=64, width=64)
    f.pack_propagate(0)
    f.pack()

    c = tk.Button(text='软件介绍', command=st)
    c.pack(fill="both", expand=1)
    c = tk.Button(text='检查更新', command=st)
    c.pack(fill="both", expand=1)
    fontPath = "./font/simhei.ttf"
    color='#6699ff'
    sss = tk.Label(window, text='PC_Z评测', bg=color, font=(fontPath, 50))
    sss.place(x=10, y=20)
    color = '#66ccff'
    a = tk.Label(window, text='版本：0.01(刷新配置请重新打开软件）', bg=color, font=(fontPath, 9))
    a.place(x=0, y=520)
    color = '#CCCCFF'
    baoc = tk.Label(window, text=('读取电脑配置需要一段时间，请耐心等待'), bg=color, font=(fontPath, 10))
    baoc.place(x=0, y=599)

    window.mainloop()
def qq():
    webbrowser.open("https://qm.qq.com/cgi-bin/qm/qr?k=ltSddyV1Y5TTW6EFG10nYLtSdWQRpHGH&jump_from=webapi")
    window.mainloop()
global ddd
ddd=[]
def gpu():
    for xk in w.Win32_VideoController():
        ddd.append("显卡名称: %s" %xk.name)
        ddd.append("显卡安装日期: %s" % xk.InstallDate)
        ddd.append("显卡驱动程序版本号: %s" % xk.DriverVersion)
        ddd.append("显示屏刷新率: %s" % xk.MaxRefreshRate)
        ddd.append("显卡上一个错误代码: %s" % xk.LastErrorCode)
        ddd.append("显卡当前分辨率: %s" % xk.VideoModeDescription)
        ddd.append("显卡最后一次复位日期（初始化）: %s" % xk.TimeOfLastReset)
        ddd.append("显卡识别符: %s" % xk.PNPDeviceID)
        ddd.append("在当前的分辨率支持的色彩数目: %s" % xk.CurrentNumberOfColors)
        ddd.append("此视频控制器列（如果在字符模式下）编号: %s" % xk.CurrentNumberOfColumns)
global qw
qw=[]
def gpu2():
    for xk in w.Win32_VideoController():
        qw.append("显卡名称: %s" %xk.name)
        qw.append("显卡当前分辨率: %s" % xk.VideoModeDescription)
def gpu_print():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg4.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=660, image=bgImg)
    bg.pack()
    global path
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    gpu()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(ddd)):
            fontPath = "./font/simhei.ttf"
            color = '#c37e00'
            baoc = tk.Label(window, text=(ddd[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=480, y=25*(i+10))


            baoc = tk.Label(window, text='显存信息（字节）：', backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 19))
            baoc.place(x=350, y=110)

            baoc = tk.Label(window, text=(meminfo.total), bg=color, font=(fontPath, 19))
            baoc.place(x=550, y=100)

            baoc = tk.Label(window, text=(deviceCount), bg=color, font=(fontPath, 10))
            baoc.place(x=775, y=550)

    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(ddd)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(ddd[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=480, y=25*(i+10))

                color = '#c37e00'
                baoc = tk.Label(window, text='显存信息(G)：', backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=640, y=500)

                baoc = tk.Label(window, text=(meminfo.total /1024**3), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=720, y=500)

    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    gpu2()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(qw)):
            fontPath = "./font/simhei.ttf"
            color = '#c37e00'
            baoc = tk.Label(window, text=(qw[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=600, y=30 * (i + 3))


    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(qw)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(qw[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=600, y=30 * (i + 3))

    vPath = "images/zh.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=180, height=40, command=main)
    v.place(x=1110, y=200)

    gPath = "images/w.png"
    gImg = ImageTk.PhotoImage(file=gPath)
    g = tk.Button(window, image=gImg, bd=0,  width=180, height=40, command=gpu_print)
    g.place(x=1110, y=240)

    cPath = "images/cpu.png"
    cImg = ImageTk.PhotoImage(file=cPath)
    c = tk.Button(window, image=cImg, bd=0, width=180, height=40, command=cpu_print)
    c.place(x=1110, y=280)

    ypPath = "images/yp.png"
    ypImg = ImageTk.PhotoImage(file=ypPath)
    yp = tk.Button(window, image=ypImg, bd=0,  width=180, height=40, command=yp_print)
    yp.place(x=1110, y=320)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)

    ncPath = "images/nc.png"
    ncImg = ImageTk.PhotoImage(file=ncPath)
    nc = tk.Button(window, image=ncImg, bd=0,  width=180, height=40, command=nc_print)
    nc.place(x=1110, y=360)

    aPath = "images/zb.png"
    aImg = ImageTk.PhotoImage(file=aPath)
    a = tk.Button(window, image=aImg, bd=0,  width=180, height=40, command=zb_print)
    a.place(x=1110, y=400)
  
    window.mainloop()


  
global qqq
qqq=[]
def vc():
    for disk in w.Win32_DiskDrive(InterfaceType = "IDE"):
        diskSize=int(disk.size)
        qqq.append("磁盘序列号: %s" %disk.Caption)
        qqq.append("磁盘大小: %.2fGB" %(diskSize/1024**3))
        qqq.append("盘驱动器的SCSI总线号: %s" % disk.SCSIBus)

        qqq.append("物理磁盘驱动器上柱面总数: %s" % disk.TotalCylinders )
        qqq.append("磁盘驱动器上磁头总数: %s" % disk.TotalHeads)
        qqq.append("物理磁盘驱动器上的扇区总数: %s" % disk.TotalSectors)

global er
er=[]
def vc2():
    for disk in w.Win32_DiskDrive(InterfaceType = "IDE"):
        diskSize=int(disk.size)
        er.append("磁盘型号: %s" %disk.Caption)


def yp_print():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg7.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=660, image=bgImg)
    bg.pack()
    global path
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    vc()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(qqq)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(qqq[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=480, y=25*(i+7))

    
    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(qqq)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(qqq[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=600, y=30 * (i + 7))

      
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    vc2()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(er)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(er[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=480, y=25*(i+1))

    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(er)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(er[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=600, y=30 * (i + 3))

             
    vPath = "images/zh.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=180, height=40, command=main)
    v.place(x=1110, y=200)

    gPath = "images/gpu.png"
    gImg = ImageTk.PhotoImage(file=gPath)
    g = tk.Button(window, image=gImg, bd=0,  width=180, height=40, command=gpu_print)
    g.place(x=1110, y=240)

    cPath = "images/cpu.png"
    cImg = ImageTk.PhotoImage(file=cPath)
    c = tk.Button(window, image=cImg, bd=0, width=180, height=40, command=cpu_print)
    c.place(x=1110, y=280)

    ypPath = "images/w.png"
    ypImg = ImageTk.PhotoImage(file=ypPath)
    yp = tk.Button(window, image=ypImg, bd=0,  width=180, height=40, command=yp_print)
    yp.place(x=1110, y=320)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)

    ncPath = "images/nc.png"
    ncImg = ImageTk.PhotoImage(file=ncPath)
    nc = tk.Button(window, image=ncImg, bd=0,  width=180, height=40, command=nc_print)
    nc.place(x=1110, y=360)

    aPath = "images/zb.png"
    aImg = ImageTk.PhotoImage(file=aPath)
    a = tk.Button(window, image=aImg, bd=0,  width=180, height=40, command=zb_print)
    a.place(x=1110, y=400)
  
    window.mainloop()

global aaa
aaa=[]
def nnc():
    for memModule in w.Win32_PhysicalMemory():
        totalMemSize=int(memModule.Capacity)
        aaa.append("内存厂商: %s" %memModule.Manufacturer)
        aaa.append("内存大小: %.2fGB" %(totalMemSize/1024**3))
        aaa.append("内存类型: %s" %memModule.Caption)
        aaa.append("内存电压（MHz）: %s" %memModule.MaxVoltage)
        aaa.append("标的频率: %s" %memModule.Speed)


global lk
lk=[]
def lc():
    for memModule in w.Win32_PhysicalMemory():
        totalMemSize=int(memModule.Capacity)
        lk.append("是否支持热插拔: %s" %memModule.HotSwappable)
        lk.append("内存带宽: %s" %memModule.DataWidth)
        lk.append("内存编号: %s" %memModule.SerialNumber)
        lk.append("内存总宽: %s" %memModule.TotalWidth)
        lk.append("设备定位器: %s" %memModule.DeviceLocator)
        lk.append("零件编号: %s" %memModule.PositionInRow)

global ad
ad=[]
def add():
    for memModule in w.Win32_PhysicalMemory():
        totalMemSize=int(memModule.Capacity)
        ad.append("内存厂商: %s" %memModule.Manufacturer)
global rt
rt=[]
def tt():
    for memModule in w.Win32_PhysicalMemory():
        totalMemSize=int(memModule.Capacity)
        rt.append("内存大小: %.2fGB" %(totalMemSize/1024**3))
def nc_print():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg5.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=660, image=bgImg)
    bg.pack()
    global path
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    nnc()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(aaa)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(aaa[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=380, y=25*(i+10))

    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(aaa)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(aaa[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=380, y=25*(i+10))

    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    lc()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(lk)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(lk[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=680, y=25*(i+10))

    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(lk)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(lk[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=680, y=25*(i+10))



 
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    add()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(ad)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(ad[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=600, y=30 * (i + 2))
    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(ad)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(ad[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=600, y=30 * (i + 2))


    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    tt()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(rt)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(rt[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=800, y=30 * (i + 2))
    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(rt)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(rt[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=800, y=30 * (i + 2))

                baoc = tk.Label(window, text='提示：信息一次重复就是一个内存的信息，内存信息请横向配对。例如.如果你有两根内存，左边一行上面的信息和右边一行上面的信息就是第一根内存条的信息，第二根内存条原理相同', backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=0, y=600)

          
    vPath = "images/zh.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=180, height=40, command=main)
    v.place(x=1110, y=200)

    gPath = "images/gpu.png"
    gImg = ImageTk.PhotoImage(file=gPath)
    g = tk.Button(window, image=gImg, bd=0,  width=180, height=40, command=gpu_print)
    g.place(x=1110, y=240)

    cPath = "images/cpu.png"
    cImg = ImageTk.PhotoImage(file=cPath)
    c = tk.Button(window, image=cImg, bd=0, width=180, height=40, command=cpu_print)
    c.place(x=1110, y=280)

    ypPath = "images/yp.png"
    ypImg = ImageTk.PhotoImage(file=ypPath)
    yp = tk.Button(window, image=ypImg, bd=0,  width=180, height=40, command=yp_print)
    yp.place(x=1110, y=320)

    ncPath = "images/w.png"
    ncImg = ImageTk.PhotoImage(file=ncPath)
    nc = tk.Button(window, image=ncImg, bd=0,  width=180, height=40, command=nc_print)
    nc.place(x=1110, y=360)

    aPath = "images/zb.png"
    aImg = ImageTk.PhotoImage(file=aPath)
    a = tk.Button(window, image=aImg, bd=0,  width=180, height=40, command=zb_print)
    a.place(x=1110, y=400)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)
  
    window.mainloop()
global mn
mn=[]
def start():
    for BIOS in w.Win32_baseboard():
        mn.append(" %s台式电脑" %BIOS.Product)
    for BIOSs in w.Win32_ComputerSystem():
        mn.append("系统位数: %s" %BIOSs.SystemType)
    for BIOSs in w.Win32_OperatingSystem():
        mn.append("系统版本: %s" %BIOSs.BuildNumber)

def start_print():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg2.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=660, image=bgImg)
    bg.pack()
    global path
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    start()#传参

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(mn)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(mn[i]),backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 15))
            baoc.place(x=600, y=30 * (i + 3))

    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(mn)):
                fontPath = "./font/simhei.ttf"

                baoc = tk.Label(window, text=(mn[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 20))
                baoc.place(x=600, y=30 * (i + 3))

    vPath = "images/bb.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=179, height=45, command=main)
    v.place(x=950, y=120)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)

    
    
    window.mainloop()
def xcx():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg1.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=660, image=bgImg)
    bg.pack()

    dpPath = "images/u.jpg"
    dpImg = ImageTk.PhotoImage(file=dpPath)
    dp = tk.Button(window, image=dpImg, bd=0, width=360, height=221, command=xncs)#把这个改成你写的性能评测就可以了，iand
    dp.place(x=330, y=50)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)
    window.mainloop()

    
global az
az=[]
def zb():
        for BIOS in w.Win32_baseboard():
            az.append("主板型号: %s" %BIOS.Product)
            az.append("主板制造商: %s" %BIOS.Manufacturer)
            az.append("主板描述: %s" %BIOS.Caption)
            az.append("主板序列号: %s" %BIOS.SerialNumber)
            az.append("描述插槽位置: %s" %BIOS.SlotLayout)
        for BIOS in w.Win32_BIOS():
            az.append("bios序列号: %s" %BIOS.SerialNumber.strip)
global wq
wq=[]
def we():
        for BIOS in w.Win32_baseboard():
            wq.append("主板型号: %s" %BIOS.Product)
            wq.append("主板制造商: %s" %BIOS.Manufacturer)
def zb_print():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bg6.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=660, image=bgImg)
    bg.pack()
    global path
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    zb()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(az)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(az[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=480, y=25*(i+10))
            baoc = tk.Label(window, text=('错误代码None表示读取失败，表示没有错误'), bg=color, font=(fontPath, 10))
            baoc.place(x=900, y=570)
    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(az)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(az[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=480, y=25*(i+10))
    path = "other"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames = BIOSs.Caption
    fileName = path + os.path.sep + UserNames + ".txt"
    we()

    # 判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        # 创建文件夹（文件路径）
        os.makedirs(path)
        # 写入文件信息
        for i in range(len(wq)):
            fontPath = "./font/simhei.ttf"
            baoc = tk.Label(window, text=(wq[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
            baoc.place(x=480, y=25*(i+10))
            baoc = tk.Label(window, text=('错误代码None表示读取失败，表示没有错误'), bg=color, font=(fontPath, 10))
            baoc.place(x=600, y=30 * (i + 3))
    else:
        print("存在")
        with open(fileName, 'w+') as f:
            for i in range(len(wq)):
                fontPath = "./font/simhei.ttf"
                color = '#c37e00'
                baoc = tk.Label(window, text=(wq[i]), backgroun="#1f1f1f", foreground="#FFFFFF", font=(fontPath, 12))
                baoc.place(x=600, y=30 * (i + 3))

    vPath = "images/zh.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=180, height=40, command=main)
    v.place(x=1110, y=200)

    gPath = "images/gpu.png"
    gImg = ImageTk.PhotoImage(file=gPath)
    g = tk.Button(window, image=gImg, bd=0,  width=180, height=40, command=gpu_print)
    g.place(x=1110, y=240)

    cPath = "images/cpu.png"
    cImg = ImageTk.PhotoImage(file=cPath)
    c = tk.Button(window, image=cImg, bd=0, width=180, height=40, command=cpu_print)
    c.place(x=1110, y=280)

    ypPath = "images/yp.png"
    ypImg = ImageTk.PhotoImage(file=ypPath)
    yp = tk.Button(window, image=ypImg, bd=0,  width=180, height=40, command=yp_print)
    yp.place(x=1110, y=320)

    ncPath = "images/nc.png"
    ncImg = ImageTk.PhotoImage(file=ncPath)
    nc = tk.Button(window, image=ncImg, bd=0,  width=180, height=40, command=nc_print)
    nc.place(x=1110, y=360)

    aPath = "images/w.png"
    aImg = ImageTk.PhotoImage(file=aPath)
    a = tk.Button(window, image=aImg, bd=0,  width=180, height=40, command=zb_print)
    a.place(x=1110, y=400)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)
  
    window.mainloop()

def xncs():
    global window
    window.destroy()
    window = tk.Toplevel()
    window.geometry('1300x650')
    window.resizable(0, 0)
    # 设置标题
    window.title('PC_Z')
    # 设置背景图片的路径
    bgPath = "./images/bgc.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1300, height=650, image=bgImg)
    bg.pack()
    vPath = "images/bt1.png"
    vImg = ImageTk.PhotoImage(file=vPath)
    v = tk.Button(window, image=vImg, bd=0, width=175, height=46, command=st)
    v.place(x=370, y=500)

    qPath = "images/pc.png"
    qImg = ImageTk.PhotoImage(file=qPath)
    q = tk.Button(window, image=qImg, bd=0, width=170, height=41, command=xncs)#把这个改成你写的性能评测就可以了，iand
    q.place(x=30, y=140)

    sPath = "images/bt2.jpg"
    sImg = ImageTk.PhotoImage(file=sPath)
    s = tk.Button(window, image=sImg, bd=0, width=170, height=41, command=start_print)#把这个改成你写的性能评测就可以了，iand
    s.place(x=16, y=190)

    dPath = "images/bt3.jpg"
    dImg = ImageTk.PhotoImage(file=dPath)
    d = tk.Button(window, image=dImg, bd=0, width=170, height=41, command=xcx)#把这个改成你写的性能评测就可以了，iand
    d.place(x=16, y=240)


    kPath = "images/bt00.jpg"
    kImg = ImageTk.PhotoImage(file=kPath)
    k = tk.Button(window, image=kImg, bd=0, width=58, height=22, command=xncs)#把这个改成你写的性能评测就可以了，iand
    k.place(x=425, y=30)

    fontPath = "./font/simhei.ttf"
    baoc = tk.Label(window, text='评测需要一段时间（2分钟左右）,请耐心等待，不要关闭弹出的小窗口', backgroun="#1f1f1f", foreground="#0396ff", font=(fontPath, 19))
    baoc.place(x=375, y=630)
    window.mainloop()



st()
