import tkinter as tk
root = tk.Tk()
root.title("Tic Tac Toe")
player = "X"
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
for ro in range(3):
    for col in range(3):
        button = tk.Button(root, text="", width=10, height=5)
        button.config(command=lambda b=button : touch(b))
        button.grid(row=ro, column=col)
root.mainloop()