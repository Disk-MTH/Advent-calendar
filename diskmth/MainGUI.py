from tkinter import *
import Utils
import ConfigGUI
import DayGUI


def main_gui():
    # Create the frame

    root = Tk()

    # Initialisation of some useful variables

    last_click_x = 0
    last_click_y = 0

    # Definition of some useful functions

    def get_picture(path):
        try:
            return PhotoImage(file=Utils.get_resources_path("resources\\" + path))
        except TclError:
            pass

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

    def open_config():
        Utils.button_click_sound(False)
        close_frame()
        ConfigGUI.config_gui()

    def open_day_gui(day_date):
        Utils.button_click_sound(True)
        close_frame()
        DayGUI.day_gui(day_date)

    def create_a_button(picture, day_date):
        return Button(image=picture, bd=0, highlightthickness=0, padx=67, pady=67,
                      command=lambda: open_day_gui(day_date))

    # Set basic parameters of frame

    root.wm_attributes("-topmost", True)
    root.geometry("1000x650")
    root.resizable(width=False, height=False)
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))
    root.bind("<Map>", mapped_frame)

    # Add components to frame

    label_background_picture = get_picture("main_background.png")
    label_background = Label(image=label_background_picture, width=1000, height=650, bd=0)
    label_background.place(x=0, y=0)

    label_title_bar_picture = get_picture("main_title_bar.png")
    label_title_bar = Label(image=label_title_bar_picture, width=1000, height=45, bd=0)
    label_title_bar.place(x=0, y=0)

    try:
        label_credit_picture = get_picture("main_credits.png")
        label_credit = Label(image=label_credit_picture, width=198, height=50, bd=0)
        label_credit.place(x=800, y=600)
    except UnboundLocalError:
        pass

    label_move_area_picture = get_picture("main_move.png")
    label_move_area = Label(image=label_move_area_picture, width=43, height=43, bd=0)
    label_move_area.place(x=0, y=0)
    label_move_area.bind("<B1-Motion>", move_frame)

    button_config_picture = get_picture("buttons\\main_config.png")
    button_button_config = Button(image=button_config_picture, bd=0,
                                  highlightthickness=0, padx=35, pady=40, command=open_config)
    button_button_config.place(x=875, y=0)

    button_reduce_picture = get_picture("buttons\\main_reduce.png")
    button_reduce = Button(image=button_reduce_picture, bd=0,
                           highlightthickness=0, padx=45, pady=40, command=reduce_frame)
    button_reduce.place(x=915, y=0)

    button_close_picture = get_picture("buttons\\main_close.png")
    button_close = Button(image=button_close_picture, bd=0,
                          highlightthickness=0, padx=40, pady=40, command=close_frame)
    button_close.place(x=960, y=0)

    button_day_1_picture = get_picture("buttons\\days\\button_day_1.png")
    button_day_1 = create_a_button(button_day_1_picture, 1)
    button_day_1.place(x=547, y=68)

    button_day_2_picture = get_picture("buttons\\days\\button_day_2.png")
    button_day_2 = create_a_button(button_day_2_picture, 2)
    button_day_2.place(x=48, y=213)

    button_day_3_picture = get_picture("buttons\\days\\button_day_3.png")
    button_day_3 = create_a_button(button_day_3_picture, 3)
    button_day_3.place(x=214, y=213)

    button_day_4_picture = get_picture("buttons\\days\\button_day_4.png")
    button_day_4 = create_a_button(button_day_4_picture, 4)
    button_day_4.place(x=381, y=362)

    button_day_5_picture = get_picture("buttons\\days\\button_day_5.png")
    button_day_5 = create_a_button(button_day_5_picture, 5)
    button_day_5.place(x=381, y=511)

    button_day_6_picture = get_picture("buttons\\days\\button_day_6.png")
    button_day_6 = create_a_button(button_day_6_picture, 6)
    button_day_6.place(x=548, y=218)

    button_day_7_picture = get_picture("buttons\\days\\button_day_7.png")
    button_day_7 = create_a_button(button_day_7_picture, 7)
    button_day_7.place(x=712, y=67)

    button_day_8_picture = get_picture("buttons\\days\\button_day_8.png")
    button_day_8 = create_a_button(button_day_8_picture, 8)
    button_day_8.place(x=547, y=360)

    button_day_9_picture = get_picture("buttons\\days\\button_day_9.png")
    button_day_9 = create_a_button(button_day_9_picture, 9)
    button_day_9.place(x=214, y=506)

    button_day_10_picture = get_picture("buttons\\days\\button_day_10.png")
    button_day_10 = create_a_button(button_day_10_picture, 10)
    button_day_10.place(x=712, y=360)

    button_day_11_picture = get_picture("buttons\\days\\button_day_11.png")
    button_day_11 = create_a_button(button_day_11_picture, 11)
    button_day_11.place(x=48, y=506)

    button_day_12_picture = get_picture("buttons\\days\\button_day_12.png")
    button_day_12 = create_a_button(button_day_12_picture, 12)
    button_day_12.place(x=880, y=219)

    button_day_13_picture = get_picture("buttons\\days\\button_day_13.png")
    button_day_13 = create_a_button(button_day_13_picture, 13)
    button_day_13.place(x=880, y=360)

    button_day_14_picture = get_picture("buttons\\days\\button_day_14.png")
    button_day_14 = create_a_button(button_day_14_picture, 14)
    button_day_14.place(x=713, y=214)

    button_day_15_picture = get_picture("buttons\\days\\button_day_15.png")
    button_day_15 = create_a_button(button_day_15_picture, 15)
    button_day_15.place(x=380, y=67)

    button_day_16_picture = get_picture("buttons\\days\\button_day_16.png")
    button_day_16 = create_a_button(button_day_16_picture, 16)
    button_day_16.place(x=213, y=358)

    button_day_17_picture = get_picture("buttons\\days\\button_day_17.png")
    button_day_17 = create_a_button(button_day_17_picture, 17)
    button_day_17.place(x=879, y=67)

    button_day_18_picture = get_picture("buttons\\days\\button_day_18.png")
    button_day_18 = create_a_button(button_day_18_picture, 18)
    button_day_18.place(x=49, y=361)

    button_day_19_picture = get_picture("buttons\\days\\button_day_19.png")
    button_day_19 = create_a_button(button_day_19_picture, 19)
    button_day_19.place(x=381, y=213)

    button_day_20_picture = get_picture("buttons\\days\\button_day_20.png")
    button_day_20 = create_a_button(button_day_20_picture, 20)
    button_day_20.place(x=214, y=68)

    button_day_21_picture = get_picture("buttons\\days\\button_day_21.png")
    button_day_21 = create_a_button(button_day_21_picture, 21)
    button_day_21.place(x=48, y=68)

    button_day_22_picture = get_picture("buttons\\days\\button_day_22.png")
    button_day_22 = create_a_button(button_day_22_picture, 22)
    button_day_22.place(x=712, y=506)

    button_day_23_picture = get_picture("buttons\\days\\button_day_23.png")
    button_day_23 = create_a_button(button_day_23_picture, 23)
    button_day_23.place(x=877, y=505)

    button_day_24_picture = get_picture("buttons\\days\\button_day_24.png")
    button_day_24 = create_a_button(button_day_24_picture, 24)
    button_day_24.place(x=547, y=510)

    # Loop the frame

    root.mainloop()
