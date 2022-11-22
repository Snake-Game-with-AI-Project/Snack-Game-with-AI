from tkinter import *
from PIL import ImageTk,Image # pip install pillow
from tkVideoPlayer import TkinterVideo
import pygame



root= Toplevel() #create a window

############### Left Side image ############

side_image = Image.open('assets/left_img-removebg-preview.jpg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(root,image=photo, bg='#DAF7A6')
side_image_label.image = photo
side_image_label.place(x=10, y=70)

root.title("Snake Game") # Add title

# Add icon
root.iconbitmap("assets/snake.ico")

root.geometry("900x550") # Window geometry
root.configure(bg='#DAF7A6')

# Add music
pygame.mixer.init()

# Add Text
# my_label1= Label(root,text="Welcome to snake game",font=('Arial',30),bg='#DAF7A6')
# my_label1.place(anchor=CENTER, relx=0.5,rely=0.1)

txt = "Snake Game"
headimg = Label(root,text=txt, font=(
    'yu gothic ui', 30, 'italic', 'bold'), bg='#DAF7A6')
headimg.pack(pady=20)

pygame.mixer.music.load("assets/music.mp3")
# Add music
def play_music():
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)
def stop_music():
    pygame.mixer.music.stop()
def low_music():
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

def option1():
    root.withdraw() # Destroy root window
    top= Toplevel() # New Window
    top.title('Snake Game with Camera')
    top.iconbitmap("assets/snake.ico")
    top.geometry("900x550") # Window geometry
    
    top.configure(bg='#DAF7A6')
    # Add Text
    
    txt = "Play Game Using AI"
    headimg = Label(top,text=txt, font=(
    'yu gothic ui', 30, 'italic', 'bold'), bg='#DAF7A6')
    headimg.pack(pady=20)
    
    side_image = Image.open('assets\AI.png')
    resize_7= resize_img(side_image,300,300)
    photo = ImageTk.PhotoImage(resize_7)
    side_image_label = Label(top,image=photo, bg='#DAF7A6')
    side_image_label.image = photo
    side_image_label.place(anchor=CENTER,relx=0.5, rely=0.75)

    def destroy_window():
        top.withdraw()
        root.deiconify()
    def tutorial():
        videoplayer = TkinterVideo(master=top, scaled=True)
        videoplayer.load(r"assets/video.mp4")
        videoplayer.place(anchor=CENTER,relx=0.5,rely=0.75,width=600,height=300)
        videoplayer.after(10000,videoplayer.destroy)

        videoplayer.play() # play the video
    def play():
        import game_with_camera
    
    watch_tut_img = Image.open('assets/button_watch-tutorial.png')
    resize_8= resize_img(watch_tut_img,200,50)
    img8 = ImageTk.PhotoImage(resize_8)
    side_image_label8 = Button(top,image=img8,command=tutorial,borderwidth=0,activebackground='#DAF7A6', bg='#DAF7A6',cursor="hand2")
    side_image_label8.image = img8
    side_image_label8.place(anchor=CENTER,relx=0.3, rely=0.3)
    
    
    start_game_img = Image.open('assets/button_start-the-game.png')
    resize_9= resize_img(start_game_img,200,50)
    img9 = ImageTk.PhotoImage(resize_9)
    side_image_label9 = Button(top,image=img9,command=play,borderwidth=0,activebackground='#DAF7A6', bg='#DAF7A6',cursor="hand2")
    side_image_label9.image = img9
    side_image_label9.place(anchor=CENTER,relx=0.7, rely=0.3)
    
    
    back_img = Image.open('assets\previous.png')
    resize_10= resize_img(back_img,50,50)
    img10 = ImageTk.PhotoImage(resize_10)
    side_image_label10 = Button(top,image=img10,command=destroy_window,borderwidth=0,activebackground='#DAF7A6', bg='#DAF7A6',cursor="hand2")
    side_image_label10.image = img10
    side_image_label10.place(anchor=CENTER,relx=0.04, rely=0.1)
    
    music_img=Image.open('assets\high_volume.png')
    resize_4=resize_img(music_img,25,25)
    img4 = ImageTk.PhotoImage(resize_4)
    m=Button(top,image=img4,command=play_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2")
    m.image=img4
    m.place(anchor=CENTER, relx=0.97,rely=0.95)

    low_music_img=Image.open('assets\low_volume.png')
    resize_5=resize_img(low_music_img,25,25)
    img5 = ImageTk.PhotoImage(resize_5)
    x=Button(top,image=img5,command=low_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2")
    x.image=img5
    x.place(anchor=CENTER, relx=0.92,rely=0.95)

    mute_music_img=Image.open('assets\mute.png')
    resize_6=resize_img(mute_music_img,25,25)
    img6 = ImageTk.PhotoImage(resize_6)
    z=Button(top,image=img6,command=stop_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2")
    z.image=img6
    z.place(anchor=CENTER, relx=0.87,rely=0.95)
    
    
    
def option2():
    root.withdraw() # Destroy root window
    top= Toplevel() # New Window
    top.title('Snake Game with Keyborad')
    top.iconbitmap("assets/snake.ico")
    top.geometry("900x550") # Window geometry
    
    top.configure(bg='#DAF7A6')
    # Add Text
    
    txt = "Play Game Using Keyboard"
    headimg = Label(top,text=txt, font=(
    'yu gothic ui', 30, 'italic', 'bold'), bg='#DAF7A6')
    headimg.pack(pady=20)
    
    side_image = Image.open('assets/buttons.png')
    resize_7= resize_img(side_image,300,300)
    photo = ImageTk.PhotoImage(resize_7)
    side_image_label = Label(top,image=photo, bg='#DAF7A6')
    side_image_label.image = photo
    side_image_label.place(anchor=CENTER,relx=0.5, rely=0.82)

    def destroy_window():
        top.withdraw()
        root.deiconify()
    def tutorial():
        videoplayer = TkinterVideo(master=top, scaled=True)
        videoplayer.load(r"assets/video.mp4")
        videoplayer.place(anchor=CENTER,relx=0.5,rely=0.75,width=600,height=300)
        videoplayer.after(10000,videoplayer.destroy)

        videoplayer.play() # play the video
    def play():
        import game_with_keyboard
    
    watch_tut_img = Image.open('assets/button_watch-tutorial.png')
    resize_8= resize_img(watch_tut_img,200,50)
    img8 = ImageTk.PhotoImage(resize_8)
    side_image_label8 = Button(top,image=img8,command=tutorial,borderwidth=0,activebackground='#DAF7A6', bg='#DAF7A6',cursor="hand2")
    side_image_label8.image = img8
    side_image_label8.place(anchor=CENTER,relx=0.3, rely=0.3)
    
    
    start_game_img = Image.open('assets/button_start-the-game.png')
    resize_9= resize_img(start_game_img,200,50)
    img9 = ImageTk.PhotoImage(resize_9)
    side_image_label9 = Button(top,image=img9,command=play,borderwidth=0,activebackground='#DAF7A6', bg='#DAF7A6',cursor="hand2")
    side_image_label9.image = img9
    side_image_label9.place(anchor=CENTER,relx=0.7, rely=0.3)
    
    
    back_img = Image.open('assets\previous.png')
    resize_10= resize_img(back_img,50,50)
    img10 = ImageTk.PhotoImage(resize_10)
    side_image_label10 = Button(top,image=img10,command=destroy_window,borderwidth=0,activebackground='#DAF7A6', bg='#DAF7A6',cursor="hand2")
    side_image_label10.image = img10
    side_image_label10.place(anchor=CENTER,relx=0.04, rely=0.1)
    
    music_img=Image.open('assets\high_volume.png')
    resize_4=resize_img(music_img,25,25)
    img4 = ImageTk.PhotoImage(resize_4)
    m=Button(top,image=img4,command=play_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2")
    m.image=img4
    m.place(anchor=CENTER, relx=0.97,rely=0.95)

    low_music_img=Image.open('assets\low_volume.png')
    resize_5=resize_img(low_music_img,25,25)
    img5 = ImageTk.PhotoImage(resize_5)
    x=Button(top,image=img5,command=low_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2")
    x.image=img5
    x.place(anchor=CENTER, relx=0.92,rely=0.95)

    mute_music_img=Image.open('assets\mute.png')
    resize_6=resize_img(mute_music_img,25,25)
    img6 = ImageTk.PhotoImage(resize_6)
    z=Button(top,image=img6,command=stop_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2")
    z.image=img6
    z.place(anchor=CENTER, relx=0.87,rely=0.95)
    
# Add Buttons
# option_1= Button(root, text="Play with Camera", command=option1,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.5,rely=0.5)

def resize_img(img,width,height):
    resize=img.resize((width,height))
    return resize

option1_img=Image.open('assets/button_play-with-camera.png')
resize_1=resize_img(option1_img,200,50)
img = ImageTk.PhotoImage(resize_1)
Button(root,image=img,command=option1,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2").place(anchor=CENTER, relx=0.75,rely=0.4)

option2_img=Image.open('assets/button_play-with-keyboard.png')
resize_2=resize_img(option2_img,200,50)
img2 = ImageTk.PhotoImage(resize_2)
Button(root,image=img2,command=option2,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2").place(anchor=CENTER, relx=0.75,rely=0.53)

exit_img=Image.open('assets/button_exit.png')
resize_3=resize_img(exit_img,100,50)
img3 = ImageTk.PhotoImage(resize_3)
Button(root,image=img3,command=root.quit,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2").place(anchor=CENTER, relx=0.75,rely=0.66)

music_img=Image.open('assets\high_volume.png')
resize_4=resize_img(music_img,25,25)
img4 = ImageTk.PhotoImage(resize_4)
Button(root,image=img4,command=play_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2").place(anchor=CENTER, relx=0.97,rely=0.95)

low_music_img=Image.open('assets\low_volume.png')
resize_5=resize_img(low_music_img,25,25)
img5 = ImageTk.PhotoImage(resize_5)
Button(root,image=img5,command=low_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2").place(anchor=CENTER, relx=0.92,rely=0.95)

mute_music_img=Image.open('assets\mute.png')
resize_6=resize_img(mute_music_img,25,25)
img6 = ImageTk.PhotoImage(resize_6)
Button(root,image=img6,command=stop_music,borderwidth=0,bg='#DAF7A6',activebackground='#DAF7A6',cursor="hand2").place(anchor=CENTER, relx=0.87,rely=0.95)


root.mainloop()