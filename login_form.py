from tkinter import *
import os
def register_user():

    username_info = username.get()
    password_info = password.get()
    file= open(username_info+".txt","w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(screen1, text="Registration Success", fg="green",font=("calibri",11)).pack()

def register():
    global screen1
    screen1= Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x256")

    global username
    global password
    global username_entry
    global password_entry
    username= StringVar()
    password= StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text= "").pack()
    Label(screen1 , text= "username * ").pack()
    username_entry= Entry(screen1, textvariable= username)
    username_entry.pack()
    Label(screen1, text= "password *").pack()
    password_entry=Entry(screen1,textvariable= password)
    password_entry.pack()
    Label(screen1, text= "").pack()
    Button(screen1, text="Register", width=10, height=1,command=register_user).pack()


def saved():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Register")
    screen8.geometry("300x256")
    Label(screen8,text="saved").pack()


def save():
    filename=raw_filename.get()
    filenote=raw_notes.get()
    file=open(filename+".txt","w")
    file.write(filenote+"\n")
    file.close()
    saved()

def create_notes():
    global raw_filename
    raw_filename=StringVar()
    global raw_notes
    raw_notes=StringVar()
    global raw_filename_entry
    global raw_notes_entry

    global screen7
    screen7 = Toplevel(screen)
    screen7.title("create notes!")
    screen7.geometry("300x256")
    Label(screen7, text="Please enter filename below").pack()
    Label(screen7, text="").pack()
    Label(screen7, text="filename * ").pack()
    raw_filename_entry = Entry(screen7, textvariable=raw_filename)
    raw_filename_entry.pack()
    Label(screen7, text="notes *").pack()
    raw_notes_entry = Entry(screen7, textvariable=raw_notes)
    raw_notes_entry.pack()
    Label(screen7, text="").pack()
    Button(screen7, text="SAVE", width=10, height=1, command=save).pack()

def view_notes1():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("notes!!")
    screen10.geometry("300x256")
    file=fil_entry.get()
    file=open(file,"r")
    filer=file.read()
    Label(screen10,text="data given below").pack()
    Label(screen10,text=filer).pack()


def view_notes():
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("view_notes")
    screen9.geometry("300x256")
    file=os.listdir()
    Label(screen9,text="please enter one of the given options").pack()
    Label(screen9,text=file).pack()
    global fil
    global fil_entry
    fil=StringVar()
    fil_entry=Entry(screen9,textvariable=fil)
    fil_entry.pack()
    Button(screen9,text="OK",command=view_notes1).pack()




def delete_notes1():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Info")
    screen10.geometry("300x256")
    file=del_entry.get()
    os.remove(file)
    Label(screen10,text=file+" removed").pack()



def delete_notes():
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("delete_notes")
    screen9.geometry("300x256")
    file=os.listdir()
    Label(screen9,text="please enter one of the given options").pack()
    Label(screen9,text=file).pack()
    global de
    global del_entry
    de=StringVar()
    del_entry=Entry(screen9,textvariable=de)
    del_entry.pack()
    Button(screen9,text="OK",command=delete_notes1).pack()


def session():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("password verification ")
    screen6.geometry("300x100")
    Label(screen6,text="dashboard").pack()
    Button(screen6, text="create notes", width=10, height=1, command=create_notes).pack()
    Button(screen6, text="view notes", width=10, height=1, command=view_notes).pack()
    Button(screen6, text="delete notes", width=10, height=1, command=delete_notes).pack()



def delete4():
    screen4.destroy()
def delete5():
    screen5.destroy()

def password_verified():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("password verification ")
    screen3.geometry("300x100")
    Label(screen3,text="password verified").pack()
    Button(screen3,text="OK",command=session).pack()

def password_unverified():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("password error")
    screen4.geometry("300x100")
    Label(screen4,text="password error").pack()
    Button(screen4,text="OK",command=delete4()).pack()

def user_notfound():
    global screen5
    screen5=Toplevel(screen)
    screen.title("user not allowed!")
    screen5.geometry("300x100")
    Label(screen5,text="user not found").pack()
    Button(screen5,text="OK",command=delete5).pack()

def login_verify():

    userid = username_verify.get()

    passw= password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    list_of_dir = os.listdir()
    userid=userid +".txt"
    if userid in list_of_dir:
        files = open(userid, "r")
        verify= files.read().splitlines()

        if passw in verify:
            password_verified()
        else:
            password_unverified()
    else:
        user_notfound()




def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login details")
    screen2.geometry("300x256")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify=StringVar()
    password_verify=StringVar()
    Label(screen2 ,text="Please enter login details").pack()
    Label(screen2, text="").pack()
    Label(screen2,text="username *").pack()
    username_entry1= Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="")
    Button(screen2, text="login",width=10,height=1,command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0",bg="grey",width="300",height="2",font=("calibri",13)).pack()
    Label(text= "").pack()
    Button(text="Login",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Register",height="2", width="30",command=register).pack()
    screen.mainloop()

main_screen()


