from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def pageopen():
    import signupGUI

root=Tk()
root.title('Login form')
root.geometry('1000x600')
root.configure(bg="#57a1f8")
root.resizable(False,False)

# background = Image.open('back.jpg')
# # resize image
# resized = background.resize((1000, 800), Image.ANTIALIAS)
# bck_end = ImageTk.PhotoImage(resized)
# lable = Label(root, image=bck_end)
# lable.place(x=0, y=0)

def signin():
    username=user.get()
    password=code.get()

    if username=='shyam' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg='white')


        screen.mainloop()

    elif username!="admin" and password!='1234':
        messagebox.showerror("Invalid","invalid username and password")

    elif password!='1234':
        messagebox.showerror("Invalid", "invalid password!")
    elif username!='admin':
        messagebox.showerror("Invalid", "invalid username!")

# img=PhotoImage(file="casino.png")
# #x=root.bitmap(r'online-game.ico')
# Label(root,border=0,image=img,background='#57a1f8').place(x=30,y=70)

Label(root,border=0,text='Welcome',background='#57a1f8',fg='red',font=('Times',90,'bold',)).place(x=450,y=20)

frame=Frame(root,width=350,height=350,bg="white")

frame.place(x=550,y=150)
heading=Label(frame,text='sign in',fg="#57a1f8",bg='white',font=('Times',25,'bold'))
heading.place(x=105,y=5)
########################____________________________________
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#####################________________________________________
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
###---------------------------------
Button(frame,width=39,pady=7,text="sign in",bg="#57a1f8",fg='white',border=0,command=signin).place(x=35,y=204)
lable=Label(frame,text="don't have account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
lable.place(x=110,y=270)

sign_up=Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg="#57a1f7",command=pageopen)
sign_up.place(x=60,y=270)
root.mainloop()

#watch from 12 minite