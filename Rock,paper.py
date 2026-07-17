import tkinter as tk #Tkinter is to create the an GUI 
import random#This module allows the computer to choose random choice

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="You: " + user_choice)
    computer_label.config(text="Computer: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = " You Win!"
    else:
        result = " Computer Wins!"

    result_label.config(text=result)

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x400")
root.configure(bg="#dff6ff")

title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="#dff6ff",
    fg="blue"
)
title.pack(pady=20)

user_label = tk.Label(root, text="You:", font=("Arial", 14), bg="#dff6ff")
user_label.pack()

computer_label = tk.Label(root, text="Computer:", font=("Arial", 14), bg="#dff6ff")
computer_label.pack()

result_label = tk.Label(
    root,
    text="Choose an option",
    font=("Arial", 16, "bold"),
    bg="#dff6ff",
    fg="red"
)
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#dff6ff")
button_frame.pack()

rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    font=("Arial", 12),
    width=10,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 12),
    width=10,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    font=("Arial", 12),
    width=10,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()
