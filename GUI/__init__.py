import tkinter as tk
from Scenes.OpeningScene import OpeningScene
import time



class Gui():

    def __init__(self, *args, **kwargs):

        self.scene = OpeningScene()
        self.textSection = None

        # Window
        self.draw_scene()


    def draw_scene(self):

        root = tk.Tk()

        root.title("RPGGame")
        root.geometry("1000x1000")

        # frames
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

        # Frames for the scene description
        textSection = tk.Frame(root)
        textSection.config(bd=3, relief="ridge", height=200, width=350)
        textSection.grid(row=0, column=0, sticky="nw")
        self.textSection = textSection

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
        sceneText = tk.Label(textSection, text="                  ")
        sceneText.config(font=("Courier", 20, "bold", "underline"))

        # Packings
        sceneText.grid(row=0, column=0, sticky="n")
        space1.grid(row=0, column=1)
        inventory.grid(row=0, column=0)
        weapons.pack()
        miscellaneous.pack()
        consumables.pack()
        tools.pack()
        wearables.pack()


        descript = self.scene.get_opening_description()
        n = len(descript)

        text = str(descript[0]) + "."  # Index 0

        self.firstSceneText = tk.Label(self.textSection, text= text)
        self.firstSceneText.grid(row=1, column=0)

        self.firstSceneText.after(2000, lambda: self.change_text(descript, text, 1, n))

        root.mainloop()

    def change_text(self, descript, prevText, i, n):

        newText = str(descript[i].strip()) + '.\n\n' + prevText
        self.firstSceneText.config(text= newText)
        self.firstSceneText.grid(row=1, column=0)
        if i != n - 1:
            self.firstSceneText.after(2000, lambda: self.change_text(descript, newText, i + 1, n))




game = Gui()




