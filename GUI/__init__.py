import tkinter as tk
from Scenes.OpeningScene import OpeningScene
import time



class Gui:

    root = tk.Tk()
    def __init__(self, *args, **kwargs):
        # Window
        self.root.title("RPG Game")
        self.root.geometry("1000x1000")
        self.openingDescription = OpeningScene


    #frames
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

    #Frames for the scene description
    firstSection = tk.Frame(root)
    firstSection.config(bd=3, relief="ridge", height=200, width=350)
    firstSection.grid(row=1, column=0)

    secSection = tk.Frame(root)
    secSection.config(bd=3, relief="ridge", height=200, width=350)
    secSection.grid(row=2, column=0)

    triSection = tk.Frame(root)
    triSection.config(bd=3, relief="ridge", height=200, width=350)
    triSection.grid(row=3, column=0)

    fourSection = tk.Frame(root)
    fourSection.config(bd=3, relief="ridge", height=200, width=350)
    fourSection.grid(row=4, column=0)

    fivSection = tk.Frame(root)
    fivSection.config(bd=3, relief="ridge", height=200, width=350)
    fivSection.grid(row=5, column=0)

    sexSection = tk.Frame(root)
    sexSection.config(bd=3, relief="ridge", height=200, width=350)
    sexSection.grid(row=6, column=0)

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
    sceneText = tk.Label(root, text="                  ")
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


    t=5

    firstText = tk.Label(text=descript[0])
    secText = tk.Label(text=descript[1])
    triText = tk.Label(text=descript[2])
    fourText = tk.Label(text=descript[3])
    fivText = tk.Label(text=descript[4])
    sexText = tk.Label(text=descript[5])

    while t >= 0:
        time.sleep(1)
        t -= 1
    firstText.config(firstSection)
    firstText.pack()

    t = 5
    while t >= 0:
        time.sleep(1)
        t -= 1
    firstText.config(secSection)
    firstText.pack()

    secText.config(firstSection)
    secText.pack()

    while t >= 0:
        time.sleep(1)
        t -= 1
    firstText.config(triSection)
    firstText.pack()

    secText.config(secSection)
    secText.pack()

    triText.config(firstSection)
    triText.pack()

    while t >= 0:
        time.sleep(1)
        t -= 1
    firstText.config(fourSection)
    firstText.pack()

    secText.config(triSection)
    secText.pack()

    triText.config(secSection)
    triText.pack()

    fourText.config(firstSection)
    fourText.pack()

    while t >= 0:
        time.sleep(1)
        t -= 1
    firstText.config(fivSection)
    firstText.pack()

    secText.config(fourSection)
    secText.pack()

    triText.config(triSection)
    triText.pack()

    fourText.config(secSection)
    fourText.pack()

    # Frames
    root.mainloop()







