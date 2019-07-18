import os
import datetime
import win32api
import win32clipboard
import win32gui
import win32con
import time
import ctypes
from PIL import ImageGrab
import aircv as ac
import win32clipboard as wincld
import webbrowser
import subprocess
import sys,os,subprocess,commands
from subprocess import Popen,PIPE


#对比两张图，找到坐标。
def matchImg(imgsrc, imgobj):  # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj, 0.9)  #0.9、confidence是精度，越小对比的精度就越低 {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    return match_result

def manyclick():
    # 这里是在点击屏幕固定区域采集能量
    for myx in range(220, 804, 50):
        for myy in range(400, 736, 50):
            myxstr = str(myx)
            myystr = str(myy)
            os.popen('adb -s 66819679 shell input tap ' + myxstr + ' '+ myystr, 'r', 1)
            # print(myxstr +' , '+myystr)
            time.sleep(0.1)
    print("get g")
    # 点击左下一点
    os.popen('adb -s 66819679 shell input tap 259 946', 'r', 1)
    time.sleep(0.1)
    # 点击右下一点
    os.popen('adb -s 66819679 shell input tap 883 774', 'r', 1)
    time.sleep(0.1)
    # 点击右下一点
    os.popen('adb -s 66819679 shell input tap 883 890', 'r', 1)
    time.sleep(0.1)
    # 返回
    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
    time.sleep(1)

#打开支付宝蚂蚁森林操作
def openalipay():
    # 返回
    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
    time.sleep(0.3)
    # 返回
    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
    time.sleep(0.3)
    # 返回
    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
    time.sleep(0.3)
    # 去点击
    os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
    time.sleep(1)
    # 打开alipay
    os.popen('adb -s 66819679 shell input tap 135 250', 'r', 1)
    time.sleep(1)
    # 首页
    os.popen('adb -s 66819679 shell input tap 108 2222', 'r', 1)
    time.sleep(1)
    # 向下滑动
    os.popen('adb -s 66819679 shell input swipe 520 300 520 1000')
    time.sleep(1)
    # 打开蚂蚁
    os.popen('adb -s 66819679 shell input tap 410 662', 'r', 1)
    time.sleep(1)
    #采集
    manyclick()
    # 打开蚂蚁
    os.popen('adb -s 66819679 shell input tap 410 662', 'r', 1)
    time.sleep(1)

# 截图
def screencap():
    # 截图
    os.popen('adb -s 66819679 shell screencap -p /storage/emulated/0/Documents/phoneScreencap.png')
    time.sleep(1.5)
    #发送到电脑
    os.popen('adb -s 66819679 pull /storage/emulated/0/Documents/phoneScreencap.png')
    time.sleep(1.5)

#主函数
def main(h=0, m=0):

    openalipay()

    def doit():
        # 截图
        screencap()

        # alipay_friend
        if matchImg('phoneScreencap.png', 'alipay_friend.png') != None:
            print("alipay_friend！" + str(
                matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0]) + ',' + str(
                matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1]))
            myx = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0])
            myy = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1])
            os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
            time.sleep(3)
            print("manyclick")
            manyclick()
            # 截图
            screencap()

        # alipay_hui给特定的好友浇水，根据头像判断
        if matchImg('phoneScreencap.png', 'alipay_hui.png') != None:
            print("alipay_hui！" + str(
                matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][0]) + ',' + str(
                matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][1]))
            myx = str(matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][0])
            myy = str(matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][1])
            os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
            time.sleep(4)
            print("water")
            os.popen('adb -s 66819679 shell input tap 1000 1500', 'r', 1)
            time.sleep(3)
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(2)

        #alipay_lookForMoreFriends查找更多好友
        if matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png') != None:
            print("alipay_lookForMoreFriends！" + str(matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][0]) +','+ str(
                matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][1]))
            myx = str(matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][0])
            myy = str(matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][1])
            os.popen('adb -s 66819679 shell input tap '+myx+' '+myy, 'r', 1)
            time.sleep(1)
            # 截图
            screencap()
            # alipay_friend
            if matchImg('phoneScreencap.png', 'alipay_friend.png') != None:
                print("alipay_friend！" + str(
                    matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 截图
                screencap()

                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(2)

        #滑动
        os.popen('adb -s 66819679 shell input swipe  520 1000 520 600')
        time.sleep(0.1)

        # alipay_nomore到底部了，得从头开始
        if matchImg('phoneScreencap.png', 'alipay_nomore.png') != None:
            print("alipay_nomore！" + str(
                matchImg('phoneScreencap.png', 'alipay_nomore.png')['result'][0]) + ',' + str(
                matchImg('phoneScreencap.png', 'alipay_nomore.png')['result'][1]))
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            openalipay()

        # alipay_love因为网络等问题，如果出现这alipay_love图标就得从头再来。
        if matchImg('phoneScreencap.png', 'alipay_love.png') != None:
            print("alipay_love！" + str(
                matchImg('phoneScreencap.png', 'alipay_love.png')['result'][0]) + ',' + str(
                matchImg('phoneScreencap.png', 'alipay_love.png')['result'][1]))
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            # 返回
            os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            time.sleep(0.3)
            openalipay()


    i = 0
    while 1 == 1:
        i = i + 1
        doit()
        time.sleep(1)
        print("已经滚动" + str(i) + "次。")

main()

