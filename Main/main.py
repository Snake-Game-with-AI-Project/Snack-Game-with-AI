from tkinter import *
from PIL import ImageTk,Image # pip install pillow
from tkVideoPlayer import TkinterVideo
import pygame


root= Tk() #create a window

root.title("Snake Game") # Add title

# Add icon
root.iconbitmap("assets/snake.ico")

root.geometry("600x400") # Window geometry
root.configure(bg='#C3F8FF')

# Add music
pygame.mixer.init()

# Add Text
my_label1= Label(root,text="Welcome to snake game",font=('Arial',20),bg='#C3F8FF')
my_label1.place(anchor=CENTER, relx=0.5,rely=0.1)


# Add Image
img= PhotoImage(file="assets\snake_img.png")
# my_img= ImageTk.PhotoImage(Image.open("assets/snake_bkg.png"))
w=Label(image=img,bg='#C3F8FF')
w.place(anchor=CENTER, relx=0.5,rely=0.3)

# Add music
def play_music():
    pygame.mixer.music.load("assets/music.mp3")
    pygame.mixer.music.play(-1)
def stop_music():
    pygame.mixer.music.stop()

def option1():
    root.withdraw() # Destroy root window
    top= Toplevel() # New Window
    top.title('Snake Game with Camera')
    root.iconbitmap("assets/snake.ico")
    top.geometry("600x400") # Window geometry
    
    top.configure(bg='#C3F8FF')
    # Add Text
    my_label1= Label(top,text="How to play Snake Game by using AI",font=('Arial',20),bg='#C3F8FF')
    my_label1.place(anchor=CENTER, relx=0.5,rely=0.1)
    
    def destroy_window():
        top.withdraw()
        root.deiconify()
    def tutorial():
        videoplayer = TkinterVideo(master=top, scaled=True)
        videoplayer.load(r"assets/video.mp4")
        videoplayer.place(anchor=CENTER,relx=0.5,rely=0.7,width=400,height=200)

        videoplayer.play() # play the video
    def play():
        import game_with_camera
    
    tutorial_btn= Button(top,text="Watch Tutorial", command=tutorial,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.2,rely=0.3)
    play_btn= Button(top,text="Start the Game", command=play,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.5,rely=0.3)
    back_btn= Button(top,text="Back to Main Menu", command=destroy_window,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.8,rely=0.3)
    mute_btn= Button(top,text="Stop song", command=stop_music,bg='#FFEBAD',activebackground='#FFF6BF',font=('romanandnews',10),cursor="hand2").place(anchor=CENTER, relx=0.9,rely=0.9)
    
    
def option2():
    root.withdraw() # Destroy root window
    top= Toplevel() # New Window
    top.title('Snake Game with Keyboard')
    top.iconbitmap("assets/snake.ico")
    top.geometry("600x400") # Window geometry
    
    top.configure(bg='#C3F8FF')
    # Add Text
    my_label1= Label(top,text="How to play Snake Game by using Keyboard",font=('Arial',20),bg='#C3F8FF')
    my_label1.place(anchor=CENTER, relx=0.5,rely=0.1)
    
    def destroy_window():
        top.withdraw()
        root.deiconify()
    def tutorial():
        videoplayer = TkinterVideo(master=top, scaled=True)
        videoplayer.load(r"assets/video.mp4")
        videoplayer.place(anchor=CENTER,relx=0.5,rely=0.7,width=400,height=200)

        videoplayer.play() # play the video
    def play():
        import game_with_keyboard
    
    tutorial_btn= Button(top,text="Watch Tutorial", command=tutorial,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.2,rely=0.3)
    play_btn= Button(top,text="Start the Game", command=play,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.5,rely=0.3)
    back_btn= Button(top,text="Back to Main Menu", command=destroy_window,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.8,rely=0.3)
    mute_btn= Button(top,text="Stop song", command=stop_music,bg='#FFEBAD',activebackground='#FFF6BF',font=('romanandnews',10),cursor="hand2").place(anchor=CENTER, relx=0.9,rely=0.9)
    
# Add Buttons
option_1= Button(root, text="Play with Camera", command=option1,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.5,rely=0.5)
option_2= Button(root, text="Play with Keyboard", command=option2,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.5,rely=0.65)
quit= Button(root, text="Exit Game", command=root.quit,bg='#FFEBAD',bd=3,padx=10,pady=5,activebackground='#FFF6BF',font=('romanandnews',12),cursor="hand2").place(anchor=CENTER, relx=0.5,rely=0.8)
music_btn= Button(root,text="Play song",command=play_music,bg='#FFEBAD',activebackground='#FFF6BF',font=('romanandnews',10),cursor="hand2").place(anchor=CENTER, relx=0.9,rely=0.9)
mute_btn= Button(root,text="Stop song", command=stop_music,bg='#FFEBAD',activebackground='#FFF6BF',font=('romanandnews',10),cursor="hand2").place(anchor=CENTER, relx=0.75,rely=0.9)



root.mainloop()