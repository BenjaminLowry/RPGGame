from tkinter import *
from Scenes.OpeningScene import OpeningScene
import time



class Gui():

    def __init__(self, *args, **kwargs):

        self.scene = OpeningScene()
        self.textSection = None
        self.command = ""

        # Window
        self.draw_scene()


    def draw_scene(self):

        root = Tk()

        root.title("RPGGame")
        root.geometry("1100x1000")

        # frames
        invent = Frame(root)
        invent.config(bd=10, relief="groove", bg="white", height=1500, width=200)
        invent.grid(row=0, column=2, sticky="ne")

        weapon = Frame(invent)
        weapon.config(bd=3, relief="solid", bg="gray", height=200, width=170)
        weapon.grid(row=1, column=0)

        tool = Frame(invent)
        tool.config(bd=3, relief="solid", bg="gray", height=200, width=170)
        tool.grid(row=2, column=0)

        wear = Frame(invent)
        wear.config(bd=3, relief="solid", bg="gray", height=200, width=170)
        wear.grid(row=3, column=0)

        consume = Frame(invent)
        consume.config(bd=3, relief="solid", bg="gray", height=200, width=180)
        consume.grid(row=4, column=0)

        miscell = Frame(invent)
        miscell.config(bd=3, relief="solid", bg="gray", height=200, width=180)
        miscell.grid(row=5, column=0)

        #Parts of the command section
        commandGrid = Frame(root)
        commandGrid.config(bd=5, relief="sunken", bg="white", height=990, width=350)
        commandGrid.grid(row=0, column=1)

        commandHeader = Label(commandGrid, text="Command space", font=("Courier", 20, "bold", "underline"))
        commandHeader.grid(row=0, column=0)

        commandDescript = Label(commandGrid, text="Here you can type in commands to perform actions\n such as using an object on something, viewing the\n description of something etc. \n The format for commands is: \n Action: Object \n Or if you want to act on two objects, \n then it would look like this: \n Action: Object, Object ", font=("Courier", 14, "italic"))
        commandDescript.grid(row=1, column=0)

        commandEntry = Entry(commandGrid, text= "Use ___ on ___ \n (separate two objects with comma \n e.g. axe, wall)", textvariable=self.command)
        commandEntry.grid(row=2, column=0)

        commandButton = Button(commandGrid, text= "Perform action")
        commandButton.grid(row=3, column=0)

        helpButton = Button(commandGrid, text= "?", highlightcolor= "purple")
        helpButton.grid(row=4, column=0)


        # Frames for the scene description
        textSection = Frame(root)
        textSection.config(bd=3, relief="ridge", height=990, width=500)
        textSection.grid(row=0, column=0, sticky="nw")
        self.textSection = textSection

        # Parts of the inventory
        inventory = Label(invent, text="Inventory:     "
                             )
        inventory.config(font=("Courier", 20, "bold", "underline"))

        weapons = Label(weapon, text="                 Weapons:                 \n"
                                        "\n"
                                        "\n"
                                        "\n")

        miscellaneous = Label(miscell, text="      Miscellaneous objects:       \n"
                                               "\n"
                                               "\n"
                                               "\n")

        consumables = Label(consume, text="              Consumables:             \n"
                                             "\n"
                                             "\n"
                                             "\n")

        wearables = Label(wear, text="                Wearables:                \n"
                                        "\n"
                                        "\n"
                                        "\n")

        tools = Label(tool, text="                    Tools:                    \n"
                                    "\n"
                                    "\n"
                                    "\n")

        # Scene text
        sceneText = Label(textSection, text="                  ")
        sceneText.config(font=("Courier", 20, "bold", "underline"))

        # Packings
        sceneText.grid(row=0, column=0, sticky="n")
        inventory.grid(row=0, column=0)
        weapons.pack()
        miscellaneous.pack()
        consumables.pack()
        tools.pack()
        wearables.pack()


        descript = self.scene.get_opening_description()
        n = len(descript)

        text =  str("                          " + descript[0] + "                         ")  # Index 0



        self.firstSceneText = Label(self.textSection, text= text)
        self.firstSceneText.grid(row=1, column=0)

        self.firstSceneText.after(3000, lambda: self.change_text(descript, text, 1, n))


        root.mainloop()

    def change_text(self, descript, prevText, i, n):

        if i == 10:
            newText = str(descript[i].strip()) + '?\n\n' + prevText
        else:
            newText = str(descript[i].strip()) + '.\n\n' + prevText
        self.firstSceneText.config(text= newText)
        self.firstSceneText.grid(row=1, column=0)
        if i != n - 1:
            self.firstSceneText.after(3000, lambda: self.change_text(descript, newText, i + 1, n))

    def command_button_pressed(self):
        commandGiven = self.command.get()
        queryResult = self.scene.parse(commandGiven)
        self.firstSceneText.config(text=queryResult)

game = Gui()




