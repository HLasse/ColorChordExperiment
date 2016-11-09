#load libraries

from psychopy import visual, core, event, gui, sound
from random import sample
import ppc
import glob

#creating pop up to get participant data
popup = gui.Dlg(title = 'Chord Experiment')
popup.addField("ID: ")
popup.addField("Age: ")
popup.addField("Which day of the month were you born?: ")
popup.addField("Gender: ", choices = ["Male", "Female"])
popup.addField("Do you play music?" , choices = ["No", "Yes"])
popup.show()
#save participant data to variables if ok is clicked, else quit
if popup.OK:
    ID = popup.data[0]
    age = popup.data[1]
    day = int(popup.data[2])
    gender = popup.data[3]
    musician = popup.data[4]
else:
    core.quit()

# defining variables
trial_list = []
audio_stim = glob.glob('ExperimentStims\*.wav')
condition = []

# setting conditions and defining windows
if day < 15:
    condition = 'happy'
    win = visual.Window(fullscr = True, color = 'Yellow')
else:
    condition = 'sad'
    win = visual.Window(fullscr = True, color = 'MidnightBlue')


# preparing list of trials
for stim in audio_stim:
    trial_list += [{
    'ID' : ID,
    'Age' : age,
    'Gender' : gender,
    'day born' : day,
    'musician' : musician,
    'condition' : condition,
    'stim': stim,
    'rating' : '',
    'happycolor' : '',
    'sadcolor' : ''
    }]

# randomizing order
trial_list = sample(trial_list, len(trial_list))

# adding trial numbers
for i, trial in enumerate(trial_list):
    trial['no'] = i + 1


# intro screen
msg = visual.TextStim(win, text = """Thank you for participating in our experiment.\n 
Throughout the experiment you will be presented with a number of sounds, which we would like you to rate on a scale from 1 to 10, 1 being very sad and 10 being very happy.\nFeel free to ask the experimenter any questions you might have.\n 
To choose a rating, click the scale then press 'enter'.\nPress 'enter' to begin!""", color = "Grey")
msg.draw()
win.flip()
key = event.waitKeys()
if key[0] in ['escape']:core.quit()


# creating rating scale
rating_scale = visual.RatingScale(win, markerColor = "Grey", singleClick = True,
scale = "Very Sad         ...         Very Happy", low =  1, high = 10,
textColor = "Grey", lineColor = "Grey")

# creating writer
writer = ppc.csvWriter(ID, saveFolder='data', headerTrial=trial_list[0])

# loop through trials
for trial in trial_list:
    stim = sound.Sound(trial['stim'])
    stim.play()
    while rating_scale.noResponse:
        rating_scale.draw()
        win.flip()
    answer = rating_scale.getRating()
    trial['rating'] = answer
    rating_scale.reset()
    key = event.waitKeys()
    if key[0] in ['escape']: 
        core.quit()


win2 = visual.Window(fullscr = True, color =  'MidnightBlue')
msg2 = visual.TextStim(win2, text = """Please rate the background color""", color = "Grey")
msg2.draw()
win2.flip()
next = event.waitKeys()
#
# creating rating scale
rating_scale = visual.RatingScale(win2, markerColor = "Grey", singleClick = True, 
scale = "Very Sad         ...         Very Happy", low =  1, high = 10, # creating a scale from 1 - 10. 
textColor = "Grey", lineColor = "Grey")



while rating_scale.noResponse:
    rating_scale.draw()
    win2.flip()
sadrating = rating_scale.getRating()
rating_scale.reset()
key = event.waitKeys()
if key[0] in ['escape']: 
    core.quit()




win3 = visual.Window(fullscr = True, color =  'Yellow')
msg3 = visual.TextStim(win3, text = """Please rate the background color""", color = "Grey")
msg3.draw()
win3.flip()
next = event.waitKeys()

rating_scale2 = visual.RatingScale(win3, markerColor = "Grey", singleClick = True,
scale = "Very Sad         ...         Very Happy", low =  1, high = 10, # creating a scale from 1 - 10. 
textColor = "Grey", lineColor = "Grey")

while rating_scale2.noResponse:
    rating_scale2.draw()
    win3.flip()
happyrating = rating_scale2.getRating()
rating_scale2.reset()
key = event.waitKeys()
if key[0] in ['escape']: 
    core.quit()


for trial in trial_list:
    trial['happycolor'] = happyrating
    trial['sadcolor'] = sadrating
    writer.write(trial)
    
msg4 = visual.TextStim(win3, text = """That's it! Thanks for participating! Press 'escape' to exit""", color = 'Grey')
msg4.draw()
win3.flip()
next = event.waitKeys(keyList=['escape'])
win3.close()
core.quit()
