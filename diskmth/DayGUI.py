from tkinter import *
import Utils
import MainGUI


def day_gui(day_date):

    # Create the frame

    root = Tk()

    # Initialisation of some useful variables

    last_click_x = 0
    last_click_y = 0
    root_width = 700
    root_height = 400

    # Definition of some useful functions

    def get_picture(path, is_day_picture):
        if is_day_picture:
            try:
                return PhotoImage(file=Utils.get_resources_path("resources\\day\\day_" + str(day_date) + ".png"))
            except TclError:
                return PhotoImage(file=Utils.get_resources_path("resources\\day\\not_found.png"))
        else:
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
        MainGUI.main_gui()

    # Set basic parameters of frame

    root.wm_attributes("-topmost", True)
    root.geometry("700x400")
    root.resizable(width=False, height=False)
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))
    root.bind("<Map>", mapped_frame)

    # Add components to frame

    label_background = Label(bg="white", width=700, height=400, bd=0)
    label_background.place(x=0, y=0)

    # a changer
    label_move_area_picture = get_picture("main_move.png", False)
    label_move_area = Label(image=label_move_area_picture, width=50, height=50, bd=0)
    label_move_area.place(x=0, y=0)
    label_move_area.bind("<B1-Motion>", move_frame)

    # a changer
    button_reduce_picture = get_picture("buttons\\main_reduce.png", False)
    button_reduce = Button(image=button_reduce_picture, bd=0, highlightthickness=0,
                           padx=45, pady=40, command=reduce_frame)
    button_reduce.place(x=915, y=0)

    # a changer
    button_close_picture = get_picture("buttons\\main_close.png", False)
    button_close = Button(image=button_close_picture, bd=0, highlightthickness=0, padx=40, pady=40, command=close_frame)
    button_close.place(x=960, y=0)

    label_day_picture = get_picture(day_date, True)
    label_day = Label(image=label_day_picture, width=label_day_picture.width(), height=label_day_picture.height(), bd=0)
    label_day.place(x=root_width / 2 - label_day_picture.width() / 2,
                    y=root_height / 2 - label_day_picture.height() / 2 + 25)

    # Loop the frame

    root.mainloop()
