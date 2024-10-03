import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.wins = {"X": 0, "O": 0}
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                               command=lambda r=r, c=c: self.on_click(r, c))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

        tk.Button(self.root, text="Restart", command=self.restart_game).grid(row=3, column=0, columnspan=2, sticky="ew")
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=3, column=2, sticky="ew")

        self.x_win_label = tk.Label(self.root, text="X Wins: 0")
        self.x_win_label.grid(row=4, column=0, columnspan=3)
        self.o_win_label = tk.Label(self.root, text="O Wins: 0")
        self.o_win_label.grid(row=5, column=0, columnspan=3)

    def on_click(self, r, c):
        btn = self.buttons[r][c]
        if btn['text'] == "" and not self.check_winner():
            btn['text'] = self.current_player
            if self.check_winner():
                self.wins[self.current_player] += 1
                self.update_win_labels()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = [self.buttons[i] for i in range(3)] + \
                [[self.buttons[r][i] for r in range(3)] for i in range(3)] + \
                [[self.buttons[i][i] for i in range(3)]] + \
                [[self.buttons[i][2-i] for i in range(3)]]
        return any(line[0]['text'] == line[1]['text'] == line[2]['text'] != "" for line in lines)

    def check_draw(self):
        return all(btn['text'] != "" for row in self.buttons for btn in row)

    def restart_game(self):
        for row in self.buttons:
            for btn in row:
                btn['text'] = ""
        self.current_player = "X"

    def update_win_labels(self):
        self.x_win_label.config(text=f"X Wins: {self.wins['X']}")
        self.o_win_label.config(text=f"O Wins: {self.wins['O']}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


