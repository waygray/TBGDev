


def get_player_name():
    user_input = input("    Enter player name: ")
    print("    Hello, " + user_input + ", Welcome to game!")

def start_game():
    print(
        """
    Something is going to go here, I dont know what I want to make this game about
    yet, this is mainly something so I have something fun to code, but to help myself learn, 
    python on a deeper level. Thanks for Reading!(If you see this before I change this, Why are you here?)
        """
    )
    print("    If you want to quit the game at any point, simply type 'quit'.\n")

def show_help():
    print("""
        ⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧
        Help / ? - Lists all commands
        Quit      - Quits the game
        ⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩
        """)

def quit_game():
    print("Thank you for playing, come back again sometime soon!")
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀""")
    raise SystemExit

def unknown_cmd(cmd):
    print(f"Unknown Command: {cmd}")
    
def game_loop():
    commands = {
        "help": show_help,
        "?": show_help,
        "quit": quit_game
    }
    while True:
        user_input = input("""
    □□□□□□□□□□□□□□□□□□□□□□□□□□□□
    What would you like to do?
    □□□□□□□□□□□□□□□□□□□□□□□□□□□□
    """).strip().lower()

        if user_input == "":
            print("""
    *****************************************************
    *   \033[1;3mPlease type something so we can move forward!\033[0m   *
    *****************************************************
    """)
            continue

        action = commands.get(user_input, None)
        if action:
            action()
        else:
            unknown_cmd(user_input)



import tkinter as tk

class SimpleGameUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Adventure Game")
        self.root.geometry("800x500")

        self.out = tk.Text(root, wrap="word", state="disabled")
        self.out.pack(fill="both", expand=True, padx=10, pady=(10, 6))

        self.entry = tk.Entry(root)
        self.entry.pack(fill="x", padx=10, pady=(0, 10))
        self.entry.bind("<Return>", self.on_enter)

        self.have_name = False
        self.player_name = ""
        self.write("Enter player name:")

    def write(self, text: str):
        self.out.configure(state="normal")
        self.out.insert("end", text.rstrip() + "\n")
        self.out.see("end")
        self.out.configure(state="disabled")

    def on_enter(self, event=None):
        text = self.entry.get().strip()
        self.entry.delete(0, "end")

        if not self.have_name:
            if text == "":
                self.write("Please enter a name.")
                return
            self.player_name = text
            self.have_name = True
            self.write(f"Hello, {self.player_name}, Welcome to game!\n")
            # Show your intro text in the window
            self.write(
                "Something is going to go here, I dont know what I want to make this game about\n"
                "yet, this is mainly something so I have something fun to code, but to help myself learn,\n"
                "python on a deeper level. Thanks for Reading!(If you see this before I change this, Why are you here?)\n"
            )
            self.write("If you want to quit the game at any point, simply type 'quit'.")
            self.write("Type 'help' or '?' for commands.")
            return

        cmd = text.lower()
        if cmd == "":
            self.write("Please type something so we can move forward!")
            return

        if cmd in ("help", "?"):
            self.write(
                "\n"
                "⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧⤧\n"
                "Help / ? - Lists all commands\n"
                "Quit      - Quits the game\n"
                "⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩⤩\n"
            )
        elif cmd == "quit":
            self.write("Thank you for playing, come back again sometime soon!")
            self.root.after(400, self.root.destroy)
        else:
            self.write(f"Unknown Command: {cmd}")

def run_gui():
    root = tk.Tk()
    SimpleGameUI(root)
    root.mainloop()


















def main():
    run_gui()
    get_player_name()
    start_game()


if __name__ == '__main__':
    main()

