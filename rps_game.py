from tkinter import *
import customtkinter
from PIL import Image
import random

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

width = 800
height = 600
root = customtkinter.CTk()
root.geometry(f"{width}x{height}")


def random_img():
    global img, game_start, computer_label, change, computer_choice
    if game_start:
        img = random.choice(img_list)
        computer_label.configure(image = img)
        computer_choice = img
    change = root.after(100, random_img)
    
def choice(c):
    global round, computer_score, player_score, game_start
    root.after_cancel(change)
    next_round_btn.configure(state="normal")
    
    if computer_choice == rock_img1 and c == "r":
        top_label2.configure(text=f"Round {round}: Draw")
    elif computer_choice == paper_img1 and c == "r":
        top_label2.configure(text=f"Round {round}: Lost")
        computer_score += 1
        computer_score_label.configure(text = f"Computer Score: {computer_score}")
    elif computer_choice == scissors_img1 and c == "r":
        top_label2.configure(text=f"Round {round}: Won")
        player_score +=1
        player_score_label.configure(text = f"Your Score: {player_score}")       
    elif computer_choice == rock_img1 and c == "p":
        top_label2.configure(text=f"Round {round}: Won")
        player_score +=1
        player_score_label.configure(text = f"Your Score: {player_score}")
    elif computer_choice == paper_img1 and c == "p":
        top_label2.configure(text=f"Round {round}: Draw")
    elif computer_choice == scissors_img1 and c == "p":
        top_label2.configure(text=f"Round {round}: Lost")
        computer_score += 1
        computer_score_label.configure(text = f"Computer Score: {computer_score}")
    elif computer_choice == rock_img1 and c == "s":
        top_label2.configure(text=f"Round {round}: Lost")
        computer_score += 1
        computer_score_label.configure(text = f"Computer Score: {computer_score}")
    elif computer_choice == paper_img1 and c == "s":
        top_label2.configure(text=f"Round {round}: Won")
        player_score +=1
        player_score_label.configure(text = f"Your Score: {player_score}")
    elif computer_choice == scissors_img1 and c == "s":
        top_label2.configure(text=f"Round {round}: Draw")
    
    if computer_score == 3:
        top_label2.configure(text=f"Sorry, You Lost but You Can Try Again", font = ("Helvetika", 40))
        top_label1.grid_forget()
        next_round_btn.configure(state="disabled")
        game_start = False
        
    elif player_score == 3:
        top_label2.configure(text=f"Congratulations, You Won", font = ("Helvetika", 40))
        top_label1.grid_forget()
        next_round_btn.configure(state="disabled")
        game_start = False
        
    round+=1
    rock_btn.configure(state="disabled")
    paper_btn.configure(state="disabled")
    scissors_btn.configure(state="disabled")
    restart_btn.configure(state="normal")
        
    

def start_game():
    global game_start, computer_label, round, player_score, computer_score, game_start, change
    round = 1
    player_score = 0
    computer_score = 0
    game_start = True
    
    
    if not first_start:
        change = root.after(100, random_img)
        rock_btn.configure(state="normal")
        paper_btn.configure(state="normal")
        scissors_btn.configure(state="normal")
        top_label1.grid(row = 0)
        top_label2.configure(text = f"Round {round}", font=("Helvetika", 20))
        player_score_label.configure(text = f"Your Score: {player_score}")
        computer_score_label.configure(text = f"Computer Score: {computer_score}")
  
    frame1.grid_forget()
    
    root.grid_rowconfigure(1, weight=1)
    top_frame.grid(row = 0, column=0, sticky= EW)
    
    
    root.grid_rowconfigure(1, weight=1)
    center_frame.grid(row = 1, column=0, sticky= EW)
    
    root.grid_rowconfigure(2, weight=1)
    bottom_frame.grid(row = 2, column=0, sticky= EW)
    
    
    centerleft_frame.grid(row = 0, column=0, sticky= NSEW)
    
    centerright_frame.grid(row = 0, column=1, sticky= NSEW)
    
    top_label1.grid(row=0)
    
    top_label2.grid(row=1)
    
    rock_frame.grid(row = 1, column=0)
    
    paper_frame.grid(row = 0, column=1)
    
    
    scissors_frame.grid(row = 1, column=2)
    
    rock_btn.grid(row = 0, pady =5, sticky= NSEW)
    
    
    paper_btn.grid(row = 0, pady =5, sticky= NSEW)
    
    scissors_btn.grid(row = 0, pady =5, sticky= NSEW)
    
    centerleft_label.grid(row=2, column=1)
    
    
    
    
    computer_label.grid(row = 0, pady =5, sticky= NSEW)
    
    centerright_label.grid(row=1, column=0)


def next_round():
    global change
    next_round_btn.configure(state = "disabled")
    rock_btn.configure(state="normal")
    paper_btn.configure(state="normal")
    scissors_btn.configure(state="normal")
    change = root.after(100, random_img)

def restart():
    global change, first_start
    first_start = False
    restart_btn.configure(state="disabled")
    next_round_btn.configure(state="disabled")
    start_game()
    
    
    
    
round = 1
player_score = 0
computer_score = 0
    
    
#Seting up the starting page
frame1 = customtkinter.CTkFrame(root, fg_color="red")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame1.grid(row = 0, sticky= NSEW)

game_img=Image.open("rps.png")
start_img = customtkinter.CTkImage(game_img, size= (70,70))
start_button = customtkinter.CTkButton(frame1, text="Start", font=("Helvetika", 20), image = start_img , height= 100, width=100, corner_radius = 30, command = start_game)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)
start_button.grid(row = 0, column = 0)



rock_img1 = customtkinter.CTkImage(Image.open("rock.png"), size=(120,120))
paper_img1 = customtkinter.CTkImage(Image.open("paper.png"), size=(120,120))
scissors_img1 = customtkinter.CTkImage(Image.open("scissors.png"), size=(120,120))

img_list = [rock_img1, paper_img1, scissors_img1]
game_start = False


top_frame = customtkinter.CTkFrame(root, corner_radius = 0, height = 100)

center_frame = customtkinter.CTkFrame(root, corner_radius = 0)

bottom_frame = customtkinter.CTkFrame(root, corner_radius = 0,height = 100)

centerleft_frame= customtkinter.CTkFrame(center_frame, corner_radius = 0)
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(0, weight=1)

centerright_frame= customtkinter.CTkFrame(center_frame, corner_radius = 0)
center_frame.grid_columnconfigure(1, weight=1)

top_label1 = customtkinter.CTkLabel(top_frame, text="Choose any of the three options", font=("Helvetika", 30))
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)

top_label2 = customtkinter.CTkLabel(top_frame, text=f"Round {round}", font=("Helvetika", 20))
top_frame.grid_rowconfigure(1, weight=1)

rock_frame = customtkinter.CTkFrame(centerleft_frame, corner_radius = 0)
centerleft_frame.grid_rowconfigure(1, weight=1)
centerleft_frame.grid_columnconfigure(0, weight=1)

paper_frame = customtkinter.CTkFrame(centerleft_frame, corner_radius = 0)
centerleft_frame.grid_rowconfigure(0, weight=1)
centerleft_frame.grid_columnconfigure(1, weight=1)

scissors_frame = customtkinter.CTkFrame(centerleft_frame, corner_radius = 0)
centerleft_frame.grid_columnconfigure(2, weight=1)

rock_img = customtkinter.CTkImage(Image.open("rock.png"), size=(50,50))
rock_btn = customtkinter.CTkButton(rock_frame, text="", image = rock_img , height= 50, width=50, corner_radius = 0, command = lambda: choice("r"))
rock_frame.grid_rowconfigure(0, weight=1)
rock_frame.grid_columnconfigure(0, weight=1)

paper_img = customtkinter.CTkImage(Image.open("paper.png"), size=(50,50))
paper_btn = customtkinter.CTkButton(paper_frame, text="", image = paper_img , height= 50, width=50, corner_radius = 0, command = lambda: choice("p"))
paper_frame.grid_rowconfigure(0, weight=1)
paper_frame.grid_columnconfigure(0, weight=1)

scissors_img = customtkinter.CTkImage(Image.open("scissors.png"), size=(50,50))
scissors_btn = customtkinter.CTkButton(scissors_frame, text="", image = scissors_img , height= 50, width=50, corner_radius = 0, command = lambda: choice("s"))
scissors_frame.grid_rowconfigure(0, weight=1)
scissors_frame.grid_columnconfigure(0, weight=1)

centerleft_label = customtkinter.CTkLabel(centerleft_frame, text="You", font=("Helvetika", 20))
centerleft_frame.grid_rowconfigure(2, weight = 1)

computer_label = customtkinter.CTkLabel(centerright_frame, text="")
centerright_frame.grid_rowconfigure(0, weight=1)
centerright_frame.grid_columnconfigure(0, weight=1)

centerright_label = customtkinter.CTkLabel(centerright_frame, text="Computer", font=("Helvetika", 20))
centerright_frame.grid_rowconfigure(1, weight = 1)
centerright_frame.grid_columnconfigure(0, weight = 1)

next_frame = customtkinter.CTkFrame(bottom_frame, corner_radius = 0)
bottom_frame.grid_rowconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(0, weight=1)
next_frame.grid(row = 0, column = 0)

score_frame = customtkinter.CTkFrame(bottom_frame, corner_radius = 0)
bottom_frame.grid_rowconfigure(1, weight=1)
score_frame.grid(row = 1, column = 0)


next_round_btn = customtkinter.CTkButton(next_frame, state="disabled", text="Next Round", height= 50, width=50, corner_radius = 0, command = next_round)
next_frame.grid_rowconfigure(0, weight=1)
next_frame.grid_columnconfigure(0, weight=1)
next_round_btn.grid(row= 0, column = 0, pady =5, padx = 100)

restart_btn = customtkinter.CTkButton(next_frame, state="disabled", text="Restart", height= 40, width=50, corner_radius = 0, command = restart)
next_frame.grid_columnconfigure(1, weight=1)
restart_btn.grid(row= 0, column = 1 ,pady =5, padx = 100)

player_score_label = customtkinter.CTkLabel(score_frame, text=f"Your Score: {player_score}", height= 50, width=50, corner_radius = 0)
score_frame.grid_rowconfigure(0, weight=1)
score_frame.grid_columnconfigure(0, weight=1)
player_score_label.grid(row = 0, column = 0, pady =5, padx = 130)

computer_score_label = customtkinter.CTkLabel(score_frame, text=f"Computer Score: {computer_score}", height= 50, width=50, corner_radius = 0)
score_frame.grid_columnconfigure(1, weight=1)
computer_score_label.grid(row = 0, column = 1, pady =5, padx = 130)

first_start = True



random_img()


root.mainloop()