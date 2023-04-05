import tkinter
from tkinter import *
from tkinter import messagebox

adminlogin_window = Tk()
adminlogin_window.title('Admin Login')
adminlogin_window.geometry("925x500+300+200")
adminlogin_window.config(bg="#ECF9FF")
adminlogin_window.resizable(False, False)

#back forward button
def backfw_btn():
    adminlogin_window.withdraw()
    import main
    main.login_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=adminlogin_window)
back_forward_btn = Button(adminlogin_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)


#logo image
img_logo =tkinter.PhotoImage(file='logo.png',master=adminlogin_window)
adminlogin_window.iconphoto(False,img_logo)
Label(adminlogin_window, image=img_logo,bg="white", background="#ECF9FF").place(x=50, y=120)


frame = Frame(adminlogin_window, width=350, height=370, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="تسجيل دخول", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=100, y=5)


def on_enter(e):
    admin_email_entry.delete(0, 'end')


def on_leave(e):
    email = admin_email_entry.get()
    if email == '':
        admin_email_entry.insert(0, 'البريد الالكتروني')


admin_email_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
admin_email_entry.place(x=30, y=100)
admin_email_entry.insert(0, 'البريد الالكتروني')
admin_email_entry.bind('<FocusIn>', on_enter)
admin_email_entry.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=125)


def on_enter(e):
    admin_pass_entry.delete(0, 'end')


def on_leave(e):
    password = admin_pass_entry.get()
    if password == '':
        admin_pass_entry.insert(0, 'كلمه السر')


admin_pass_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
admin_pass_entry.place(x=30, y=180)
admin_pass_entry.insert(0, 'كلمه السر')
admin_pass_entry.bind('<FocusIn>', on_enter)
admin_pass_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=205)

def hide():
    eye_img.config(file='closedeye.png')
    admin_pass_entry.config(show='*')
    openeye_btn.config(command=show)
def show():
    eye_img.config(file='openeye.png')
    admin_pass_entry.config(show='')
    openeye_btn.config(command=hide)

eye_img = tkinter.PhotoImage(file='openeye.png',master=adminlogin_window)
openeye_btn = Button(frame,bd=0,image=eye_img,activebackground="#ECF9FF",command=hide)
openeye_btn.place(x=280, y=170)

def adminlogin():
   if admin_email_entry.get()=='البريد الالكتروني' or admin_pass_entry.get()=='كلمه السر':
       messagebox.showerror('Error', 'all fields are required')
   else:
       adminlogin_window.withdraw()
       import dashboard_admin
       dashboard_admin.admin_dashboard_window.deiconify()

btn_login = Button(frame, cursor='hand2',width=39, pady=7, text="تسجيل الدخول",
                   bg="#57a1f8", fg='white', border=0, command=adminlogin)
btn_login.place(x=35, y=250)

adminlogin_window.mainloop()