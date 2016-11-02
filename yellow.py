#load libraries

from psychopy import visual, core, event, gui
import random
import pandas as pd

#creating pop up to get participant data
popup = gui.Dlg(title = 'Chord Experiment')
popup.addField("ID: ")
popup.addField("Age: ")
popup.addField("Gender: ", choices = ["Male", "Female"])
popup.addField("Do you play music?" , choices = ["Yes", "No"])
popup.show()
#save participant data to variables if ok is clicked, else quit
if popup.OK:
    id = popup.data[0]
    age = popup.data[1]
    gender = popup.data[2]
    musician = popup.data[3]
else:
    core.quit()

win = visual.Window(fullscr=True, rgb=(255,255,0))
msg = visual.TextStim(win, text = """In this experiment you will be presented with a word in the middle of the screen.\n
Your task is to press the 'space' button on the keyboard when you have read the word.\n
That's it! Press any key to begin the experiment!""")
msg.draw()
win.flip()
next = event.waitKeys()
#
#def show_info(txt):
#    txtstm = visual.TextStim(win, text=txt) 
#    txtstm.draw()
#    win.flip()
#    event.waitKeys()
#    if key[0] in ['escape']: core.quit()
