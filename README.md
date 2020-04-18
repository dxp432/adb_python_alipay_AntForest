# 蚂蚁森林自动收取能量、偷取能量、浇水
蚂蚁森林自动收取能量、偷取能量、浇水（使用adb、python）adb_python_alipay_AntForest

## 涉及到的技术：
1、python

2、adb
## 具备的功能：
1、自动收取能量

2、自动偷取能量

3、自动给指定的朋友浇水
## 使用方法：
1、打开电脑，USB线一头接手机，一头接电脑。

2、电脑运行python程序，会自动执行手机操作。

3、python程序偷完所有的朋友能量，会自动永远循环再来，继续从头偷。

## 代码思路：
1、用adb去控制手机：包括自动点击、滑屏、截图送到电脑那。但是点哪里？什么时候滑动？这时候python出马了。

2、用python主要去判断手机送过来的截图是否是我要的，并找到坐标，让adb点击坐标。同理，通过手机adb送过来的截图，判断，通过点击进行自动收取能量、自动偷取能量、自动给指定的朋友浇水。

## 部分代码：
用python主要去判断手机送过来的截图是否是我要的，并找到坐标：
对比两张图，找到坐标。
```Python
def matchImg(imgsrc, imgobj):  # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj, 0.9)  #0.9、confidence是精度，越小对比的精度就越低 {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    return match_result
```
通过截图和下面的小图片对比，找到坐标：

如果发现截图包含这个图片就说明需要从头继续![](alipay_nomore.png)

如果发现截图包含这个图片就说明需要点击，查看更多好友![](alipay_lookForMoreFriends.png)

如果发现截图包含这个图片就说明点击进行浇水![](alipay_water.png)

如果发现截图包含这个图片就说明需要点击去偷能量![](alipay_friend.png)

adb截图、发送到电脑：
```Python
# 截图
    os.popen('adb -s 66819679 shell screencap -p /storage/emulated/0/Documents/phoneScreencap.png')
    time.sleep(1.5)
    os.popen('adb -s 66819679 pull /storage/emulated/0/Documents/phoneScreencap.png')
    time.sleep(1.5)
```

adb点击
```Python
os.popen('adb -s 66819679 shell input tap 135 250', 'r', 1)
```

adb滑动：
```Python
# 向下滑动
    os.popen('adb -s 66819679 shell input swipe 520 300 520 1000')
```


## 注意：
如果想用在自己手机上，得修改几个地方：

* 请修改你要执行的时间。比如我的代码时定时在7点开始执行支付宝操作。如果你想8点，就修改为if (mytime.hour == 8) 之类的。

* 修改指定相应的设备 serialNumber 号，我的是66819679

* 修改你的坐标。我的手机分辨率和你的不一定一样。

* 截图的路径。我的手机截图路径和你的不一定一样。

* 加入了刷宝和快看点这两个app，主要是在晚上睡觉的时候自动刷视频新闻，每天早上会自动提现，两个app加起来每天大概0.6元的提现可以拿到手。

---
微信公众账号：小鹏同学

如果对你有帮助，可以微信赞赏我，万分感谢。

![avatar](https://raw.githubusercontent.com/dxp432/Cloud-disk/master/img/money.jpg)
