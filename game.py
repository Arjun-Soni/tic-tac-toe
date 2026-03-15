import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe")
player = "X"
root.config(bg="#dddddd")
title_label = tk.Label(
    root,
    text="Tic Tac Toe",
    font=("Arial", 23, "bold"),
    bg="#dddddd"
    )
title_label.grid(row=0, column=0, columnspan=3, pady=10)
def touch(btn):
    global player
    if btn["text"] != "":
        return
    if player == "X":
        btn.config(text="X")
        player = "O"
    else:
        btn.config(text="O")
        player = "X"
    check_winner()
    check_draw()

def check_winner():
    for ro in range(3):
        if buttons[ro][0]["text"] == buttons[ro][1]["text"] == buttons[ro][2]["text"] !="":
            winner = buttons[ro][0]["text"]
            messagebox.showinfo("Game Over", f"{winner} wins!")
            disable_board()
            return
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] !="":
            winner = buttons[0][col]["text"]
            messagebox.showinfo("Game Over", f"{winner} wins!")
            disable_board()
            return
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] !="":
            winner = buttons[0][0]["text"]
            messagebox.showinfo("Game Over", f"{winner} wins!")
            disable_board()
            return
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] !="":
        winner = buttons[0][2]["text"]
        messagebox.showinfo("Game Over", f"{winner} wins!")
        disable_board()
        return

def disable_board():
    for ro in buttons:
        for button in ro:
            button.config(state="disabled")

def check_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return
    messagebox.showinfo("Game Over", "It's a Draw!")
    disable_board()            

def restart_game():
    global player
    player = "X"
    for ro in buttons:
        for button in ro:
            button.config(state="normal", text="")

buttons = []
for ro in range(3):
    row_button = []
    for col in range(3):
        button = tk.Button(
            root,
            text="",
            width=10,
            height=5,
            font=("Arial",22,"bold"),
            bg="white",
            activebackground="#d6eaff"
            )
        row_button.append(button)
        button.config(command=lambda b=button : touch(b))
        button.grid(row=ro, column=col)
    buttons.append(row_button)
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial",14,"bold"),
    bg="#4CAF50",
    fg="white",
    command=restart_game
)
restart_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
root.mainloop()