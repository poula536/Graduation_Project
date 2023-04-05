import tkinter
from tkinter import *
from tkinter import messagebox

new_admin_window = Tk()
new_admin_window.title('Add Admin')
new_admin_window.geometry("925x500+300+200")
new_admin_window.config(bg="#ECF9FF")
new_admin_window.resizable(False, False)

#back forward button
def backfw_btn():
    new_admin_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=new_admin_window)
back_forward_btn = Button(new_admin_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)


img_logo = tkinter.PhotoImage(file='logo.png',master=new_admin_window)
Label(new_admin_window, bg="white",image=img_logo ,background="#ECF9FF").place(x=50, y=120)
frame = Frame(new_admin_window, width=350, height=400, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="انشاء حساب جديد", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=100, y=10)


def on_enter(e):
    newadmin_email_entry.delete(0, 'end')


def on_leave(e):
    name = newadmin_email_entry.get()
    if name == '':
        newadmin_email_entry.insert(0, 'عنوان البريد الالكتروني')


newadmin_email_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
newadmin_email_entry.place(x=30, y=95)
newadmin_email_entry.insert(0, 'عنوان البريد الالكتروني')
newadmin_email_entry.bind('<FocusIn>', on_enter)
newadmin_email_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=120)


def on_enter(e):
    admin_username_entry.delete(0, 'end')


def on_leave(e):
    teacher_name = admin_username_entry.get()
    if teacher_name == '':
        admin_username_entry.insert(0, 'اسم المستخدم')


admin_username_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
admin_username_entry.place(x=30, y=145)
admin_username_entry.insert(0, 'اسم المستخدم')
admin_username_entry.bind('<FocusIn>', on_enter)
admin_username_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=173)


def on_enter(e):
    institute_entry.delete(0, 'end')


def on_leave(e):
    institute_name = institute_entry.get()
    if institute_name == '':
        institute_entry.insert(0, 'اسم المعهد')


institute_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=30, y=200)
institute_entry.insert(0, 'اسم المعهد')
institute_entry.bind('<FocusIn>', on_enter)
institute_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=230)

#password

def on_enter(e):
    password_entry.delete(0, 'end')


def on_leave(e):
    password = password_entry.get()
    if password == '':
        password_entry.insert(0, 'كلمه السر')


password_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
password_entry.place(x=30, y=254)
password_entry.insert(0, 'كلمه السر')
password_entry.bind('<FocusIn>', on_enter)
password_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=280)


def on_enter(e):
    conf_pass_entry.delete(0, 'end')


def on_leave(e):
    confirm_password = conf_pass_entry.get()
    if confirm_password == '':
        conf_pass_entry.insert(0, 'تاكيد كلمه السر')


conf_pass_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
conf_pass_entry.place(x=30, y=305)
conf_pass_entry.insert(0, 'تاكيد كلمه السر')
conf_pass_entry.bind('<FocusIn>', on_enter)
conf_pass_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=330)
#End password

def clear():
    newadmin_email_entry.delete(0,END)
    newadmin_email_entry.insert(0,'عنوان البريد الالكتروني')

    conf_pass_entry.delete(0, END)
    conf_pass_entry.insert(0,'تاكيد كلمه السر')

    password_entry.delete(0, END)
    password_entry.insert(0,'كلمه السر')

    institute_entry.delete(0, END)
    institute_entry.insert(0,'اسم المعهد')

    admin_username_entry.delete(0, END)
    admin_username_entry.insert(0,'اسم المستخدم')


def creat_account():
    if newadmin_email_entry.get()=='عنوان البريد الالكتروني' or password_entry.get()=='كلمه السر' or conf_pass_entry.get()=='تاكيد كلمه السر' or institute_entry.get()=='اسم المعهد' or admin_username_entry.get()=='اسم المستخدم':
        messagebox.showerror('Error', 'all fields are required')
    elif password_entry.get()!= conf_pass_entry.get():
        messagebox.showerror('Error','Password must be the same')
    else:
        messagebox.showinfo('Done', 'Registration is done successfully')
        clear()


btn_login = Button(frame, cursor='hand2',width=39, pady=7, text="انشاء الحساب ",
                   bg="#57a1f8", fg='white', border=0,command=creat_account)
btn_login.place(x=35, y=360)

new_admin_window.mainloop()