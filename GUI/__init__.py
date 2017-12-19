import tkinter as tk

class gui():
    root = tk.Tk()
    def __init__(self, *args, **kwargs):
        # Window
        self.root.title("RPG Game")
        self.root.geometry("1000x1000")

    invent = tk.Frame(root)
    invent.config(bd=10, relief="groove", bg="white", height=990, width=200)
    invent.grid(row=0, column=2, sticky="ne")

    weapon = tk.Frame(invent)
    weapon.config(bd=3, relief="solid", bg="gray", height=200, width=170)
    weapon.grid(row=1, column=0)

    tool = tk.Frame(invent)
    tool.config(bd=3, relief="solid", bg="gray", height=200, width=170)
    tool.grid(row=2, column=0)

    wear = tk.Frame(invent)
    wear.config(bd=3, relief="solid", bg="gray", height=200, width=170)
    wear.grid(row=3, column=0)

    consume = tk.Frame(invent)
    consume.config(bd=3, relief="solid", bg="gray", height=200, width=180)
    consume.grid(row=4, column=0)

    miscell = tk.Frame(invent)
    miscell.config(bd=3, relief="solid", bg="gray", height=200, width=180)
    miscell.grid(row=5, column=0)

    # Parts of the inventory
    inventory = tk.Label(invent, text="Inventory:     "
                         )
    inventory.config(font=("Courier", 20, "bold", "underline"))

    weapons = tk.Label(weapon, text="                 Weapons:                 \n"
                                    "\n"
                                    "\n"
                                    "\n")

    miscellaneous = tk.Label(miscell, text="      Miscellaneous objects:       \n"
                                           "\n"
                                           "\n"
                                           "\n")

    consumables = tk.Label(consume, text="              Consumables:             \n"
                                           "\n"
                                           "\n"
                                           "\n")

    wearables = tk.Label(wear, text="                Wearables:                \n"
                                         "\n"
                                         "\n"
                                         "\n")

    tools = tk.Label(tool, text="                    Tools:                    \n"
                                         "\n"
                                         "\n"
                                         "\n")
    space1 = tk.Label(root,
                      text="                                                                                        ")

    # Scene text
    sceneText = tk.Label(root, text="This is what happens in the scene.")
    sceneText.config(font=("Courier", 20, "bold", "underline"))

    # Packings
    sceneText.grid(row=0, column=0, sticky="nw")
    space1.grid(row=0, column=1)
    inventory.grid(row=0, column=0)
    weapons.pack()
    miscellaneous.pack()
    consumables.pack()
    tools.pack()
    wearables.pack()

    # Frames
    root.mainloop()


