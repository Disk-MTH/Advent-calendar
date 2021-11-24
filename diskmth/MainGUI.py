from tkinter import *
import Utils
import ConfigGUI

def mainGUI():

    #                      Create frame and init song                        #

    root = Tk()

    #                 Initialisation of some useful variables                #

    lastClickX = 0
    lastClickY = 0

    backgroundPicture = PhotoImage(file=Utils.getResourcesPath("resources\\main_background.png"))
    titleBarPicture = PhotoImage(file=Utils.getResourcesPath("resources\\main_title_bar.png"))
    movePicture = PhotoImage(file=Utils.getResourcesPath("resources\\main_move.png"))
    try:
        creditsPicture = PhotoImage(file=Utils.getResourcesPath("resources\\main_credits.png"))
    except TclError:
        pass

    configPicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\main_config.png"))
    reducePicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\main_reduce.png"))
    closePicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\main_close.png"))

    day1Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_1.png"))
    day2Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_2.png"))
    day3Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_3.png"))
    day4Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_4.png"))
    day5Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_5.png"))
    day6Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_6.png"))
    day7Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_7.png"))
    day8Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_8.png"))
    day9Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_9.png"))
    day10Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_10.png"))
    day11Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_11.png"))
    day12Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_12.png"))
    day13Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_13.png"))
    day14Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_14.png"))
    day15Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_15.png"))
    day16Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_16.png"))
    day17Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_17.png"))
    day18Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_18.png"))
    day19Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_19.png"))
    day20Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_20.png"))
    day21Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_21.png"))
    day22Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_22.png"))
    day23Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_23.png"))
    day24Picture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\days\\day_24.png"))

    #                Initialisation of some useful functions                #

    def moveFrame(event):
        x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
        root.geometry("+%s+%s" % (x, y))

    def mappedFrame(event):
        root.overrideredirect(True)

    def reduceFrame():
        Utils.buttonClick("button_reduce")
        root.state('withdrawn')
        root.overrideredirect(False)
        root.state('iconic')

    def closeFrame():
        Utils.buttonClick("button_close")
        root.destroy()

    def openConfig():
        Utils.buttonClick("button_config")
        closeFrame()
        ConfigGUI.configGUI()

    def createAButton(image, command):
        return Button(image=image, bd=0, highlightthickness=0, padx=67, pady=67, command=command)

    #                      Set frame basics parameters                       #

    root.wm_attributes("-topmost", True)
    root.geometry("1000x650")
    root.resizable(width=False, height=False)
    root.iconbitmap(Utils.getResourcesPath("resources\\icons\\app_icon.ico"))
    root.bind("<Map>", mappedFrame)

    #                        Add components to frame                         #

    background = Label(image=backgroundPicture, width=1000, height=650, bd=0)
    background.place(x=0, y=0)

    titleBar = Label(image=titleBarPicture, width=1000, height=45, bd=0)
    titleBar.place(x=0, y=0)

    try:
        credits = Label(image=creditsPicture, width=198, height=50, bd=0)
        credits.place(x=800, y=600)
    except UnboundLocalError:
        pass

    moveArea = Label(image=movePicture, width=43, height=43, bd=0)
    moveArea.place(x=0, y=0)
    moveArea.bind("<B1-Motion>", moveFrame)

    buttonConfig = Button(image=configPicture, bd=0, highlightthickness=0, padx=35, pady=40, command=openConfig)
    buttonConfig.place(x=875, y=0)

    buttonReduce = Button(image=reducePicture, bd=0, highlightthickness=0, padx=45, pady=40, command=reduceFrame)
    buttonReduce.place(x=915, y=0)

    buttonClose = Button(image=closePicture, bd=0, highlightthickness=0, padx=40, pady=40, command=closeFrame)
    buttonClose.place(x=960, y=0)

    buttonDay1 = createAButton(day1Picture, None)
    buttonDay1.place(x=547, y=68)

    buttonDay2 = createAButton(day2Picture, None)
    buttonDay2.place(x=48, y=213)

    buttonDay3 = createAButton(day3Picture, None)
    buttonDay3.place(x=214, y=213)

    buttonDay4 = createAButton(day4Picture, None)
    buttonDay4.place(x=381, y=362)

    buttonDay5 = createAButton(day5Picture, None)
    buttonDay5.place(x=381, y=511)

    buttonDay6 = createAButton(day6Picture, None)
    buttonDay6.place(x=548, y=218)

    buttonDay7 = createAButton(day7Picture, None)
    buttonDay7.place(x=712, y=67)

    buttonDay8 = createAButton(day8Picture, None)
    buttonDay8.place(x=547, y=360)

    buttonDay9 = createAButton(day9Picture, None)
    buttonDay9.place(x=214, y=506)

    buttonDay10 = createAButton(day10Picture, None)
    buttonDay10.place(x=712, y=360)

    buttonDay11 = createAButton(day11Picture, None)
    buttonDay11.place(x=48, y=506)

    buttonDay12 = createAButton(day12Picture, None)
    buttonDay12.place(x=880, y=219)

    buttonDay13 = createAButton(day13Picture, None)
    buttonDay13.place(x=880, y=360)

    buttonDay14 = createAButton(day14Picture, None)
    buttonDay14.place(x=713, y=214)

    buttonDay15 = createAButton(day15Picture, None)
    buttonDay15.place(x=380, y=67)

    buttonDay16 = createAButton(day16Picture, None)
    buttonDay16.place(x=213, y=358)

    buttonDay17 = createAButton(day17Picture, None)
    buttonDay17.place(x=879, y=67)

    buttonDay18 = createAButton(day18Picture, None)
    buttonDay18.place(x=49, y=361)

    buttonDay19 = createAButton(day19Picture, None)
    buttonDay19.place(x=381, y=213)

    buttonDay20 = createAButton(day20Picture, None)
    buttonDay20.place(x=214, y=68)

    buttonDay21 = createAButton(day21Picture, None)
    buttonDay21.place(x=48, y=68)

    buttonDay22 = createAButton(day22Picture, None)
    buttonDay22.place(x=712, y=506)

    buttonDay23 = createAButton(day23Picture, None)
    buttonDay23.place(x=877, y=505)

    buttonDay24 = createAButton(day24Picture, None)
    buttonDay24.place(x=547, y=510)

    #                             Loop the frame                              #

    root.mainloop()