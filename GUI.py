from tkinter import *
from Face_lock import *
from threading import *
from login import*
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import ImageTk, Image

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


location = 'image\\'


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


def set_user():
    use = user.get().lower()
    pas = code.get()
    nam = name.get()
    date = dob.get()

    print(date)

    if use == '':
        messagebox.showerror("Invalid","pleste enter Username")
    elif pas == '':
        messagebox.showerror("Invalid","pleste enter Passwors")
    elif nam == '':
        messagebox.showerror("Invalid","pleste enter Name")
    elif date == ''or date == None:
        messagebox.showerror("Invalid","pleste enter Date of birth")
    elif singup(use,pas,nam,date) == 1:
        messagebox.showinfo("singed in", 'Account created succesfull')
        signin_frame(2)
    elif singup(use,pas,nam,date) == 2:
        messagebox.showinfo("Exist",'User already exist')
    else:
        messagebox.showerror("Invalid","Somthing went wrong")


def get_user():
    use = user.get().lower()
    pas = code.get()
    if use == '':
        messagebox.showerror("Invalid","pleste enter Username")
    elif pas == '':
        messagebox.showerror("Invalid","pleste enter Passwors")
    elif singin(use,pas) == 1:
        messagebox.showinfo("loged in", 'login succesfull')
        signin_frame(4)
    else:
        msg = singin(use,pas)
        if msg == 2:
            messagebox.showerror("Invalid", 'invalid password')
        else:
            messagebox.showerror("Invalid", "Username not found please Sing Up")

def forgot_pass():
    use = user.get().lower()
    date = dob.get()
    pas = code.get()

    if use == '':
        messagebox.showerror("Invalid","pleste enter Username")
    elif date == ''or date == None:
        messagebox.showerror("Invalid","pleste Select Date of birth")
    elif forgot(use,date) == 2:
        messagebox.showerror("Invalid",'invalid credentials')
    elif pas == '':
        messagebox.showerror("Invalid","pleste enter new Passwors")
    elif forgot(use, date, pas) == 1:
        messagebox.showinfo("Succes",'Password reset succesfully')
        signin_frame(2)


def signin_frame(step):
    global logframe, name, user, code, dob
    try:
        logframe.destroy()
    except Exception as e:
        print('problem in sing in frame',e)
    logframe = Frame(root, width=1200, height=700, relief=GROOVE, borderwidth=8)
    logframe.place(x=0,y=0)

    logbglb = Label(logframe, image=logbgimg)
    logbglb.place(relheight=1,relwidth=1)

    Label(logframe,border=0,text='Welcome', bg='#ab23ff',fg="white",font=('Times',40,'bold',)).place(x=470,y=10)

    frame =Frame(logframe,width=500,height=500,bg="white")
    frame.place(x=350,y=100)

    if step == 1:
        
        heading=Label(frame,text='Sign Up',fg="#57a1f8",bg='white',font=('Times',25,'bold'))
        heading.place(x=170,y=5)

        namelb = Label(frame,text='Name: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        namelb.place(x=20, y=70)
        name= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        name.place(x=180,y=80)

        Frame(frame,width=300,height=2,bg='black').place(x=180,y=110)

        userlb = Label(frame,text='Username: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        userlb.place(x=20, y=150)
        user= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        user.place(x=180,y=160)

        Frame(frame,width=300,height=2,bg='black').place(x=180,y=190)

        codelb = Label(frame,text='Password: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        codelb.place(x=20, y=230)
        code= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        code.place(x=180,y=240)
    
        Frame(frame,width=300,height=2,bg='black').place(x=180,y=270)

        doblb = Label(frame,text='DOB: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        doblb.place(x=20, y=310)

        dob = DateEntry(frame, date_pattern='yyyy-mm-dd', firstweekday='sunday', locale='en_US', width=27,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
        dob.place(x=180,y=320)
    
        Frame(frame,width=300,height=2,bg='black').place(x=180,y=350)

        sinupgbt = Button(frame,width=15,pady=7,text="Sign Up", cursor='hand2', font=('Times',15,'bold'),bg="#57a1f8",fg='white', relief=GROOVE,command=set_user)
        sinupgbt.place(x=150,y=370)

        qlb1=Label(frame,text="Already have account? -->",fg='black',bg='white',font=('Microsoft YaHei UI Light',12))
        qlb1.place(x=70,y=450)

        sign_inbt=Button(frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg="#57a1f7",command=lambda:signin_frame(2), font=('Microsoft YaHei UI Light',12))
        sign_inbt.place(x=330,y=445)

    elif step == 2:
    
        heading=Label(frame,text='Sign In',fg="#57a1f8",bg='white',font=('Times',25,'bold'))
        heading.place(x=170,y=5)

        userlb = Label(frame,text='Username: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        userlb.place(x=20, y=90)
        user= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        user.place(x=180,y=100)

        Frame(frame,width=300,height=2,bg='black').place(x=180,y=130)

        codelb = Label(frame,text='Password: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        codelb.place(x=20, y=170)
        code= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        code.place(x=180,y=180)
    
        Frame(frame,width=300,height=2,bg='black').place(x=180,y=210)

        singbt = Button(frame,width=15,pady=7,text="Sign in", cursor='hand2', font=('Times',15,'bold'),bg="#57a1f8",fg='white', relief=GROOVE,command=get_user)
        singbt.place(x=150,y=270)

        qlb1=Label(frame,text="Forgot Password? -->",fg='black',bg='white',font=('Microsoft YaHei UI Light',12))
        qlb1.place(x=70,y=400)

        forgot=Button(frame,width=14,text='Forgot Password',border=0,bg='white',cursor='hand2',fg="#57a1f7",command=lambda:signin_frame(3), font=('Microsoft YaHei UI Light',12))
        forgot.place(x=280,y=395)

        qlb2=Label(frame,text="Don't have account? -->",fg='black',bg='white',font=('Microsoft YaHei UI Light',12))
        qlb2.place(x=70,y=450)

        sign_upbt=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg="#57a1f7",command=lambda:signin_frame(1), font=('Microsoft YaHei UI Light',12))
        sign_upbt.place(x=310,y=445)

    elif step == 3:
        heading=Label(frame,text='Forgot !',fg="#57a1f8",bg='white',font=('Times',25,'bold'))
        heading.place(x=170,y=5)

        userlb = Label(frame,text='Username: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        userlb.place(x=20, y=150)
        user= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        user.place(x=180,y=160)

        Frame(frame,width=300,height=2,bg='black').place(x=180,y=190)

        doblb = Label(frame,text='DOB: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        doblb.place(x=20, y=230)
        dob = DateEntry(frame, date_pattern='yyyy-mm-dd', firstweekday='sunday', locale='en_US', width=27,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
        dob.place(x=180, y=240)

        Frame(frame,width=300,height=2,bg='black').place(x=180,y=270)

        codelb = Label(frame,text='New Password: ', fg="#57a1f8",bg='white',font=('Times',18,'bold'))
        codelb.place(x=20, y=310)
        code= Entry(frame,width=25,fg='black',border=0,bg='White',font=('Microsoft YaHei UI Light',11))
        code.place(x=230, y=320)
    
        Frame(frame,width=250,height=2,bg='black').place(x=230,y=350)

        resetbt = Button(frame,width=15,pady=7,text="Reset", cursor='hand2', font=('Times',15,'bold'),bg="#57a1f8",fg='white', relief=GROOVE,command=forgot_pass)
        resetbt.place(x=140,y=380)


        qlb1=Label(frame,text="Return to singin -->",fg='black',bg='white',font=('Microsoft YaHei UI Light',12))
        qlb1.place(x=70,y=450)

        sign_inbt=Button(frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg="#57a1f7",command=lambda:signin_frame(2), font=('Microsoft YaHei UI Light',12))
        sign_inbt.place(x=270,y=445)

    elif step == 4:
        heading=Label(frame,text='Add Face lock',fg="#57a1f8",bg='white',font=('Times',25,'bold'))
        heading.place(x=130,y=50)
    
        facebt = Button(frame, image=facegbgimg, relief=GROOVE, cursor='hand2', borderwidth=10, bg='White', command= lambda:face(1))
        facebt.place(x=150,y=150)

        notelb = Label(frame,text="Note--> Stay in the light and look into the Camera",fg='red',bg='white',font=('Microsoft YaHei UI Light',12))
        notelb.place(x=20, y=400)

def face(op):
    if op == 1:
        reset_face()
        face_sample()   #take face samples
        face_train()    #train face model
        logframe.destroy()
    else:
        reset_face()
        signin_frame(2)

speak_status = 1


def my_window(main):
    global bglb, theme_check, name_lb, silence_png, silent_button, start_button, speak_status, sound_png, root, photo, logbgimg, facegbgimg
    root = Tk()
    root.geometry('1200x700')
    root.resizable(False,False)
    root.title('ANGEL_2.0')
    logo = PhotoImage(file="image\\logo.png")
    root.iconphoto(False, logo)

    if os.listdir('samples'):
        if face_match():
            print('welcome')
        else:
            signin_frame(4)
            
    logbgopen = Image.open('image\\login bg.png') #login page background
    # resize image
    resized = logbgopen.resize((1200, 700), Image.LANCZOS)
    logbgimg = ImageTk.PhotoImage(resized)

    facebgopen = Image.open('image\\face-id.png') #login page background
    # resize image
    resized = facebgopen.resize((200, 200), Image.LANCZOS)
    facegbgimg = ImageTk.PhotoImage(resized)

    photo = PhotoImage(file=location + "background.png")
    bglb = Label(root, image=photo)
    bglb.place(relwidth=1, relheight=1)

    theme_check = Checkbutton(root, text='Dark Theme', command=change_theme, fg='Blue')
    theme_check.pack(anchor=W, padx=5, pady=10)

    silence_png = PhotoImage(file=location + "silence.png")
    sound_png = PhotoImage(file=location + "sound.png")
    silent_button = Button(root, image=silence_png, relief=GROOVE, borderwidth=2, command=off_speak)
    silent_button.pack(anchor=W, padx=40)

    logoutbt = Button(root, text='Logout', cursor='hand2', font=('Times',12,'bold'),bg="red",fg='white', relief=GROOVE,command=lambda:face(2))
    logoutbt.place(x=1110, y=10)

    name_lb = Label(root, text='A\nN\nG\nE\nL', font=('Arial', 40), fg='Blue')
    name_lb.pack(anchor=W, padx=30, pady=10)

    start_button = Button(root, text='Start', font=('Arial', 12), relief=GROOVE, fg='Blue', borderwidth=10, height=2,
                          width=5, command=lambda: new_frame(main))
    start_button.place(x=800, y=372)

    # implementing face lock system
    
    # if not os.listdir('samples'):
    #     print('no face samples')
    #     face_sample()   #take face samples
    #     face_train()    #train face model
    # else:
    #     if face_match():    #recognize face
    #         print('welcome sir...')

    if not os.listdir('samples'):
        signin_frame(2)
    root.mainloop()