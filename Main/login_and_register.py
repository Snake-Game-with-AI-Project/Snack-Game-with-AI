from tkinter import *
import os
from PIL import ImageTk, Image
import sys
from tkinter import messagebox

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(login_screen)
    register_screen.title("Register")
    register_screen.iconbitmap("assets/snake.ico")
    
    register_screen.geometry("900x550")
    
    
    ###### Login Frame ###########
    lgn_frame = Frame(
        register_screen, bg='#DAF7A6', width='900', height='550')
    lgn_frame.pack(fill='both', expand='yes')

    txt = "Snake Game"
    headimg = Label(lgn_frame, text=txt, font=(
        'yu gothic ui', 30, 'italic', 'bold'), bg='#DAF7A6')
    headimg.place(x=80, y=30, width=300, height=30)
    
    ############### Left Side image ############

    side_image = Image.open('assets/left_img-removebg-preview.jpg')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    side_image_label.image = photo
    side_image_label.place(x=10, y=70)
    
    ############# sign in image ###############
    signin_image = Image.open(
        'assets/circle_mouse-resize-modified.png')
    photo = ImageTk.PhotoImage(signin_image)
    signin_image_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    signin_image_label.image = photo
    signin_image_label.place(x=600, y=90)

    signin_label = Label(lgn_frame, text="Sign Up",
                                bg='#DAF7A6', fg='black', font=('yu gothic ui', 15, 'italic'))
    signin_label.place(x=620, y=180)
    
    # user name entry
    
    username_label = Label(lgn_frame, text="Username",
                                    bg='#DAF7A6', fg='black', font=('yu gothic ui', 20, 'italic'))
    username_label.place(x=500, y=220)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    username_entry = Entry(lgn_frame, textvariable=username, highlightthickness=0,
                                relief=FLAT, bg='#DAF7A6', fg='black', font=('yu gothic ui', 12, 'bold'))
    username_entry.place(x=500, y=270, width=270)
    
    username_line = Canvas(
        lgn_frame, width=300, height=2.0, bg='#148863', highlightthickness=0)
    username_line.place(x=500, y=292)
    
    ############# Username Icon #############
    username_icon = Image.open(
        'assets/username_icon-removebg-preview (1).jpg')
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    username_icon_label.image = photo
    username_icon_label.place(x=475, y=270)
    
    
    
    ############# Password ##############
    password_label = Label(lgn_frame, text="Password",
                                bg='#DAF7A6', fg='black', font=('yu gothic ui', 20, 'italic'))
    password_label.place(x=500, y=320)

    # line 54 bg=#DAF7A6 to do it like a line insede box.
    password_entry = Entry(lgn_frame,show='*', textvariable=password, highlightthickness=0, relief=FLAT,
                                bg='#DAF7A6', fg='black', font=('yu gothic ui', 12, 'bold'))
    password_entry.place(x=500, y=368, width=270)

    password_line = Canvas(
        lgn_frame, width=300, height=2.0, bg='#148863', highlightthickness=0)
    password_line.place(x=499, y=390)

    ############# Password Icon #############

    password_icon = Image.open('assets/key-removebg-preview (1).jpg')
    photo = ImageTk.PhotoImage(password_icon)
    password_icon_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    password_icon_label.image = photo
    password_icon_label.place(x=476, y=368)
    
    
    ########## signup ##########
    signup = Button(lgn_frame, command=register_user, text='Sign up', font=(
        'yu gothic ui', 12, 'bold underline'), fg='white', width=25, bd=0, bg='#019875', activebackground='#b3cb23', cursor='hand2')
    signup.place(x=520, y=430)
    
        
    # back to sign in 
    back_to_login = Button(lgn_frame,command=lambda :[register_screen.withdraw(),login_screen.deiconify()], text='Back to login', font=(
        'yu gothic ui', 12, 'bold underline'), fg='white', width=25, bd=0, bg='#019875', activebackground='#b3cb23', cursor='hand2')
    back_to_login.place(x=520, y=470)

def register_user():

    username_info = username.get()
    password_info = password.get()
    location = "Main/users"
    complete_name = os.path.join(location, username_info)

    file = open(complete_name, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    x=Label(register_screen, text="Registration Success",
          fg="green",bg='#DAF7A6', font=("calibri", 11))
    x.place(x=570,y=400)
    x.after(5000,x.destroy)

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir("./Main/users")
    if username1 in list_of_files:
        location = "Main/users"
        complete_name = os.path.join(location, username1)
        file1 = open(complete_name, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            with open('user_name', 'w') as file:
                file.write(username1)
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success
def login_sucess():
    login_screen.withdraw()
    import main

# Designing popup for login invalid password
def password_not_recognised():
    response=messagebox.showerror("Error message", "Invalid Password")
    if response=='ok':
        print('invalid password')

# Designing popup for user not found
def user_not_found():
    response=messagebox.showerror("Error message", "Invalid Username")
    if response=='ok':
        print('invalid username')

# Designing Main(first) window
def login():
    global login_screen
    login_screen = Tk()
    login_screen.geometry("900x550")
    login_screen.iconbitmap("assets/snake.ico")
    login_screen.title("Login")
    
    ###### Login Frame ###########
    lgn_frame = Frame(
        login_screen, bg='#DAF7A6', width='900', height='550')
    # lgn_frame.place(x=200, y=80)
    lgn_frame.pack(fill='both', expand='yes')

    txt = "Snake Game"
    headimg = Label(lgn_frame, text=txt, font=(
        'yu gothic ui', 30, 'italic', 'bold'), bg='#DAF7A6')
    headimg.place(x=80, y=30, width=300, height=30)
    
    ############### Left Side image ############

    side_image = Image.open('assets/left_img-removebg-preview.jpg')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    side_image_label.image = photo
    side_image_label.place(x=10, y=70)
    
    ############# sign in image ###############
    signin_image = Image.open(
        'assets/circle_mouse-resize-modified.png')
    photo = ImageTk.PhotoImage(signin_image)
    signin_image_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    signin_image_label.image = photo
    signin_image_label.place(x=600, y=90)

    signin_label = Label(lgn_frame, text="Sign In",
                                bg='#DAF7A6', fg='black', font=('yu gothic ui', 15, 'italic'))
    signin_label.place(x=620, y=180)
    
    # user name entry
    
    username_label = Label(lgn_frame, text="Username",
                                    bg='#DAF7A6', fg='black', font=('yu gothic ui', 20, 'italic'))
    username_label.place(x=500, y=220)

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    
    username_login_entry = Entry(lgn_frame, textvariable=username_verify, highlightthickness=0,
                                relief=FLAT, bg='#DAF7A6', fg='black', font=('yu gothic ui', 12, 'bold'))
    username_login_entry.place(x=500, y=270, width=270)
    
    username_line = Canvas(
        lgn_frame, width=300, height=2.0, bg='#148863', highlightthickness=0)
    username_line.place(x=500, y=292)
    
    ############# Username Icon #############
    username_icon = Image.open(
        'assets/username_icon-removebg-preview (1).jpg')
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    username_icon_label.image = photo
    username_icon_label.place(x=475, y=270)
    
    ############# Password ##############
    password_label = Label(lgn_frame, text="Password",
                                bg='#DAF7A6', fg='black', font=('yu gothic ui', 20, 'italic'))
    password_label.place(x=500, y=320)

    # line 54 bg=#DAF7A6 to do it like a line insede box.
    password_login_entry = Entry(lgn_frame, show='*',textvariable=password_verify, highlightthickness=0, relief=FLAT,
                                bg='#DAF7A6', fg='black', font=('yu gothic ui', 12, 'bold'))
    password_login_entry.place(x=500, y=368, width=270)

    password_line = Canvas(
        lgn_frame, width=300, height=2.0, bg='#148863', highlightthickness=0)
    password_line.place(x=499, y=390)

    ############# Password Icon #############

    password_icon = Image.open('assets/key-removebg-preview (1).jpg')
    photo = ImageTk.PhotoImage(password_icon)
    password_icon_label = Label(
        lgn_frame, image=photo, bg='#DAF7A6')
    password_icon_label.image = photo
    password_icon_label.place(x=476, y=368)
    
    ########## login x 2##########
    login = Button(lgn_frame, command=login_verify, text='Login', font=(
        'yu gothic ui', 12, 'bold underline'), fg='white', width=25, bd=0, bg='#019875', activebackground='#b3cb23', cursor='hand2')
    login.place(x=520, y=430)
    
    ######### sign up ########

    signup_label = Label(lgn_frame, text='No account yet', font=(
        'yu gothic ui', 12, 'bold underline'), fg='#84A59D', width=25, bd=0, bg='#DAF7A6')
    signup_label.place(x=440, y=480)

    signup_button = Image.open('assets/Register.png')
    photo = ImageTk.PhotoImage(signup_button)
    signup_button_label = Button(lgn_frame, image=photo, bg='#DAF7A6', cursor='hand2', bd=0,command=lambda :[login_screen.withdraw(),register()])
    signup_button_label.image_names = photo 
    signup_button_label.place(x=630, y=480, width=111, height=35)

    login_screen.mainloop()

if __name__=='__main__':
    login()
