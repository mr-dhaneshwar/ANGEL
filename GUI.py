from tkinter import *
from Face_lock import *
from threading import *

theme = 'Light'


def change_theme():
    global theme
    if theme == 'Light':
        c = 'Black'
        bglb.configure(bg=c)
        theme_check.configure(bg=c)
        name_lb.configure(bg=c)
        silent_button.configure(bg=c)
        start_button.configure(bg=c)
        try:
            my_frame.configure(bg=c)
            clr_button.configure(bg=c)
            f_label.configure(bg=c)
            close_button.configure(bg=c)
            status.configure(bg=c)
            anime.configure(bg=c)
            scrollbar.configure(bg=c)
            output.configure(bg=c, fg='White', insertbackground='White')

        except Exception as e:
            print("error converting dark theme", e)
        theme = 'Dark'
    else:
        c = 'White'
        bglb.configure(bg=c)
        theme_check.configure(bg=c)
        silent_button.configure(bg=c)
        name_lb.configure(bg=c)
        start_button.configure(bg=c, fg='Blue')
        try:
            my_frame.configure(bg=c)
            clr_button.configure(bg=c)
            f_label.configure(bg=c)
            close_button.configure(bg=c)
            status.configure(bg=c)
            anime.configure(bg=c)
            scrollbar.configure(bg=c)
            output.configure(bg=c, fg='Black', insertbackground='Black')


        except Exception as e:
            print("error converting dark theme", e)
        theme = 'Light'


def off_speak():
    global speak_status

    if speak_status == 1:
        speak_status = 0
        silent_button.configure(image=sound_png)
        return False
    else:
        speak_status = 1
        silent_button.configure(image=silence_png)
        return True


def speak_check():
    if speak_status == 1:
        return True
    else:
        return False


def write(text):
    # print(text+'\n')
    output.insert('end', text + '\n')


def close():
    my_frame.destroy()


def clear():
    output.delete(1.0, END)


def change_leble(line, no):
    global status, anime, my_frame, art_img
    status.configure(text=line)
    anime.configure(image=art_img[no])


location = 'D:\\Project\\Angel\\image\\'


def new_frame(main):
    global my_frame, f_label, scrollbar, output, broom_png, clr_button, close_button, close_png, smile_png, anime, t
    global confused_png, gotit_png, idea_png, listening_png, love_png, status, location, art_img

    if theme == "Dark":
        c = 'Black'
        fc = 'White'
    else:
        c = 'White'
        fc = 'Black'

    my_frame = Frame(root, width=1100, height=700, bg=c, relief=GROOVE, borderwidth=8)
    my_frame.place(x=100, y=0)

    broom_png = PhotoImage(file=location + "clean.png")
    clr_button = Button(my_frame, image=broom_png, relief=GROOVE, bg=c, command=clear)
    clr_button.place(x=250, y=8)

    status = Label(my_frame, text='connecting....', bg=c, fg='Red', font=('Arial', 12))
    status.place(x=70, y=400)

    smile_png = PhotoImage(file=location + "smile.png")
    confused_png = PhotoImage(file=location + "confused.png")
    gotit_png = PhotoImage(file=location + "gotit.png")
    idea_png = PhotoImage(file=location + "idea.png")
    listening_png = PhotoImage(file=location + "listening.png")
    love_png = PhotoImage(file=location + "love.png")
    art_img = ["", smile_png, confused_png, gotit_png, idea_png, listening_png, love_png]

    anime = Label(my_frame, image=smile_png, height=220, width=220, bg=c)
    anime.place(x=10, y=460)

    f_label = Label(my_frame, relief=GROOVE, height=2, width=63, borderwidth=2,
                    text='Automated Network Generating Expert Logic  ( ANGEL )', bg=c, fg='Red', font=('Arial', 12))
    f_label.place(x=305, y=5)

    t = Thread(target=main)
    t.start()

    close_png = PhotoImage(file=location + "close.png")
    close_button = Button(my_frame, image=close_png, relief=GROOVE, bg=c, command=close)
    close_button.place(x=1010, y=8)

    scrollbar = Scrollbar(my_frame, orient=VERTICAL)
    scrollbar.place(x=1065, relheight=1)

    output = Text(my_frame, bg=c, fg=fc, insertbackground=fc, height=24, width=80, relief=GROOVE, borderwidth=2,
                  yscrollcommand=scrollbar.set, font=('Segoe UI', 11))
    output.place(x=250, y=65)
    scrollbar.config(command=output.yview)
    output.config(yscrollcommand=scrollbar.set)


speak_status = 1


def my_window(main):
    global bglb, theme_check, name_lb, silence_png, silent_button, start_button, speak_status, sound_png, root
    root = Tk()
    root.geometry('1200x700')
    root.minsize(1200, 700)
    root.maxsize(1200, 700)
    root.title('ANGEL_2.0')
    # root.wm_iconbitmap("D:\\Project\\Angel\\image\\Angel icon.png")

    # implementing face lock system
    # if not os.listdir('samples'):
    #     print('no face samples')
    #     face_sample()   #take face samples
    #     face_train()    #train face model
    # else:
    #     if face_match():    #recognize face
    #         speak('welcome sir')

    photo = PhotoImage(file=location + "background.png")
    bglb = Label(root, image=photo)
    bglb.place(relwidth=1, relheight=1)

    theme_check = Checkbutton(root, text='Dark Theme', command=change_theme, fg='Blue')
    theme_check.pack(anchor=W, padx=5, pady=10)

    silence_png = PhotoImage(file=location + "silence.png")
    sound_png = PhotoImage(file=location + "sound.png")
    silent_button = Button(root, image=silence_png, relief=GROOVE, borderwidth=2, command=off_speak)
    silent_button.pack(anchor=W, padx=40)

    name_lb = Label(root, text='A\nN\nG\nE\nL', font=('Arial', 40), fg='Blue')
    name_lb.pack(anchor=W, padx=30, pady=10)

    start_button = Button(root, text='Start', font=('Arial', 12), relief=GROOVE, fg='Blue', borderwidth=10, height=2,
                          width=5, command=lambda: new_frame(main))
    start_button.place(x=800, y=372)
    root.mainloop()
