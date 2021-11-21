from tkinter import *
import MainGUI
import Utils

def configGUI():
    #                            Create frame                               #

    root = Tk()

    #                 Initialisation of some useful variables                #

    lastClickX = 0
    lastClickY = 0

    backgroundPicture = PhotoImage(file=Utils.getResourcesPath("resources\\config_background.png"))
    titleBarPicture = PhotoImage(file=Utils.getResourcesPath("resources\\config_title_bar.png"))
    movePicture = PhotoImage(file=Utils.getResourcesPath("resources\\config_move.png"))
    toggleMusicPicture = PhotoImage(file=Utils.getResourcesPath("resources\\config_toggle_music.png"))
    toggleSoundEffectsPicture = PhotoImage(file=Utils.getResourcesPath("resources\\config_toggle_sound_effects.png"))
    resetConfigPicture = PhotoImage(file=Utils.getResourcesPath("resources\\config_reset_config.png"))

    reducePicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\config_reduce.png"))
    closePicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\config_close.png"))
    soundOnPicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\sound_on.png"))
    soundOffPicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\sound_off.png"))
    resetConfigButtonPicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\reset_config.png"))

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
        MainGUI.mainGUI()

    def refreshFrame(event):
        if Utils.getSettingValue("music"):
            button_toggle_music.config(image=soundOnPicture)
        elif not Utils.getSettingValue("music"):
            button_toggle_music.config(image=soundOffPicture)

        if Utils.getSettingValue("sound_effects"):
            button_toggle_sound_effects.config(image=soundOnPicture)
        elif not Utils.getSettingValue("sound_effects"):
            button_toggle_sound_effects.config(image=soundOffPicture)

        volume_control.set(Utils.getSettingValue("volume"))
        volume_value.config(text=Utils.getSettingValue("volume") + " %")

    def toggleMusic():
        Utils.buttonClick("button_toggle_music")
        if Utils.getSettingValue("music"):
            button_toggle_music.config(image=soundOffPicture)
            Utils.setSettingValue("music", "toggleOff")
        elif not Utils.getSettingValue("music"):
            button_toggle_music.config(image=soundOnPicture)
            Utils.setSettingValue("music", "toggleOn")

    def toggleSoundEffects():
        Utils.buttonClick("button_toggle_sound_effects")
        if Utils.getSettingValue("sound_effects"):
            button_toggle_sound_effects.config(image=soundOffPicture)
            Utils.setSettingValue("sound_effects", "toggleOff")
        elif not Utils.getSettingValue("sound_effects"):
            button_toggle_sound_effects.config(image=soundOnPicture)
            Utils.setSettingValue("sound_effects", "toggleOn")

    def setVolume(volume):
        Utils.setSettingValue("volume", str(volume))
        volume_value.config(text=Utils.getSettingValue("volume") + " %")

    def getPictureForButton(buttonName):
        if buttonName == "music":
            if Utils.getSettingValue("music"):
                return soundOnPicture
            elif not Utils.getSettingValue("music"):
                return soundOffPicture
        elif buttonName == "sound_effects":
            if Utils.getSettingValue("sound_effects"):
                return soundOnPicture
            elif not Utils.getSettingValue("sound_effects"):
                return soundOffPicture

    def resetConfig():
        Utils.buttonClick("button_reset_config")
        Utils.resetConfig()

    #                      Set frame basics parameters                       #

    root.wm_attributes("-topmost", 1)
    root.geometry("200x200")
    root.resizable(width=False, height=False)
    root.iconbitmap(Utils.getResourcesPath("resources\\icons\\app_icon.ico"))
    root.bind("<Map>", mappedFrame)

    #                        Add components to frame                         #

    root.bind("<Enter>", refreshFrame)

    background = Label(image=backgroundPicture, width=200, height=200, bd=0)
    background.place(x=0, y=0)

    title_bar = Label(image=titleBarPicture, width=200, height=30, bd=0)
    title_bar.place(x=0, y=0)

    move_area = Label(image=movePicture, width=28, height=28, bd=0)
    move_area.place(x=0, y=0)
    move_area.bind("<B1-Motion>", moveFrame)

    toggle_music = Label(image=toggleMusicPicture, width=80, height=20, bd=0)
    toggle_music.place(x=50, y=50)

    toggle_sound_effects = Label(image=toggleSoundEffectsPicture, width=115, height=20, bd=0)
    toggle_sound_effects.place(x=50, y=80)

    reset_config = Label(image=resetConfigPicture, width=70, height=15, bd=0)
    reset_config.place(x=56, y=132)

    volume = Label(text="Volume : ", font=("Segoe Script", 8), bd=0, bg="white")
    volume.place(x=25, y=160)

    volume_value = Label(text=Utils.getSettingValue("volume") + " %", font=("Segoe Script", 8), bd=0, bg="white")
    volume_value.place(x=80, y=160)

    button_reduce = Button(image=reducePicture, bd=0, highlightthickness=0, padx=32, pady=28, command=reduceFrame)
    button_reduce.place(x=140, y=0)

    button_close = Button(image=closePicture, bd=0, highlightthickness=0, padx=28, pady=28, command=closeFrame)
    button_close.place(x=172, y=0)

    button_toggle_music = Button(image=getPictureForButton("music"), bd=0, highlightthickness=0, padx=40, pady=40, command=toggleMusic)
    button_toggle_music.place(x=25, y=50)

    button_toggle_sound_effects = Button(image=getPictureForButton("sound_effects"), bd=0, highlightthickness=0, padx=40, pady=40, command=toggleSoundEffects)
    button_toggle_sound_effects.place(x=25, y=80)

    button_reset_config = Button(image=resetConfigButtonPicture, bd=0, highlightthickness=0, padx=28, pady=28, command=resetConfig)
    button_reset_config.place(x=26, y=131)

    volume_control = Scale(from_=1, to=100, orient=HORIZONTAL, length=140, width=10, bd=0, bg="#ba0308", activebackground="#ba0308", troughcolor="white",sliderrelief="flat", sliderlength=20, showvalue=0,  highlightthickness=2, highlightbackground="black", command=setVolume)
    volume_control.set(Utils.getSettingValue("volume"))
    volume_control.place(x=25, y=180)

    #                          Loop the frame                           #

    root.mainloop()