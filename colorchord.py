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
if day < 10:
    condition = 'happy'
    win = visual.Window(fullscr = True, color = 'Yellow')
elif day < 20:
    condition = 'sad'
    win = visual.Window(fullscr = True, color = 'MightnightBlue')
else:
    condition = 'neutral'
    win = visual.Window(fullscr = True, color = 'White')
    
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
    'sadcolor' : '',
    'neutralcolor' : ''
    }]

# randomizing order
trial_list = sample(trial_list, len(trial_list))

# adding trial numbers
for i, trial in enumerate(trial_list):
    trial['no'] = i + 1


# intro screen
msg = visual.TextStim(win, text = """Test text!""", color = "Black")
msg.draw()
win.flip()
key = event.waitKeys()
if key[0] in ['escape']:core.quit()


# creating rating scale
rating_scale = visual.RatingScale(win, markerColor = "White", 
scale = "Very Sad         ...         Very Happy", low =  1, high = 10,
labels = ['1','5','10'],
textColor = "Black", lineColor = "Black")

# creating writer
writer = ppc.csvWriter(ID, saveFolder='data', headerTrial=trial_list[0])

print trial_list

# loop through trials
for trial in trial_list:
    if trial['condition'] == 'happy':
        stim = sound.Sound(trial['stim'])
        stim.play()
        while rating_scale.noResponse:
            rating_scale.draw()
            win.flip()
        answer = rating_scale.getRating()
        trial['rating'] = answer
        rating_scale.reset()
    elif trial['condition'] == 'sad':
        stim = sound.Sound(trial['stim'])
        stim.play()
        while rating_scale.noResponse:
            rating_scale.draw()
            win.flip()
        answer = rating_scale.getRating()
        trial['rating'] = answer
        rating_scale.reset()
    else:
        stim = sound.Sound(trial['stim'])
        stim.play()
        while rating_scale.noResponse:
            rating_scale.draw()
            win.flip()
        answer = rating_scale.getRating()
        trial['rating'] = answer
        rating_scale.reset()
    writer.write(trial)

win.close()
core.quit()
#
#win2 = visual.Window(fullscr = True, rgb =(255,255,0))
#msg2 = visual.TextStim(win2, text = """Please rate the background color""", color = "Black")
#msg2.draw()
#win2.flip()
#next = event.waitKeys()
#
#while rating_scale.noResponse:
#    rating_scale.draw()
#    win2.flip()
#    happyrating = rating_scale.getRating()
#    trial['happycolor'] = happyrating
#if key[0] in ['escape']:
#    core.quit()
#    
#win.close()
#core.quit()


