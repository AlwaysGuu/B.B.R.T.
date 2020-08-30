#coding = utf-8
import sys,os,shutil
import easygui as gui
gui.msgbox("B.B.R.T. 0.1 By AlwaysGu. 请把程序放置在Ballance/3D Entities",title="About")
l = gui.buttonbox(msg="选择球的类型",title="B.B.R.T.",choices=("力量球","其他球","默认"))
ballpath = "Balls.nmo"
path = "Res"   
if l == "默认":
    os.remove("Balls.nmo")
    npath = path + "/Balls.nmo"    
    shutil.copy(npath,ballpath)
    gui.msgbox("替换完成",title="B.B.R.T.")
elif l == "力量球":
    while 1:
        l1 = gui.enterbox(msg="选择球：1为1.5倍，2为2倍，3为3倍，5为5倍，10为10倍，50为50倍，100为100倍")
        if l1 == "1":
            npath = path + "/Power/Balls1.5t.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "2":
            npath = path + "/Power/Balls2t.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "3":
            npath = path + "/Power/Balls3t.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "5":
            npath = path + "/Power/Balls5t.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "10":
            npath = path + "/Power/Balls10t.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "50":
            npath = path + "/Power/Balls50t.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "100":
            npath = path + "/Power/Balls100t.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        else:
            gui.msgbox("请输入正确数字")
elif l == "其他球":
    while 1:
        l1 = gui.enterbox(msg="选择球：a为不会转的球，b为三高球，c为自动过关球，d为无语球，e为小弹力球，f无重力球，g为大弹力球，h为半透明球")
        if l1 == "a":
            npath = path + "/Other/BallDoesnotturns.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "b":
            npath = path + "/Other/Balls3High.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "c":
            npath = path + "/Other/BallsAuto.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "d":
            npath = path + "/Other/Ballsbyst.Nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "e":
            npath = path + "/Other/BallsLittleT.NMO"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "f":
            npath = path + "/Other/BallsNoG.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "g":
            npath = path + "/Other/BallsT.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        elif l1 == "h":
            npath = path + "/Other/BallsTranslucent.nmo"
            os.remove("Balls.nmo")
            shutil.copy(npath,ballpath)
            gui.msgbox("替换完成")
            sys.exit()
        else:
            gui.msgbox("请输入正确小写字母")