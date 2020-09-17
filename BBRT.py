# coding = utf-8
import os
import shutil
import sys

import easygui as gui

ver = 0.2

gui.msgbox("B.B.R.T. " + str(ver) + " By AlwaysGu & Swung0x48. 请把程序放置在Ballance/3D Entities", title="About")
ballType = gui.choicebox("选择球的类型：", "B.B.R.T.", ["力量球", "其他球", "默认"])
ballPath = "Balls.nmo"
path = "Res/"


def swap(arg):
    if arg is None:
        sys.exit()
    if os.path.exists("Balls.nmo"):
        os.remove("Balls.nmo")
    shutil.copy(os.path.join(path, "Balls" + arg + ".nmo"), ballPath)
    gui.msgbox("替换完成", title="B.B.R.T.")
    sys.exit()


if ballType == "默认":
    swap("")
elif ballType == "力量球":
    option = gui.choicebox("选择倍率：", "B.B.R.T.", ["1.5t", "2t", "3t", "5t", "10t", "50t", "100t"])
    swap(option)
elif ballType == "其他球":
    option = gui.choicebox("选择类型：", "B.B.R.T.", ["不会转的球", "三高球", "自动过关球", "无语球", "小弹力球", "无重力球", "大弹力球", "半透明球"])
    dictionary = {
        "不会转的球": "Doesnotturns",
        "三高球": "3High",
        "自动过关球": "Auto",
        "无语球": "byst",
        "小弹力球": "LittleT",
        "无重力球": "NoG",
        "大弹力球": "T",
        "半透明球": "Translucent"
    }
    swap(dictionary[option])
