import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.iconbitmap("logo.ico") 
app.title("The Roshambo Game")
app.geometry("500x550")

# Scores
p_score = 0
c_score = 0 

def update_score(winner):
    global p_score, c_score
    if winner == "player": p_score += 1
    if winner == "computer": c_score += 1
    score_label.configure(text=f"Player: {p_score}  |  CPU: {c_score}")

def play(player_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
    
    if player_choice == computer_choice:
        res = "IT'S A TIE!"
        color = "#aaaaaa"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        res = "YOU WIN! ✨"
        color = "#2ecc71"
        update_score("player")
    else:
        res = "YOU LOSE! 🤖"
        color = "#e74c3c"
        update_score("computer")

    comp_label.configure(text=f"CPU Choice: {computer_choice}")
    result_display.configure(text=res, text_color=color)

# --- UI --=
title = ctk.CTkLabel(app, text="Roshambo Arcade", font=("Impact", 35))
title.pack(pady=20)

score_label = ctk.CTkLabel(app, text="Player: 0  |  CPU: 0", font=("Arial", 18, "bold"))
score_label.pack(pady=10)

# Display
display_frame = ctk.CTkFrame(app, width=400, height=150, corner_radius=15)
display_frame.pack(pady=20)

comp_label = ctk.CTkLabel(display_frame, text="Waiting for move...", font=("Arial", 20))
comp_label.place(relx=0.5, rely=0.3, anchor="center")

result_display = ctk.CTkLabel(display_frame, text="Choose Rock, Paper, or Scissors", font=("Arial", 22, "bold"))
result_display.place(relx=0.5, rely=0.7, anchor="center")

# Buttons 
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=20)

ctk.CTkButton(btn_frame, text="🪨 Rock", width=120, height=50, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
ctk.CTkButton(btn_frame, text="📄 Paper", width=120, height=50, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
ctk.CTkButton(btn_frame, text="✂️ Scissors", width=120, height=50, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

app.mainloop()