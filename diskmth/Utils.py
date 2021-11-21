from time import sleep
import pygame
import MainGUI
import os
import sys

def getResourcesPath(relativePath):
    try:
        fileName = relativePath.split("\\")[-1]
        base_path = sys._MEIPASS
        return os.path.join(base_path + "\\" + fileName)
    except Exception:
        base_path = os.path.realpath(__file__)
        base_path = base_path.replace("\\Utils.py", "")
        return os.path.join(base_path + "\\" + relativePath)

def getSettingValue(settingToGet) :
    with open(getResourcesPath("resources\\settings.txt"), "r") as file:
        lines = file.read().split()
        if settingToGet == "music":
            if lines[2] == "enable":
                return True
            elif lines[2] == "disable":
                return False
        elif settingToGet == "sound_effects":
            if lines[6] == "enable":
                return True
            elif lines[6] == "disable":
                return False
        elif settingToGet == "volume":
            return str(lines[9])

def setSettingValue(settingToSet, value):
    with open(getResourcesPath("resources\\settings.txt"), "rt") as file:
        fileContent = file.read()

    if settingToSet == "music":
        if value == "toggleOn":
            with open(getResourcesPath("resources\\settings.txt"), "wt") as file:
                fileContent = fileContent.replace("music : disable", "music : enable")
                file.write(fileContent)
        elif value == "toggleOff":
            with open(getResourcesPath("resources\\settings.txt"), "wt") as file:
                fileContent = fileContent.replace("music : enable", "music : disable")
                file.write(fileContent)

    elif settingToSet == "sound_effects":
        if value == "toggleOn":
            with open(getResourcesPath("resources\\settings.txt"), "wt") as file:
                fileContent = fileContent.replace("sound effects : disable", "sound effects : enable")
                file.write(fileContent)
        elif value == "toggleOff":
            with open(getResourcesPath("resources\\settings.txt"), "wt") as file:
                fileContent = fileContent.replace("sound effects : enable", "sound effects : disable")
                file.write(fileContent)

    elif settingToSet == "volume":
        with open(getResourcesPath("resources\\settings.txt"), "r") as file:
            lines = file.read().split()
            volume = lines[9]
            with open(getResourcesPath("resources\\settings.txt"), "wt") as file:
                fileContent = fileContent.replace("volume : " + str(volume), "volume : " + str(value))
                file.write(fileContent)

def resetConfig():
    with open(getResourcesPath("resources\\settings.txt"), "wt") as file:
        defaultSettings = ["music : enable\n", "sound effects : enable\n", "volume : 80\n"]
        index = 0
        for i in range(len(defaultSettings)):
            lineToWrite = defaultSettings[index]
            file.write(lineToWrite)
            index += 1

def buttonClick(nameOfButton):
    click_sound = pygame.mixer.Sound(getResourcesPath("resources\\sounds\\click_sound.mp3"))
    if getSettingValue("sound_effects"):
        if "day" in nameOfButton:
            click_sound.set_volume(float((int(getSettingValue("volume")) / 100)))
            click_sound.play()
        else:
            click_sound.set_volume(float((int(getSettingValue("volume")) / 100)))
            click_sound.play()

    elif not getSettingValue("sound_effects"):
        if "day" in nameOfButton:
            pass
        else:
            pass

def launchGUI():
    MainGUI.mainGUI()

def launchSounds(GUIThread):
    isMusicActive = False
    pygame.mixer.init()
    while GUIThread.is_alive():

        with open(getResourcesPath("resources\\settings.txt"), "r") as file:
            lines = file.read().split()
            isMusicEnable = False
            if lines[2] == "enable":
                isMusicEnable = True
            elif lines[2] == "disable":
                isMusicEnable = False
            volume = lines[9]

        pygame.mixer.music.set_volume(float((int(volume)/ 100)))
        if isMusicEnable and not isMusicActive:
            pygame.mixer.music.load(getResourcesPath("resources\\sounds\\background_music.mp3"))
            pygame.mixer.music.play()
            isMusicActive = True
        elif not isMusicEnable and isMusicActive:
            pygame.mixer.music.stop()
            isMusicActive = False
        sleep(0.25)

def checkConfig(GUIThread):
    while GUIThread.is_alive():
        with open(getResourcesPath("resources\\settings.txt"), "r") as file:
            lines = file.read().split()
            try:
                if lines[0] + " " + lines[1] + " " != "music : ":
                    resetConfig()
                if (lines[2] != "enable") and (lines[2] != "disable"):
                    resetConfig()
                if lines[3] + " " + lines[4] + " " + lines[5] + " " != "sound effects : ":
                    resetConfig()
                if (lines[6] != "enable") and (lines[6] != "disable"):
                    resetConfig()
                if lines[7] + " " + lines[8] + " " != "volume : ":
                    resetConfig()
                if (int(lines[9]) > 100) or (int(lines[9]) < 1):
                    resetConfig()
            except IndexError:
                resetConfig()
        sleep(0.25)