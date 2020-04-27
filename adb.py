import datetime
import time
import aircv as ac
import os
import random


# 主函数
def main():
    firsttime = 1

    # 对比两张图，找到坐标。
    def matchImg(imgsrc, imgobj):  # imgsrc=原始图像，imgobj=待查找的图片
        imsrc = ac.imread(imgsrc)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj,
                                        0.9)
        # 0.9、confidence是精度，越小对比的精度就越低 {'confidence': 0.5435812473297119,
        # 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.alipay_leave0)}
        if match_result is not None:
            match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
        return match_result

    # 返回好多次，保证能完全退出软件。
    def backback():
        # 返回
        print("返回backback")
        r = os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        print(r)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)

    def manyclick():
        # 这里是在点击屏幕固定区域采集能量
        for myx in range(229, 804, 50):
            for myy in range(439, 736, 50):
                myxstr = str(myx)
                myystr = str(myy)
                os.popen('adb -s 66819679 shell input tap ' + myxstr + ' ' + myystr, 'r', 1)
                # print(myxstr +' , '+myystr)
                time.sleep(0.05)
        print("get g")
        # 点击左下一点
        os.popen('adb -s 66819679 shell input tap 259 946', 'r', 1)
        time.sleep(0.1)
        # 点击右下一点
        os.popen('adb -s 66819679 shell input tap 883 774', 'r', 1)
        time.sleep(0.1)
        # 点击右下一点
        os.popen('adb -s 66819679 shell input tap 883 890', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(4)

    # 打开支付宝蚂蚁森林操作
    def openalipay():
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 去点击
        os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
        time.sleep(2)
        # 打开alipay
        os.popen('adb -s 66819679 shell input tap 135 250', 'r', 1)
        time.sleep(4)
        # 首页
        os.popen('adb -s 66819679 shell input tap 108 2222', 'r', 1)
        time.sleep(4)
        # 向下滑动
        os.popen('adb -s 66819679 shell input swipe 520 300 520 1000')
        time.sleep(7)
        # 打开蚂蚁

        # 打开蚂蚁
        # 截图
        screencap()
        try:
            # alipay_friend
            if matchImg('phoneScreencap.png', 'antIcon.png') is not None:
                print("antIcon！" + str(
                    matchImg('phoneScreencap.png', 'antIcon.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'antIcon.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'antIcon.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'antIcon.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                # 采集
                manyclick()
                time.sleep(4)
                print("打开蚂蚁")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)

        except Exception as e:
            print(e)
            print("这里有个异常")

    # 截图
    def screencap():
        try:
            # 截图
            os.popen('adb -s 66819679 shell screencap -p /storage/emulated/0/Pictures/Screenshots/phoneScreencap.png')
            time.sleep(3)
            print("截图")
            # 发送到电脑
            os.popen('adb -s 66819679 pull /storage/emulated/0/Pictures/Screenshots/phoneScreencap.png')
            time.sleep(5)
        except Exception as e:
            print(e)
            print("这里有个异常adb -s 66819679 shell screencap")

    def doit():
        print("doit")
        # 截图
        screencap()

        try:
            # alipay_friend
            if matchImg('phoneScreencap.png', 'alipay_friend.png') is not None:
                print("alipay_friend！" + str(
                    matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                print("manyclick")
                manyclick()
            elif matchImg('phoneScreencap.png', 'install.png') is not None:
                print("install！" + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'install.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'install.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)
                return

            # time.sleep(2)
            # 截图
            # screencap()
            # alipay_help
            if matchImg('phoneScreencap.png', 'alipay_help.png') is not None:
                print("alipay_help！" + str(
                    matchImg('phoneScreencap.png', 'alipay_help.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_help.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_help.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_help.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                print("manyclick,alipay_help")
                manyclick()

            mytime = datetime.datetime.now()
            if mytime.hour == 7 and mytime.minute <= 15:
                # 截图
                screencap()
                # alipay_hui给特定的好友浇水，根据头像判断
                if matchImg('phoneScreencap.png', 'alipay_hui.png') is not None:
                    print("alipay_hui！" + str(
                        matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(4)
                    screencap()
                    print("water")
                    if matchImg('phoneScreencap.png', 'alipay_water.png') is not None:
                        print("alipay_water！" + str(
                            matchImg('phoneScreencap.png', 'alipay_water.png')['result'][0]) + ',' + str(
                            matchImg('phoneScreencap.png', 'alipay_water.png')['result'][1]))
                        myx = str(matchImg('phoneScreencap.png', 'alipay_water.png')['result'][0])
                        myy = str(matchImg('phoneScreencap.png', 'alipay_water.png')['result'][1])
                        os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                        time.sleep(4)
                        screencap()
                    if matchImg('phoneScreencap.png', 'alipay_water_confirm.png') is not None:
                        print("alipay_water_confirm！" + str(
                            matchImg('phoneScreencap.png', 'alipay_water_confirm.png')['result'][0]) + ',' + str(
                            matchImg('phoneScreencap.png', 'alipay_water_confirm.png')['result'][1]))
                        myx = str(matchImg('phoneScreencap.png', 'alipay_water_confirm.png')['result'][0])
                        myy = str(matchImg('phoneScreencap.png', 'alipay_water_confirm.png')['result'][1])
                        os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                        time.sleep(4)
                    time.sleep(4)
                    # 返回
                    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                    time.sleep(3)

            # time.sleep(2)
            # 截图
            # screencap()
            # alipay_lookForMoreFriends查找更多好友
            if matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png') is not None:
                print("alipay_lookForMoreFriends！" + str(
                    matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(2)
                # 截图
                screencap()
                # # alipay_friend
                # if matchImg('phoneScreencap.png', 'alipay_friend.png') is not None:
                #     print("alipay_friend！" + str(
                #         matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0]) + ',' + str(
                #         matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1]))
                #     myx = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0])
                #     myy = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1])
                #     os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                #     time.sleep(4)
                #     # 截图
                #     screencap()
                #
                #     # 返回
                #     os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                #     time.sleep(3)

            # 滑动
            os.popen('adb -s 66819679 shell input swipe  520 1300 520 200')
            time.sleep(3)

            # 截图
            screencap()

            # alipay_nomore到底部了，得从头开始
            if matchImg('phoneScreencap.png', 'alipay_nomore.png') is not None:
                print("alipay_nomore！" + str(
                    matchImg('phoneScreencap.png', 'alipay_nomore.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_nomore.png')['result'][1]))
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)
                openalipay()

            # # alipay_love因为网络等问题，如果出现这alipay_love图标就得从头再来。
            # if matchImg('phoneScreencap.png', 'alipay_love.png') is not None:
            #     print("alipay_love！" + str(
            #         matchImg('phoneScreencap.png', 'alipay_love.png')['result'][0]) + ',' + str(
            #         matchImg('phoneScreencap.png', 'alipay_love.png')['result'][1]))
            #     # 返回
            #     os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            #     time.sleep(0.7)
            #     # 返回
            #     os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            #     time.sleep(0.7)
            #     # 返回
            #     os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            #     time.sleep(0.7)
            #     # 返回
            #     os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
            #     time.sleep(0.7)
            #     openalipay()

            # 从头再来。
            if matchImg('phoneScreencap.png', 'bottom.png') is not None:
                print("bottom！" + str(
                    matchImg('phoneScreencap.png', 'bottom.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'bottom.png')['result'][1]))
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)
                openalipay()

            # 返回即可
            if matchImg('phoneScreencap.png', 'alipay_no.png') is not None:
                print("alipay_no！" + str(
                    matchImg('phoneScreencap.png', 'alipay_no.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_no.png')['result'][1]))
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)

            # 1212活动界面返回即可
            if matchImg('phoneScreencap.png', 'alipay_leave.png') is not None:
                print("alipay_leave！" + str(
                    matchImg('phoneScreencap.png', 'alipay_leave.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_leave.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_leave.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_leave.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(2)
                # 返回
                # os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                # time.sleep(2)
                # # 返回
                # os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                # time.sleep(2)

            # 指纹界面
            if matchImg('phoneScreencap.png', 'alipay_c.png') is not None:
                print("alipay_c.png！" + str(
                    matchImg('phoneScreencap.png', 'alipay_c.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_c.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_c.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_c.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(2)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(2)
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)
                openalipay()


        except Exception as e:
            print(e)
            print("这里有个异常")

    # 刷宝
    def shuabao():
        os.popen('adb -s 66819679 shell input tap 100 2222', 'r', 1)
        mytime = random.uniform(5.0, 15.0)
        print("see time : " + str(mytime))
        time.sleep(mytime)
        # 截图
        screencap()
        try:
            # 窗口1
            if matchImg('phoneScreencap.png', 'fuli1.png') is not None:
                print("fuli1！" + str(
                    matchImg('phoneScreencap.png', 'fuli1.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli1.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli1.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli1.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                print("fuli1")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') is not None:
                    print("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close1")
                if matchImg('phoneScreencap.png', 'close2.png') is not None:
                    print("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close2")

            if matchImg('phoneScreencap.png', 'install.png') is not None:
                print("install！" + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'install.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'install.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)
                return
            # 窗口2
            if matchImg('phoneScreencap.png', 'fuli2.png') is not None:
                print("fuli2！" + str(
                    matchImg('phoneScreencap.png', 'fuli2.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli2.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli2.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli2.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                print("fuli2")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') is not None:
                    print("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close1")
                if matchImg('phoneScreencap.png', 'close2.png') is not None:
                    print("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close2")

            if matchImg('phoneScreencap.png', 'fuli3.png') is not None:
                print("fuli3！" + str(
                    matchImg('phoneScreencap.png', 'fuli3.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli3.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli3.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli3.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                print("fuli3")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') is not None:
                    print("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close1")
                if matchImg('phoneScreencap.png', 'close2.png') is not None:
                    print("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close2")

            if matchImg('phoneScreencap.png', 'fuli4.png') is not None:
                print("fuli4！" + str(
                    matchImg('phoneScreencap.png', 'fuli4.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli4.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli4.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli4.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                print("fuli4")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') is not None:
                    print("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close1")
                if matchImg('phoneScreencap.png', 'close2.png') is not None:
                    print("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close2")

            if matchImg('phoneScreencap.png', 'fuli5.png') is not None:
                print("fuli5！" + str(
                    matchImg('phoneScreencap.png', 'fuli5.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli5.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli5.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli5.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                print("fuli5")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') is not None:
                    print("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close1")
                if matchImg('phoneScreencap.png', 'close2.png') is not None:
                    print("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    print("close2")

        except Exception as e:
            print(e)
            print("这里有个异常")

    # 快看点
    def kuaikandian():
        # 点击左下角的刷新按钮
        os.popen('adb -s 66819679 shell input tap 107 2222', 'r', 1)
        print("快看点_点击左下角的刷新按钮")
        time.sleep(3)
        # 向下滑动
        os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
        time.sleep(6)
        # 截图
        screencap()
        print("快看点_截图")
        try:
            # 点击分钟前，能进去看
            if matchImg('phoneScreencap.png', 'kuaikandian_min.png') is not None:
                print("淘新闻_点kuaikandian进去看资讯！" + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 向下滑动
                for i in range(1, 15, 1):
                    i = i + 1
                    time.sleep(random.uniform(1.0, 2.0))
                    # 向下滑动
                    os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                    mytime = datetime.datetime.now()
                    print("kuaikandian_已经滚动" + str(i) + "次。" + str(mytime) + "")

                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                print("kuaikandian_返回")
                time.sleep(2)
            # 点击评论，能进去看
            elif matchImg('phoneScreencap.png', 'kuaikandian_comment.png') is not None:
                print("kuaikandian_comment！" + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 向下滑动
                for i in range(1, 15, 1):
                    i = i + 1
                    time.sleep(random.uniform(1.0, 2.0))
                    # 向下滑动
                    os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                    mytime = datetime.datetime.now()
                    print("kuaikandian__已经滚动" + str(i) + "次。" + str(mytime) + "")

                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                print("kuaikandian_返回")
                time.sleep(2)
            elif matchImg('phoneScreencap.png', 'install.png') is not None:
                print("install！" + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'install.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'install.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)

        except Exception as e:
            print(e)
            print("这里有个异常")
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)

    def douyin():
        os.popen('adb -s 66819679 shell input tap 100 2222', 'r', 1)
        mytime = random.uniform(5.0, 15.0)
        print("see time : " + str(mytime))
        time.sleep(mytime)

    # 打开微博
    def openWeibo():
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 去点击
        os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
        time.sleep(2)
        # 打开weibo
        os.popen('adb -s 66819679 shell input tap 125 607', 'r', 1)
        time.sleep(7)
        # 点击发现
        os.popen('adb -s 66819679 shell input tap 552 2212', 'r', 1)
        time.sleep(4)
        # 再一次点击发现
        os.popen('adb -s 66819679 shell input tap 552 2212', 'r', 1)
        time.sleep(4)
        # 点击搜索框
        os.popen('adb -s 66819679 shell input tap 552 155', 'r', 1)
        time.sleep(2)
        # 点击最近的一次搜索文字
        os.popen('adb -s 66819679 shell input tap 552 311', 'r', 1)
        time.sleep(5)
        # 点击实时
        os.popen('adb -s 66819679 shell input tap 406 286', 'r', 1)
        time.sleep(5)

    # 微博点赞
    def Weibo_zan():

        mytime = random.uniform(1.0, 3.0)
        print("-------zan函数被调用: " + str(mytime))
        time.sleep(mytime)
        # 截图
        screencap()
        try:
            # 窗口1
            if matchImg('phoneScreencap.png', 'zan.png') is not None:
                print("找到zan！" + str(
                    matchImg('phoneScreencap.png', 'zan.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'zan.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'zan.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'zan.png')['result'][1])
                print("我来点击：点赞")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(1)
        except Exception as e:
            print(e)
            print("这里有个异常")

        try:
            # 窗口1
            if matchImg('phoneScreencap.png', 'comment.png') is not None:
                print("找到评论！" + str(
                    matchImg('phoneScreencap.png', 'comment.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'comment.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'comment.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'comment.png')['result'][1])
                print("我来点击：评论")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'baidulogo.png') is not None:
                    print("找到baidulogo！" + str(
                        matchImg('phoneScreencap.png', 'baidulogo.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'baidulogo.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'baidulogo.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'baidulogo.png')['result'][1])
                    print("我来点击：baidulogo")
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(2)
                    # 百度输入法 -- 懒人短语
                    os.popen('adb -s 66819679 shell input tap 680 1663', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 点击我的话
                    os.popen('adb -s 66819679 shell input tap 428 1713', 'r', 1)
                    time.sleep(2)
                    # 百度输入法 -- 键盘随便一个字母
                    myxstr = str(random.randint(203, 841))
                    myystr = str(random.randint(1600, 1960))
                    os.popen('adb -s 66819679 shell input tap ' + myxstr + ' ' + myystr, 'r', 1)
                    print(myxstr + myystr)
                    time.sleep(2)
                    # 百度输入法 -- 回车
                    os.popen('adb -s 66819679 shell input tap 974 2150', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 发送
                    os.popen('adb -s 66819679 shell input tap 988 1253', 'r', 1)
                    time.sleep(2)
                    # goback()
                elif matchImg('phoneScreencap.png', 'comment2.png') is not None:
                    print("找到评论comment2！" + str(
                        matchImg('phoneScreencap.png', 'comment2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'comment2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'comment2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'comment2.png')['result'][1])
                    print("评论comment2：")
                    # 点击底部的评论按钮
                    os.popen('adb -s 66819679 shell input tap 513 2212', 'r', 1)
                    time.sleep(3)
                    # 百度输入法
                    os.popen('adb -s 66819679 shell input tap 87 1463', 'r', 1)
                    time.sleep(2)
                    # 百度输入法 -- 懒人短语
                    os.popen('adb -s 66819679 shell input tap 680 1663', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 点击我的话
                    os.popen('adb -s 66819679 shell input tap 428 1713', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 键盘随便一个字母
                    myxstr = str(random.randint(203, 841))
                    myystr = str(random.randint(1600, 1960))
                    os.popen('adb -s 66819679 shell input tap ' + myxstr + ' ' + myystr, 'r', 1)
                    print(myxstr + myystr)
                    time.sleep(2)
                    # 百度输入法 -- 回车
                    os.popen('adb -s 66819679 shell input tap 974 2150', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 发送
                    os.popen('adb -s 66819679 shell input tap 988 1253', 'r', 1)
                    time.sleep(2)
                    goback()
        except Exception as e:
            print(e)
            print("这里有个异常")

        for i in range(1, 4):
            # 截图
            time.sleep(2)
            screencap()

            if matchImg('phoneScreencap.png', 'search.png') is not None:
                print("找到search！" + str(
                    matchImg('phoneScreencap.png', 'search.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'search.png')['result'][1]))
                # myx = str(matchImg('phoneScreencap.png', 'search.png')['result'][0])
                # myy = str(matchImg('phoneScreencap.png', 'search.png')['result'][1])
                # 向下滑动
                print("向下滑动")
                os.popen('adb -s 66819679 shell input swipe 361 1700 361 1400')
                time.sleep(2)
            else:
                print('不是预计的界面，要返回了')
                goback()
                time.sleep(2)

        # 向下滑动
        print("向下滑动")
        os.popen('adb -s 66819679 shell input swipe 361 1700 361 1000')
        time.sleep(2)

    # 模拟滑动
    def initlocal():
        time.sleep(2)  # 滑动前休息2秒，避免网络不好
        os.system('adb -s 66819679 shell input swipe 900 1200 900 500')  # 模拟从下往上滑动
        time.sleep(2)  # 滑动后休息2秒，避免开始计时延迟

    # 返回上一页面
    def goback():
        os.system('adb -s 66819679 shell input keyevent KEYCODE_BACK')  # 返回
        print('返回')

    # 刷宝提现
    def shuabao_money():
        print("刷宝提现开始")


        i = 0
        # 返回好多次
        backback()
        # 打开刷宝
        print("打开刷宝")
        os.popen('adb -s 66819679 shell input tap 337 267', 'r', 1)
        time.sleep(5)
        # 点击“我”
        print("点击“我”")
        os.popen('adb -s 66819679 shell input tap 983 2195', 'r', 1)
        time.sleep(5)
        os.popen('adb -s 66819679 shell input tap 983 2195', 'r', 1)
        time.sleep(5)
        goback()
        os.popen('adb -s 66819679 shell input tap 983 2195', 'r', 1)
        time.sleep(5)
        # 点击当前余额
        print("点击当前余额")
        os.popen('adb -s 66819679 shell input tap 629 840', 'r', 1)
        time.sleep(5)
        # 点击提现
        print("# 点击提现")
        os.popen('adb -s 66819679 shell input tap 926 442', 'r', 1)
        time.sleep(5)
        # 点击0.31
        print("# 点击0.31")
        os.popen('adb -s 66819679 shell input tap 852 825', 'r', 1)
        time.sleep(5)
        # 点击立即提现
        print("# 点击立即提现")
        os.popen('adb -s 66819679 shell input tap 509 2185', 'r', 1)
        time.sleep(5)
        # 返回好多次
        print("# 返回好多次")
        backback()
        # home
        os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
        time.sleep(3)



        # 签到
        # 打开刷宝
        print("打开刷宝")
        os.popen('adb -s 66819679 shell input tap 337 267', 'r', 1)
        time.sleep(5)
        # 点击“任务”
        print("点击“任务”")
        os.popen('adb -s 66819679 shell input tap 747 2222', 'r', 1)
        time.sleep(3)
        # 点击“任务”
        print("点击“任务”")
        os.popen('adb -s 66819679 shell input tap 747 2222', 'r', 1)
        time.sleep(7)
        # 点击“关闭小窗口”
        print("点击“关闭小窗口”")
        os.popen('adb -s 66819679 shell input tap 867 712', 'r', 1)
        time.sleep(3)
        # 点击“立即签到”
        print("点击立即签到")
        os.popen('adb -s 66819679 shell input tap 896 541', 'r', 1)
        time.sleep(2)
        # 点击“立即签到”
        print("点击立即签到")
        os.popen('adb -s 66819679 shell input tap 896 541', 'r', 1)
        time.sleep(2)
        # # 点击“立即签到”
        # print("点击立即签到")
        # os.popen('adb -s 66819679 shell input tap 896 541', 'r', 1)
        # time.sleep(3)
        # 点击“看视频”
        print("看视频")
        os.popen('adb -s 66819679 shell input tap 737 1528', 'r', 1)
        time.sleep(33)
        # 关掉视频”
        print("关掉视频”")
        os.popen('adb -s 66819679 shell input tap 978 170', 'r', 1)
        time.sleep(2)
        # 关掉视频”
        print("关掉视频”")
        os.popen('adb -s 66819679 shell input tap 978 170', 'r', 1)
        time.sleep(2)


        

    # 快看点提现
    def kuaikandian_money():
        print("快看点提现开始")
        # 返回
        print("返回返回好多次")
        # 返回好多次
        backback()
        # 打开快看点
        os.popen('adb -s 66819679 shell input tap 957 260', 'r', 1)
        time.sleep(7)
        # 点击任务
        print("点击任务")
        os.popen('adb -s 66819679 shell input tap 963 2202', 'r', 1)
        time.sleep(3)
        # 点击任务
        print("点击任务")
        os.popen('adb -s 66819679 shell input tap 963 2202', 'r', 1)
        time.sleep(2)
        goback()
        # 点击任务
        print("点击任务")
        os.popen('adb -s 66819679 shell input tap 963 2202', 'r', 1)
        time.sleep(3)
        # 点击我的金币
        print("点击我的金币")
        os.popen('adb -s 66819679 shell input tap 126 437', 'r', 1)
        time.sleep(5)
        # 点击去提现
        print("点击去提现")
        os.popen('adb -s 66819679 shell input tap 980 360', 'r', 1)
        time.sleep(3)
        # 点击提现
        print("点击提现长按钮")
        os.popen('adb -s 66819679 shell input tap 568 2205', 'r', 1)
        time.sleep(6)
       
        print("点击提现长按钮")
        os.popen('adb -s 66819679 shell input tap 568 2205', 'r', 1)
        time.sleep(6)
        # 点击绿色的按钮提现
        print("点击绿色的按钮提现")
        os.popen('adb -s 66819679 shell input tap 553 739', 'r', 1)
        time.sleep(6)
        # 返回好多次
        backback()
        # home
        os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
        time.sleep(3)


    i = 0
    while 1 == 1:
        mytime = datetime.datetime.now()
        print("现在时间（）：" + str(mytime.date())+ str(mytime.minute))

        # 刷宝
        if (mytime.hour == 2) or (mytime.hour == 3) or (mytime.hour == 0) or (mytime.hour == 23) or (mytime.hour == 1) or (mytime.hour == 12) :
            print("刷宝开始")
            i = 0
            # 返回好多次
            backback()
            # 打开刷宝
            os.popen('adb -s 66819679 shell input tap 337 267', 'r', 1)
            time.sleep(10)
            for myy in range(1, 20, 1):
                i = i + 1
                shuabao()
                mytime = datetime.datetime.now()
                print("shuabao" + str(i) + "次。" + str(mytime))
                # if myy == 1 :
                #     shuabao_comment()
                #     print("shuabao_comment")
            time.sleep(1)
            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()
      
        # 快看点
        if (mytime.hour == 4) or (mytime.hour == 5) or (mytime.hour == 21) or (mytime.hour == 22) or (mytime.hour == 6):
            # 判断是不是第一次运行,提现
            print("判断是不是第一次运行")
            print(firsttime)
            if firsttime == 1 and mytime.hour == 6:
                firsttime = 0
                print(firsttime)
                shuabao_money()
                kuaikandian_money()
            print("快看点开始")
            i = 0
            # 返回
            print("返回" + str(mytime))
            # 返回好多次
            backback()
            # 打开快看点
            os.popen('adb -s 66819679 shell input tap 957 260', 'r', 1)
            time.sleep(10)
            for myy in range(1, 20, 1):
                i = i + 1
                kuaikandian()
                mytime = datetime.datetime.now()
                print("快看点" + str(i) + "次。" + str(mytime))
            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()

        # 支付宝
        if (mytime.hour == 7) or (mytime.hour == 8) or (mytime.hour == 9) or (mytime.hour == 10):


            i = 0
            # 返回好多次
            backback()
            openalipay()
            for myy in range(1, 15, 1):
                i = i + 1
                time.sleep(1)
                doit()
                mytime = datetime.datetime.now()
                print("已经滚动" + str(i) + "次。" + str(mytime))
            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()

        # 手机微博点赞

        myinttime = 25
        myinttime2 = 26
        if (mytime.hour == myinttime) or (mytime.hour == myinttime2):
            mytime = datetime.datetime.now()
            i = 0
            # 返回好多次

            backback()

            openWeibo()
            for myy in range(1, 10000, 1):
                print("for循环内")
                mytime = datetime.datetime.now()
                if (mytime.hour == myinttime) or (mytime.hour == myinttime2):
                    Weibo_zan()
                    print("是这个时间段")
                else:
                    print("不是这个时间段")
                    break

            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        print("现在时间（）：" + str(datetime.datetime.now()))
        print("if outside _ timesleep。。。。。。。。")
        time.sleep(3)


main()
