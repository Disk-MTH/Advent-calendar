from tkinter import *
import MainGUI
import Utils


def config_gui():
    # Create the frame

    root = Tk()

    # Initialisation of some useful variables

    last_click_x = 0
    last_click_y = 0

    # Definition of some useful functions

    def get_picture(path):
        try:
            print("aaa"
                  "")
            return PhotoImage(file=Utils.get_resources_path("resources\\" + path))
        except TclError:
            print("called")

    def move_frame(event):
        x, y = event.x - last_click_x + root.winfo_x(), event.y - last_click_y + root.winfo_y()
        root.geometry("+%s+%s" % (x, y))

    def mapped_frame(event):
        root.overrideredirect(True)

    def reduce_frame():
        Utils.button_click_sound(False)
        root.state('withdrawn')
        root.overrideredirect(False)
        root.state('iconic')

    def close_frame():
        Utils.button_click_sound(False)
        root.destroy()
        MainGUI.main_gui()

    sound_on_picture = PhotoImage(file=get_picture("buttons\\sound_on.png"))
    sound_off_picture = PhotoImage(file=get_picture("buttons\\sound_off.png"))

    #sound_on_picture = PhotoImage(file=Utils.get_resources_path("resources\\" + "buttons\\sound_on.png"))
    #sound_off_picture = PhotoImage(file=Utils.get_resources_path("resources\\" + "buttons\\sound_off.png"))

    def get_picture_for_toggle_buttons(button):
        if button == "music":
            if Utils.get_setting_value("music"):
                return sound_on_picture
            elif not Utils.get_setting_value("music"):
                return sound_off_picture
        elif button == "sound_effects":
            if Utils.get_setting_value("sound_effects"):
                return sound_on_picture
            elif not Utils.get_setting_value("sound_effects"):
                return sound_off_picture

    def toggle(button):
        Utils.button_click_sound(False)
        if button == "music":
            if Utils.get_setting_value("music"):
                button_toggle_music.config(image=sound_off_picture)
                Utils.set_setting_value("music", False)
            elif not Utils.get_setting_value("music"):
                button_toggle_music.config(image=sound_on_picture)
                Utils.set_setting_value("music", True)
        elif button == "sound_effects":
            if Utils.get_setting_value("sound_effects"):
                button_toggle_sound_effects.config(image=sound_off_picture)
                Utils.set_setting_value("sound_effects", False)
            elif not Utils.get_setting_value("sound_effects"):
                button_toggle_sound_effects.config(image=sound_on_picture)
                Utils.set_setting_value("sound_effects", True)

    def set_volume(volume):
        Utils.set_setting_value("volume", str(volume))
        label_volume_value.config(text=str(volume) + " %")

    def reset_config():
        Utils.button_click_sound(False)
        Utils.reset_config()

    def refresh_frame(event):
        if Utils.get_setting_value("music"):
            button_toggle_music.config(image=sound_on_picture)
        elif not Utils.get_setting_value("music"):
            button_toggle_music.config(image=sound_off_picture)

        if Utils.get_setting_value("sound_effects"):
            button_toggle_sound_effects.config(image=sound_on_picture)
        elif not Utils.get_setting_value("sound_effects"):
            button_toggle_sound_effects.config(image=sound_off_picture)

        scale_volume_control.set(Utils.get_setting_value("volume"))
        label_volume_value.config(text=Utils.get_setting_value("volume") + " %")

    # Set basic parameters of frame

    root.wm_attributes("-topmost", 1)
    root.geometry("200x200")
    root.resizable(width=False, height=False)
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))
    root.bind("<Map>", mapped_frame)

    # Add components to frame

    root.bind("<Enter>", refresh_frame)

    label_background_picture = get_picture("config_background.png")
    label_background = Label(image=label_background_picture, width=200, height=200, bd=0)
    label_background.place(x=0, y=0)

    label_title_bar_picture = get_picture("config_title_bar.png")
    label_title_bar = Label(image=label_title_bar_picture, width=200, height=30, bd=0)
    label_title_bar.place(x=0, y=0)

    label_move_area_picture = get_picture("config_move.png")
    label_move_area = Label(image=label_move_area_picture, width=28, height=28, bd=0)
    label_move_area.place(x=0, y=0)
    label_move_area.bind("<B1-Motion>", move_frame)

    label_toggle_music_picture = get_picture("config_toggle_music.png")
    label_toggle_music = Label(image=label_toggle_music_picture, width=80, height=20, bd=0)
    label_toggle_music.place(x=50, y=50)

    label_toggle_sound_effects_picture = get_picture("config_toggle_sound_effects.png")
    label_toggle_sound_effects = Label(image=label_toggle_sound_effects_picture, width=115, height=20, bd=0)
    label_toggle_sound_effects.place(x=50, y=80)

    label_reset_config_picture = get_picture("config_reset_config.png")
    label_reset_config = Label(image=label_reset_config_picture, width=70, height=15, bd=0)
    label_reset_config.place(x=56, y=132)

    label_volume = Label(text="Volume : ", font=("Segoe Script", 8), bd=0, bg="white")
    label_volume.place(x=25, y=160)

    label_volume_value = Label(text=Utils.get_setting_value("volume") + " %", font=("Segoe Script", 8),
                               bd=0, bg="white")
    label_volume_value.place(x=80, y=160)

    button_reduce_picture = get_picture("buttons\\config_reduce.png")
    button_reduce = Button(image=button_reduce_picture, bd=0, highlightthickness=0,
                           padx=32, pady=28, command=reduce_frame)
    button_reduce.place(x=140, y=0)

    button_close_picture = get_picture("buttons\\config_close.png")
    button_close = Button(image=button_close_picture, bd=0, highlightthickness=0, padx=28, pady=28, command=close_frame)
    button_close.place(x=172, y=0)

    button_toggle_music = Button(image=get_picture_for_toggle_buttons("music"), bd=0, highlightthickness=0, padx=40,
                                 pady=40, command=lambda: toggle("music"))
    button_toggle_music.place(x=25, y=50)

    button_toggle_sound_effects = Button(image=get_picture_for_toggle_buttons("sound_effects"), bd=0,
                                         highlightthickness=0, padx=40, pady=40, command=lambda: toggle("sound_effects"))
    button_toggle_sound_effects.place(x=25, y=80)

    button_reset_config_picture = get_picture("buttons\\reset_config.png")
    button_reset_config = Button(image=button_reset_config_picture, bd=0, highlightthickness=0, padx=28, pady=28,
                                 command=reset_config)
    button_reset_config.place(x=26, y=131)

    scale_volume_control = Scale(from_=1, to=100, orient=HORIZONTAL, length=140, width=10, bd=0, bg="#ba0308",
                                 activebackground="#ba0308", troughcolor="white", sliderrelief="flat", sliderlength=20,
                                 showvalue=0, highlightthickness=2, highlightbackground="black", command=set_volume)
    scale_volume_control.set(Utils.get_setting_value("volume"))
    scale_volume_control.place(x=25, y=180)

    # Loop the frame

    root.mainloop()
