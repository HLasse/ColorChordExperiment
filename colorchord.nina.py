#load libraries

from psychopy import visual, core, event, gui, sound
from random import sample, randint
import ppc # PPC save rows. Made by Kristian. 
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
    day = int(popup.data[2]) # Int makes into a numerous string and not a text string so we can use the birthdays. 
    gender = popup.data[3]
    musician = popup.data[4]
else:
    core.quit()

# defining variables
trial_list = [] # Empty list for all out files.
audio_stim = glob.glob('ExperimentStims/*.wav') # Opload all our soundfiles. The star gets files that ends with wav. 

# setting conditions and defining windows
#if randint(0,1) == 0
if day < 15:
    condition = 'happy'
    win = visual.Window(fullscr = True, color = 'Yellow') # Hvis dag er under 15 s pop-up condition happy med yellow baggrundfarve.
else:
    condition = 'sad'
    win = visual.Window(fullscr = True, color = 'MightnightBlue') # Ellers pop-up condition sad of mrkebl. 


# preparing list of trials
for stim in audio_stim[0:2]: # For hver lydfil laver den en dictionary
    trial_list += [{ # dictionary: curly bracket = key value feks "ID" + value ID,
    'ID' : ID,
    'Age' : age,
    'Gender' : gender,
    'day born' : day,
    'musician' : musician,
    'condition' : condition,
    'stim': stim,
    'rating' : '',
    'happycolor' : '',
#    'sadcolor' : '',
    }]

# randomizing order
trial_list = sample(trial_list, len(trial_list))# Get the sounds in random order. 

# adding trial numbers
for i, trial in enumerate(trial_list): # Assign a number to each row. 
    trial['no'] = i + 1


# intro screen
msg = visual.TextStim(win, text = """Thank you for participating in our experiment.\n 
Throughout the experiment you will be presented with a number of sounds, which we would like you to rate on a scale from 1 to 10,
1 being very sad and 10 being very happy.\n Feel free to ask the experimenter any questions you might have.\n 
The experiment will take approximately 3 minutes.""", color = "Grey")
msg.draw()
win.flip()
key = event.waitKeys()
if key[0] in ['escape']:core.quit()


# creating rating scale
rating_scale = visual.RatingScale(win, markerColor = "White", 
scale = "Very Sad         ...         Very Happy", low =  1, high = 10, # creating a scale from 1 - 10. 
textColor = "Grey", lineColor = "Grey")

# creating writer
writer = ppc.csvWriter(ID, saveFolder='data', headerTrial=trial_list[0])# We send the trial list to the file with ID as a definer. 

print trial_list

# loop through trials
for trial in trial_list:
#    if trial['condition'] == 'happy':
        stim = sound.Sound(trial['stim']) # Play sound.sound. stim the sounds that we loaded. We refer to key value "stim" in our dictionary. 
        stim.play() # Play sound. 
        while rating_scale.noResponse:
            rating_scale.draw()
            win.flip()
        answer = rating_scale.getRating() # saving ratin as answer 
        trial['rating'] = answer # Adding answer to key value "rating." 
        rating_scale.reset() # reset rating scale to get ready for a new round. 
#    elif trial['condition'] == 'sad':
#        stim = sound.Sound(trial['stim']) 
#        stim.play()
#        while rating_scale.noResponse:
#            rating_scale.draw()
#            win.flip()
#        answer = rating_scale.getRating()
#        trial['rating'] = answer
#        rating_scale.reset()
# Too early to write here, we dont know the rating for the backgound!    writer.write(trial) # Everytime et goes trough 1 sounds it saves it in the datafile. 


win2 = visual.Window(fullscr = True, color =  'Green')
msg2 = visual.TextStim(win2, text = """Please rate the background color""", color = "Black")
msg2.draw()
win2.flip()
next = event.waitKeys()
#
# creating rating scale
rating_scale = visual.RatingScale(win2, markerColor = "White", 
scale = "Very Sad         ...         Very Happy", low =  1, high = 10, # creating a scale from 1 - 10. 
textColor = "Grey", lineColor = "Grey")

print('Waiting for background rating')

while rating_scale.noResponse:
    rating_scale.draw()
    win2.flip()
print('Rating scale has response')
happyrating = rating_scale.getRating()

print('Writing background rating to all trials')
for trial in trial_list:
    trial['happycolor'] = happyrating
    writer.write(trial)

#trial['happycolor'] = happyrating


#if key[0] in ['escape']:
#    core.quit()
    
#win.close()
#core.quit()

# Save in another file and with same ID. 
print('Closing window and shutting down program')
win.close()
core.quit()