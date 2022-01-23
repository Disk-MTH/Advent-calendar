import time
import pygame
import MainGUI
import os
import sys

global music
global sound_effects
global volume
global lines


def get_resources_path(relative_path):
    try:
        file_name = relative_path.split("\\")[-1]
        base_path = sys._MEIPASS
        return os.path.join(base_path + "\\" + file_name)
    except Exception:
        base_path = os.path.realpath(__file__)
        base_path = base_path.replace("\\Utils.py", "")
        return os.path.join(base_path + "\\" + relative_path)


def get_config_path():
    return os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Advent-calendar\\"


def load_config():
    global lines

    try:
        os.mkdir(get_config_path())
    except FileExistsError:
        pass

    try:
        with open(get_config_path() + "settings.txt", "r") as file:
            lines = file.readlines()
            lines[0] = lines[0].replace("\n", "")
            lines[1] = lines[1].replace("\n", "")
            lines[2] = lines[2].replace("\n", "")
    except FileNotFoundError:
        create_config()
        with open(get_config_path() + "settings.txt", "r") as file:
            lines = file.readlines()
            lines[0] = lines[0].replace("\n", "")
            lines[1] = lines[1].replace("\n", "")
            lines[2] = lines[2].replace("\n", "")


def check_config():
    global music
    global sound_effects
    global volume
    global lines

    if lines[0][:8] == "music : ":
        if lines[0][8:] == "enable":
            music = True
        elif lines[0][8:] == "disable":
            music = False
        else:
            create_config()
            load_config()
            check_config()
    else:
        create_config()
        load_config()
        check_config()

    if lines[1][:16] == "sound effects : ":
        if lines[1][16:] == "enable":
            sound_effects = True
        elif lines[1][16:] == "disable":
            sound_effects = False
        else:
            create_config()
            load_config()
            check_config()
    else:
        create_config()
        load_config()
        check_config()

    if lines[2][:9] == "volume : ":
        if 0 <= int(lines[2][9:]) <= 100:
            volume = lines[2][9:]
        else:
            create_config()
            load_config()
            check_config()
    else:
        create_config()
        load_config()
        check_config()


def create_config():
    with open((get_config_path() + "settings.txt"), "w") as file:
        default_settings = ["music : enable\n", "sound effects : enable\n", "volume : 80\n"]
        index = 0
        for i in range(len(default_settings)):
            line_to_write = default_settings[index]
            file.write(line_to_write)
            index += 1


def save_config():
    global music
    global sound_effects
    global volume

    with open((get_config_path() + "settings.txt"), "w") as file:
        if music:
            music = "music : enable\n"
        else:
            music = "music : disable\n"

        if sound_effects:
            sound_effects = "sound effects : enable\n"
        else:
            sound_effects = "sound effects : disable\n"

        volume = "volume : " + str(volume) + "\n"
        settings = [music, sound_effects, volume]
        index = 0
        for i in range(len(settings)):
            line_to_write = settings[index]
            file.write(line_to_write)
            index += 1


def reset_config():
    global music
    global sound_effects
    global volume

    music = True
    sound_effects = True
    volume = "80"


def get_setting_value(setting_to_get):
    global music
    global sound_effects
    global volume

    if setting_to_get == "music":
        return music
    elif setting_to_get == "sound_effects":
        return sound_effects
    elif setting_to_get == "volume":
        return volume


def set_setting_value(setting_to_set, value):
    global music
    global sound_effects
    global volume

    if setting_to_set == "music":
        music = value
    elif setting_to_set == "sound_effects":
        sound_effects = value
    elif setting_to_set == "volume":
        volume = value


def button_click_sound(is_day_button):
    global volume
    click_sound = pygame.mixer.Sound(get_resources_path("resources\\sounds\\click_sound.mp3"))
    if get_setting_value("sound_effects"):
        if is_day_button:
            click_sound.set_volume(float((int(get_setting_value("volume")) / 100)))
            click_sound.play()
            # add effect for case opening
        else:
            click_sound.set_volume(float((int(get_setting_value("volume")) / 100)))
            click_sound.play()


def launch_gui():
    MainGUI.main_gui()


def launch_sounds(gui_thread):
    global music
    global volume
    is_music_enable = False
    is_music_active = False

    pygame.mixer.init()

    while gui_thread.is_alive():
        if music:
            is_music_enable = True
        else:
            is_music_enable = False

        pygame.mixer.music.set_volume(float((int(volume) / 100)))

        if is_music_enable and not is_music_active:
            pygame.mixer.music.load(get_resources_path("resources\\sounds\\background_music.mp3"))
            pygame.mixer.music.play()
            is_music_active = True
        elif not is_music_enable and is_music_active:
            pygame.mixer.music.stop()
            is_music_active = False
        time.sleep(0.6)
