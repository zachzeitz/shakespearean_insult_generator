from tkinter import *
from tkinter import ttk
import pyttsx3
import random
from lists import *

def shakespeare_insult():
    engine = pyttsx3.init('espeak')   
    coin = random.randint(1, 2)
    
    if coin ==1:
        ins=str("You " + random.choice(s_verb)+" "+ random.choice(s_adjective)+" " + random.choice(s_noun) + "!")
        engine.say(ins)
    elif coin == 2:
        ins=str("You " + random.choice(s_adverb)+" "+ random.choice(s_verb)+" " + random.choice(s_noun) + "!")
        engine.say(ins)
    #print(ins)
    engine.runAndWait()

root= Tk()
root.title("Insult Generator")
root.geometry("330x330")

gen_ins_button= Button(root, text="Shakesperean Insult", command=shakespeare_insult)
gen_ins_button.grid(row=0, column=0, padx=10, pady=10,sticky=N, ipadx=70)

root.mainloop()