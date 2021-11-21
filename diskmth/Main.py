import Utils
from threading import Thread

if __name__ == '__main__':
    GUIThread = Thread(target=Utils.launchGUI, name="GUIThread")
    SoundThread = Thread(target=Utils.launchSounds, args=(GUIThread, ), name="SoundThread")
    SettingsThread = Thread(target=Utils.checkConfig, args=(GUIThread, ), name="SettingsThread")

    GUIThread.start()
    SoundThread.start()
    SettingsThread.start()

    GUIThread.join()
    SoundThread.join()
    SettingsThread.join()