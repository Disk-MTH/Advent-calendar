from tkinter import *
from PIL import Image, ImageTk
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
                picture = Image.open(Utils.get_resources_path("resources\\day\\day_" + str(day_date) + ".png"))
                resized_picture = picture.resize((700, 350), Image.ANTIALIAS)
                return ImageTk.PhotoImage(resized_picture)
            except FileNotFoundError:
                try:
                    return PhotoImage(file=Utils.get_resources_path("resources\\day\\not_found.png"))
                except TclError:
                    pass
        else:
            try:
                return PhotoImage(file=Utils.get_resources_path("resources\\" + path))
            except TclError:
                pass

    def get_title(date):
        if date == 1:
            return "December 1st"
        elif date == 2:
            return "December 2nd"
        elif date == 3:
            return "December 3rd"
        else:
            return "December " + str(date) + "th"

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
    root.iconbitmap(Utils.get_resources_path("resources\\icon\\app_icon.ico"))
    root.bind("<Map>", mapped_frame)

    # Add components to frame

    label_background = Label(bg="white", width=700, height=400, bd=0)
    label_background.place(x=0, y=0)

    label_title = Label(text=get_title(day_date), font=("Segoe Script", 18), bd=0, bg="White")
    label_title.place(x=root_width / 2 - label_title.winfo_reqwidth() / 2,
                      y=25 - label_title.winfo_reqheight() / 2)

    label_move_area_picture = get_picture("day_move.png", False)
    label_move_area = Label(image=label_move_area_picture, width=40, height=40, bd=0)
    label_move_area.place(x=5, y=5)
    label_move_area.bind("<B1-Motion>", move_frame)

    button_reduce_picture = get_picture("buttons\\day_reduce.png", False)
    button_reduce = Button(image=button_reduce_picture, bd=0, highlightthickness=0,
                           padx=40, pady=10, command=reduce_frame)
    button_reduce.place(x=610, y=20)

    button_close_picture = get_picture("buttons\\day_close.png", False)
    button_close = Button(image=button_close_picture, bd=0, highlightthickness=0, padx=40, pady=40, command=close_frame)
    button_close.place(x=655, y=5)

    label_day_picture = get_picture(day_date, True)
    label_day = Label(image=label_day_picture, width=700, height=350, bd=0)
    label_day.place(x=0, y=50)

    # Loop the frame

    root.mainloop()
