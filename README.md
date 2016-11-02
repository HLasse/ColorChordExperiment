# ColorChordExperiment

#### Hypothesis: Seeing a highly saturated color will bias you to rate a chord as more positive than seeing a low saturated color.

Output of experiment:
[id, age, gender, musician, color, rating, condition, 


#load libraries

from psychopy import visual, gui, core, event, data
import cv2, sys, winsound
from random import sample

#Make popup 
#   Gender
#   Age
#   So on

popup = gui.Dlg(title = "Sound Experiment")
popup.addField("ID: "
popup.addField("Gender:", choices = ["Male","Female"])
popup.addField("Age: ")
popup.addField("Musical Experience:", choices = ["Yes","No"])

popup.show()

if popup.OK:
    ID = popup.data[0]
    Gender = popup.data[1]
    Age = popup.data[2]
    Musical_Exp = popup.data[3]
else:
    core.quit()



#Instructions


#Start Loop
#   play sound
#   get response




















