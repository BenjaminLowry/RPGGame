import tkinter as tk

root = tk.Tk()

#Window
root.title("RPG Game")
root.geometry("1000x1000")

#Frames
invent = tk.Frame(root)
invent.config(bd=10, relief="groove", bg="red", height=990, width=200)
invent.grid(row=0, column=2, sticky="ne")

weapon = tk.Frame(invent)
weapon.config(bd=3, relief="solid", bg="black", height=150, width=180)
weapon.grid(row=1, column=0)

#Parts of the inventory
inventory = tk.Label(invent, text= "Inventory:     "
                                   " \n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n")
inventory.config(font = ("Courier", 20, "bold", "underline"))


weapons = tk.Label(weapon, text="Weapons: \n"
                                "\n"
                                "\n"
                                "\n")

space1 = tk.Label(root, text= "                                                                                        ")


#Scene text
sceneText = tk.Label(root, text="This is what happens in the scene.")
sceneText.config(font = ("Courier", 20, "bold", "underline"))

#Packings
sceneText.grid(row=0, column=0, sticky="nw")
space1.grid(row=0, column=1)
inventory.pack()
weapons.pack()



root.mainloop()