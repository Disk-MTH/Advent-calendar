import Utils
from threading import Thread

if __name__ == '__main__':
    Utils.load_config()
    Utils.check_config()

    gui_thread = Thread(target=Utils.launch_gui, name="GUIThread")
    sound_thread = Thread(target=Utils.launch_sounds, args=(gui_thread, ), name="SoundThread")

    gui_thread.start()
    sound_thread.start()

    gui_thread.join()
    sound_thread.join()

    Utils.save_config()
