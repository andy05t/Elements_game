from tkinter import *
import random
import tkinter.messagebox 
import json
import sys

elements = dict()
with open("Python/periodic_table.json") as f:
    df = json.load(f)['elements']
for d in df:
    elements[d["number"]] = d['symbol']

#elements = {1:'H',2: "He",3: "Li", 4: "Be",5: "B",6: "C",7: "N",8: "O",9: "F",10: "Ne",
#11: "Na",12: "Mg",13: "Al",14: "Si",15: "P",16: "S",17: "Cl",18: "Ar",19: "K",20: "Ca"}
counter = 0
el = random.randint(1,20)


root = Tk()

textv = StringVar()
textv.set("The atomic number is: " + str(el))

def quit_popup():
    q = tkinter.messagebox.askquestion("Quitting...", "Are you sure you want to quit?")
    if q == "yes":
        root.destroy()

def check():
    global counter, el
    #print(elements[el],user_input) 
    if elements[el] == user_input.get():
        tkinter.messagebox.showinfo("Congratulations!", "Well done! Please proceed to the next question")
        el = random.randint(1,20)
        textv.set("The atomic number is: " + str(el))
        counter = 0
    else:
        tkinter.messagebox.showinfo("Answer", "Incorrect")
        counter += 1
        for key,value in elements.items():
            #print(user_input.get(),value)
            if user_input.get() == value:
                if key > el:
                    tkinter.messagebox.showinfo("Hint!", "Hint: The actual element is to the left!")
                elif key < el:
                    tkinter.messagebox.showinfo("Hint!", "Hint: The actual element is to the right")
                break   
        if user_input.get() not in elements.values():
            tkinter.messagebox.showinfo("Error", "Error: There is no such element! Try again!") 
                
        if counter == 5:
            tkinter.messagebox.showinfo("Game over", "Game over: try again later")
            root.destroy()

def solution():
    tkinter.messagebox.showinfo("Answer", "Disappointing... the correct answer is: {}".format(elements[el]))

a_Label = Label(root, textvariable = textv)  
answ_label = Label(root, text = "Answer:")
user_input = Entry(root)

submit = Button(root, text = "Submit", bg = "green", command = check)
get_answ = Button(root, text = "Get answer", bg = "yellow", command = solution)
quitting = Button(root, text = "Quit", bg = "red", command = quit_popup)


a_Label.pack()
answ_label.pack()
user_input.pack()
submit.pack()
get_answ.pack()
quitting.pack()

root.mainloop()