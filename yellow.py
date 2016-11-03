#load libraries

from psychopy import visual, core, event, gui, sound
from random import sample
import ppc


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
    id = popup.data[0]
    age = popup.data[1]
    day = int(popup.data[2])
    gender = popup.data[3]
    musician = popup.data[4]
else:
    core.quit()

# defining variables
trial_list = []
audio_stim = ("cat_meow_x.waw")
condition = []

# setting conditions
if day < 10:
    condition = 'happy'
elif day < 20:
    condition = 'sad'
else:
    condition = 'neutral'
    
# preparing list of trials
for stim in audio_stim:
    trial_list += [{
    'ID' : id,
    'Age' : age,
    'Gender' : gender,
    'day born' : day,
    'musician' : musician,
    'condition' : condition,
    'rating' : ''
    }]

# randomizing order
trial_list = sample(trial_list, len(trial_list))

# adding trial numbers
for i, trial in enumerate(trial_list):
    trial['no'] = i + 1

# creating window

if condition == 'happy':
    win = visual.Window(fullscr = True, rgb=(255,255,0))
elif condition == 'sad':
    win = visual.Window(fullscr = True, rgb=(0, 255, 255))
else:
    win = visual.Window(fullscr = True)


# intro screen
msg = visual.TextStim(win, text = """Test text!""", color = "Black")
msg.draw()
win.flip()
next = event.waitKeys()


# creating rating scale
rating_scale = visual.RatingScale(win, markerColor = "White", 
scale = "Very Sad         ...         Very Happy", low =  1, high = 10,
labels = ['1','5','10'],
textColor = "Black", lineColor = "Black")

# creating writer


# loop through trials
for trial in trial_list:
    if trial['condition'] == 'happy':
        while rating_scale.noResponse:
            stim = sound.Sound(audio_stim)
            stim.play() 
            rating_scale.draw()
            win.flip()
    elif trial['condition'] == 'sad':
        while rating_scale.noResponse:
            rating_scale.draw()
            win.flip()
    else:
        while rating_scale.noResponse:
            rating_scale.draw()
            win.flip()
