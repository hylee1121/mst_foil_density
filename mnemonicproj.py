#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on Tue Jul  5 15:42:46 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

ATM 7/13/2022

TO DO:
    1) Finish the retrieval dictionary of lists, using list comprehension similar to the ENC_RUN_TRIALS syntax #finally..completed..but...in a bit weird way..
    2) Add a indoor/outdoor response during the encoding trials to ensure people are attending (NOT SELF TIMED) #completed
    2a) write a separate datFile that has the image name, response given, and the latency of the response #completed
    3) Make the confidence judgment self-paced rather than timed - follow the example of the retrieval image response syntax #completed


"""
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'mstfoil'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# ATM 7/6/2022 added
import pandas as pd
# Ensure that relative paths start from the same directory as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# The following code all deals with setting up the encoding and recognition trial structure across runs ### modified by HLee
encodingtrials_lists = pd.read_excel(f"data/sub-{expInfo['participant']}/encoding.xlsx")

# CREATE A DICTIONARY BELOW CALLED ENC_RUN_TRIALS THAT LOOKS LIKE THE FOLLOWING:
# ENC_RUN_TRIALS = {1: [{"stim":'SetC/001a.jpg'}, {"stim":'SetC/002a.jpg'},{"stim":'SetC/003a.jpg'}, ..., {"stim":'SetC/045a.jpg'}],
 #                                   2: [{"stim":'SetC/046a.jpg'}, {"stim":'SetC/047a.jpg'},{"stim":'SetC/048a.jpg'},..., {"stim":'SetC/090a.jpg'}],
 # ...
 #                                    4: [{"stim":'SetC/100a.jpg'}, {"stim":'SetC/101a.jpg'},{"stim":'SetC/102a.jpg'}, ..., {"stim":'SetC/145a.jpg'}]}
ENC_RUN_TRIALS = {
    ENCRUN: [{"stim": curr_enc_img} for curr_enc_img in encodingtrials_lists[f"encoding{ENCRUN}"]]
    for ENCRUN in range(1,5)
}
recognitionblocks_lists = {RECRUN: pd.read_excel(f"data/sub-{expInfo['participant']}/recognition{RECRUN}.xlsx") for RECRUN in range(1,5)}
#recognitionblocks_lists = pd.read_excel(f"data/sub-{expInfo['participant']}/recognition.xlsx")


# REC_RUN_BLOCKS = {
#     RECRUN: [{"rec_list": curr_rec_list} for curr_rec_list in recognitionblocks_lists[f"recog_list{RECRUN}"]]
#     for RECRUN in range(1,5)
# }

# REC_RUN_CRESPS = {
#     RECRUN: [{"rec_cresp": curr_recog_cresp} for curr_recog_cresp in recognitionblocks_lists[f"cresp{RECRUN}"]]
#     for RECRUN in range(1,5)
# }
#recognitionblocks_lists = {RECRUN: pd.read_excel(f"data/sub-{expInfo['participant']}/recognition{RECRUN}.xlsx") for RECRUN in range(1,5)}
# REC_RUN_TRIALS = {
#     RECRUN: [{"rec_stim": curr_rec_img} for curr_rec_img in recognitiontrials_lists[f"rec_stim{RECRUN}"]]
#     for RECRUN in range(1, 5)
# }
#RET_RUN = {RECRUN: pd.read_excel(f"data/sub-{expInfo['participant']}/retrieval{RECRUN}.xlsx") for RECRUN in range(1,5)}

# CREATE A DICTIONARY BELOW CALLED RET_RUN_TRIALS THAT LOOKS LIKE THE FOLLOWING:
# RET_RUN_TRIALS = {1: [{'stim': 'SetC/001a.jpg', 'type': 'targ'}, {'stim': 'SetC/002a.jpg', 'type': 'targ'}, ...,  {'stim': 'SetC/048b.jpg', 'type': 'lure'}],
#                                   2: [{'stim': 'SetC/049a.jpg', 'type': 'targ'}, {'stim': 'SetC/050a.jpg', 'type': 'targ'}, ..., {'stim': 'SetC/108a.jpg', 'type': 'foil'}],
 # ...
 #                                    4: [{'stim': 'SetC/181a.jpg', 'type': 'targ'}, {'stim': 'SetC/182a.jpg', 'type': 'targ'}, ..., {'stim': 'SetD/084a.jpg', 'type': 'foil'}]}
# REC_RUN_TRIALS = {
#     [{"stim_in_rec_trials": curr_rec_list} for curr_rec_list in recognitiontrial_lists["recog_stim"]]
# }

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = SCRIPT_DIR + os.sep + u'{0}_data/sub-{1}/ses-S1/{2}/sub-{1}_task-mstfoil_events'.format(expName, expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
# ATM 7/6/2022 edited for readability
thisExp = data.ExperimentHandler(
    name=expName,
    version='',
    extraInfo=expInfo,
    runtimeInfo=None,
    originPath=None,
    savePickle=True,
    saveWideText=True,
    dataFileName=filename,
)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900],
    fullscr=True,
    screen=0,
    winType='pyglet',
    allowGUI=False,
    allowStencil=False,
    monitor='testMonitor',
    color=[1,1,1],
    colorSpace='rgb',
    blendMode='avg',
    useFBO=True,
    units='height')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

welcome_message = """Hello, thanks for your participation.

This experiment consists of a total of FOUR blocks.

In each block, you'll see pictures, after which

you'll play a Sudoku game and do memory tests.


Press “M” to move on to the next screen."""

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(
    win=win,
    name='welcome_text',
    text=welcome_message,
    font='Open Sans',
    pos=(0, 0),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);
welcome_resp = keyboard.Keyboard()

# Initialize components for Routine "ready_block" ###edited by HLee
# encoding_instruct_message = """You are in block {0}
#
# Now, you will see the pictures, each for 2 seconds.
#
# After that, please answer whether the object you saw is for indoor or outdoor use.
#
#
# H = Indoor,
#
# J = Outdoor,
#
# K = Ambiguous,
#
# L = I forgot what I just saw.
#
#
# When you are ready to begin, press the "R" key."""

encoding_intructClock = core.Clock()
encoding_instruct_text = visual.TextStim(
    win=win,
    name='encoding_instruct_text',
    text=None,
    font='Open Sans',
    pos=(0, 0),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);
encoding_instruct_resp = keyboard.Keyboard()

# Initialize components for Routine "fixationcross"
fixationcrossClock = core.Clock()
fixation = visual.TextStim(
    win=win,
    name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ecd_trial"
encoding_imgClock = core.Clock()
encoding_img = visual.ImageStim(
    win=win,
    name='encoding_img',
    image=None,
    mask=None,
    ori=0.0,
    pos=(0, 0),
    size=None, #(0.5, 0.5),
    color=[1,1,1],
    colorSpace='rgb',
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=False,
    depth=0.0)

# Initialize components for Routine "inandout_decision" ### added by HLee
inandout_decClock = core.Clock()

inandout_dec_instruct = visual.TextStim(
    win=win,
    name='inandout_dec_instruct',
    text='Please answer whether the object you saw is for indoor or outdoor use.',
    font='Open Sans',
    pos=(0, 0.3),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);

inandout_dec_options = visual.TextStim(
    win=win,
    name='inandout_resp_options',
    text="""
    H = indoor,

    J = outdoor,

    K = ambiguous,

    L = I forgot what I just saw""",
    font='Open Sans',
    pos=(0, 0),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=3.0);

inandout_dec_resp = keyboard.Keyboard()



# Initialize components for Routine "sudoku_intro"
sudoku_message = """Now, you will play Sudoku for 5 minutes.

Please use the paper and pen given to you.

If you don't know how to play Sudoku, refer to the instrctions.

Do your best! Your results will be analyzed.

When you are ready press the "R" key to start the timer.
"""
sudoku_instructClock = core.Clock()
sudoku_instructions = visual.TextStim(
    win=win,
    name='sudoku_instructions',
    text=sudoku_message,
    font='Open Sans',
    pos=(0, 0),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);
sudoku_instruct_resp = keyboard.Keyboard()

# Initialize components for Routine "sudoku_timer"
sudoku_timerClock = core.Clock()
sudoku_timer_text = visual.TextStim(
    win=win,
    name='sudoku_timer_text',
    text='',
    font='Open Sans',
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=-1.0);

recog_instruct_message = """Now you are going to do a memory test.

If the object that appears is what you just saw (old), press H.

If the object that appears is similar to what you saw (similar), press J.

If the object that appears is not what you saw (new), press K.

Then, rate how confident you are about your answer.

H = very certain,

J = somewhat certain,

K = somewhat uncertain,

L = very uncertain.

When you are ready to begin, press the "A" key.
"""

# Initialize components for Routine "recog_intro"
recognition_instructClock = core.Clock()
recognition_instruct = visual.TextStim(
    win=win,
    name='recognition_instruct',
    text=recog_instruct_message,
    font='Open Sans',
    pos=(0, 0),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);
recognition_instruct_resp = keyboard.Keyboard()

# Initialize components for Routine "rcg_trial"
recognition_imgClock = core.Clock()
recognition_img = visual.ImageStim(
    win=win,
    name='recognition_img',
    image=None,
    mask=None,
    ori=0.0,
    pos=(0, 0),
    size=None, #(0.5, 0.5),
    color=[1,1,1],
    colorSpace='rgb',
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=False,
    depth=0.0)
recognition_img_resp = keyboard.Keyboard()

recognition_resp_prompt_main = visual.TextStim(
    win=win,
    name='recognition_resp_prompt_main',
    text='Please select from the responses below.',
    font='Open Sans',
    pos=(0, 0.35),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=-2.0);
recognition_resp_prompt_options = visual.TextStim(
    win=win,
    name='recognition_resp_prompt_options',
    text='H = old,   J = similar,   K = new',
    font='Open Sans',
    pos=(0, -0.35),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "confidence" ### modified by HLee
confidence_respClock = core.Clock()
confidence_resp_prompt_main = visual.TextStim(
    win=win,
    name='confidence_resp_prompt_main',
    text='Please rate your confidence in your answer.',
    font='Open Sans',
    pos=(0, 0.35),
    height=0.03,
    wrapWidth=None,
    ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);

confidence_ratebar = visual.ImageStim(
    win=win,
    name='confidence_ratebar',
    image='ratebar.png',
    mask=None,
    ori=0.0,
    pos=(0, -0.05),
    size=(1.2, 0.7),
    color=[1,1,1],
    colorSpace='rgb',
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=False,
    depth=-1.0)
confidence_resp = keyboard.Keyboard()

# Initialize components for Routine "ExpEnd"
ExpEndClock = core.Clock()
byebye = visual.TextStim(
    win=win,
    name='byebye',
    text='Thank you for your participation.\nPlease enter any key to exit this screen.',
    font='Open Sans',
    pos=(0, 0),
    height=0.03,
    wrapWidth=None, ori=0.0,
    color='black',
    colorSpace='rgb',
    opacity=None,
    languageStyle='LTR',
    depth=0.0);
bye_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine


#############################################################################################
################################ Components of the main loop ################################
# 1) "welcome" routine
# 2) "ready" routine; explains the whole procedure

############################# 3) - 6) will repeat four times. ###############################
# 3) Encoding loop (repeats 48 times within each block)
 # 3a) "encoding_instructions"; It tells you which block you are in.
 # 3b) "fixationcross"; lasts 0.5s
 # 3c) "encoding_img"; It shows objects that you have to remember for the recognition tests, 2s
 # 3d) "inandout_decision";
        # A task to determine whether the object you saw is for indoor or outdoor use.
        # This is for the purpose of verifying the encoding.
        # Stimuli for which the "I forgot what I just saw" option were selected can be excluded from recognition data analysis.

# 4) Sudoku Loop
 # 4a) "sudoku_intro"; It lets participants know that they will play a sudoku game
 # 4b) "sudoku_instructions" ;
       # how to play will explain via paper
       # because it's repeated routine
       # so I don't want people to see the same long explanation multiple times
 # 4c) "sudoku_timer"; 300s count down timer

# 5) "recog_intro"; It lets participants know that they will do a recognition test with confidence checking

# 6) Recognition Loop (repeats 48, 60, 72, or 96 within each block)
      # 48 - 24 targets & 24 lures / 60 - 24 targets, 24 lures, & 12 foils
      # 72 - 24 targets, 24 lures, & 24 foils / 96 - 24 targets, 24 lures, & 48 foils

 # 6a) "fixationcross"; lasts 0.5s
 # 6b) "rcg_trial"; self-paced task asking whether you saw objects before or not
 # 6c) "confidence"; self-paced question asking their deicision
#############################################################################################

# 7) "ExpEnd" routine; It lets participants know that they're done with the experiment

#############################################################################################


#############################################################################################
################################## Start of the main loop ###################################
#############################################################################################


# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_resp.keys = []
welcome_resp.rt = []
_welcome_resp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, welcome_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)

    # *welcome_resp* updates
    waitOnFlip = False
    if welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_resp.getKeys(keyList=['m'], waitRelease=False)
        _welcome_resp_allKeys.extend(theseKeys)
        if len(_welcome_resp_allKeys):
            welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
            welcome_resp.rt = _welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# check responses
if welcome_resp.keys in ['', [], None]:  # No response was made
    welcome_resp.keys = None
thisExp.addData('welcome_resp.keys',welcome_resp.keys)
if welcome_resp.keys != None:  # we had a response
    thisExp.addData('welcome_resp.rt', welcome_resp.rt)
thisExp.addData('welcome_resp.started', welcome_resp.tStartRefresh)
thisExp.addData('welcome_resp.stopped', welcome_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ATM 7/7/2022 added....iterating over 4 runs hard coded.
for _run in range(1, 5):

    #encoding_instruct_message = encoding_instruct_message.format(_run)
    encoding_instruct_message = """You are in block %d.

    Now, you will see the pictures, each for 2 seconds.

    After that, please answer whether the object you saw is for indoor or outdoor use.


    H = Indoor,

    J = Outdoor,

    K = Ambiguous,

    L = I forgot what I just saw.


    When you are ready to begin, press the "R" key.""" % _run


    datFile_base = SCRIPT_DIR + "/mstfoil_data/sub-{0}/ses-S1/{1}/sub-{0}_task-mstfoil_events".format(expInfo["participant"], expInfo["date"])
    # If restart occurs within the same minute, prevents writing to same file
    if os.path.exists(datFile_base + ".tsv"):
        datFile_base += "_latest"

    datFile = open(datFile_base + ".tsv", "a",)
    datFile.write("trial_type\trecog_resp\trecog_resp_time\tconfi_resp\tconfi_resp_time\tstim_file\tperformance\n")

    # ------Prepare to start Routine "ready_intructions_block"-------
    continueRoutine = True
    # update component parameters for each repeat
    encoding_instruct_resp.keys = []
    encoding_instruct_resp.rt = []
    _encoding_instruct_resp_allKeys = []
    encoding_instruct_text.text = encoding_instruct_message
    # keep track of which components have finished
    encoding_instructComponents = [encoding_instruct_text, encoding_instruct_resp]
    for thisComponent in encoding_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    encoding_intructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "encoding_instructions"-------
    while continueRoutine:
        # get current time
        t = encoding_intructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=encoding_intructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text* updates
        if encoding_instruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_instruct_text.frameNStart = frameN  # exact frame index
            encoding_instruct_text.tStart = t  # local t and not account for scr refresh
            encoding_instruct_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_instruct_text, 'tStartRefresh')  # time at next scr refresh
            encoding_instruct_text.setAutoDraw(True)

        # *key_resp* updates
        waitOnFlip = False
        if encoding_instruct_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_instruct_resp.frameNStart = frameN  # exact frame index
            encoding_instruct_resp.tStart = t  # local t and not account for scr refresh
            encoding_instruct_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_instruct_resp, 'tStartRefresh')  # time at next scr refresh
            encoding_instruct_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(encoding_instruct_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(encoding_instruct_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if encoding_instruct_resp.status == STARTED and not waitOnFlip:
            theseKeys = encoding_instruct_resp.getKeys(keyList=['r'], waitRelease=False)
            _encoding_instruct_resp_allKeys.extend(theseKeys)
            if len(_encoding_instruct_resp_allKeys):
                encoding_instruct_resp.keys = _encoding_instruct_resp_allKeys[-1].name  # just the last key pressed
                encoding_instruct_resp.rt = _encoding_instruct_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in encoding_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "encoding_instructions"-------
    for thisComponent in encoding_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ready_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    curr_enc_run = ENC_RUN_TRIALS[_run] #ATM 7/7/2022 added
    encoding_trials_block = data.TrialHandler(
        nReps=1.0,
        method='sequential',
        extraInfo=expInfo,
        originPath=-1,
        trialList=curr_enc_run, #ATM 7/7/2022 added this
        seed=None,
        name='encoding_trials_block')
    thisExp.addLoop(encoding_trials_block)  # add the loop to the experiment
    thisEncoding_trials_block = encoding_trials_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEcd_block.rgb)
    if thisEncoding_trials_block != None:
        for paramName in thisEncoding_trials_block:
            exec('{} = thisEncoding_trials_block[paramName]'.format(paramName))

    for thisEncoding_trials_block in encoding_trials_block:
        currentLoop = encoding_trials_block
        # abbreviate parameter names if possible (e.g. rgb = thisEcd_block.rgb)
        if thisEncoding_trials_block != None:
            for paramName in thisEncoding_trials_block:
                exec('{} = thisEncoding_trials_block[paramName]'.format(paramName))

        # ------Prepare to start Routine "fixationcross"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixation]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationcrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "fixationcross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationcrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationcrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *polygon* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "fixationcross"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        encoding_trials_block.addData('fixation.started', fixation.tStartRefresh)
        encoding_trials_block.addData('fixation.stopped', fixation.tStopRefresh)

        # ------Prepare to start Routine "encoding_trials"-------
        continueRoutine = True
        routineTimer.add(2.00000)
        #routineTimer.add(0.01000)
        # update component parameters for each repeat
        encoding_img.image = thisEncoding_trials_block.stim #ATM 7/7/2022 added
        # keep track of which components have finished
        encoding_imgComponents = [encoding_img]
        for thisComponent in encoding_imgComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        encoding_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "encoding_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = encoding_imgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=encoding_imgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *ecd_img* updates
            if encoding_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                encoding_img.frameNStart = frameN  # exact frame index
                encoding_img.tStart = t  # local t and not account for scr refresh
                encoding_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encoding_img, 'tStartRefresh')  # time at next scr refresh
                encoding_img.setAutoDraw(True)
            if encoding_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encoding_img.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    encoding_img.tStop = t  # not accounting for scr refresh
                    encoding_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(encoding_img, 'tStopRefresh')  # time at next scr refresh
                    encoding_img.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in encoding_imgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "encoding_trial"-------
        for thisComponent in encoding_imgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        encoding_trials_block.addData('encoding_img.started', encoding_img.tStartRefresh)
        encoding_trials_block.addData('encoding_img.stopped', encoding_img.tStopRefresh)

        # ------Prepare to start Routine "inandout_dec"-------
        continueRoutine = True
        # update component parameters for each repeat
        inandout_dec_resp.keys = []
        inandout_dec_resp.rt = []
        _inandout_dec_resp_allKeys = []
        # keep track of which components have finished
        inandout_decComponents = [inandout_dec_instruct, inandout_dec_options, inandout_dec_resp]
        for thisComponent in inandout_decComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset _timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inandout_decClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "inandout_dec"-------
        while continueRoutine:
            #get current time
            t = inandout_decClock.getTime()
            tThisFlip =  win.getFutureFlipTime(clock=inandout_decClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1 # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *inandout_dec_instruct* updates
            if inandout_dec_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inandout_dec_instruct.frameNStart = frameN # exact frame index
                inandout_dec_instruct.tStart = t  # local t and not account for scr refresh
                inandout_dec_instruct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inandout_dec_instruct, 'tStartRefresh')  # time at next scr refresh
                inandout_dec_instruct.setAutoDraw(True)

            # *inandout_dec_options* updates
            if inandout_dec_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inandout_dec_options.frameNStart = frameN  # exact frame index
                inandout_dec_options.tStart = t  # local t and not account for scr refresh
                inandout_dec_options.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inandout_dec_options, 'tStartRefresh')  # time at next scr refresh
                inandout_dec_options.setAutoDraw(True)

            # "inandout_dec_resp" updates
            waitOnFlip = False
            if inandout_dec_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inandout_dec_resp.frameNStart = frameN  # exact frame index
                inandout_dec_resp.tStart = t  # local t and not account for scr refresh
                inandout_dec_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inandout_dec_resp, 'tStartRefresh')  # time at next scr refresh
                inandout_dec_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(inandout_dec_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(inandout_dec_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if inandout_dec_resp.status == STARTED and not waitOnFlip:
                theseKeys = inandout_dec_resp.getKeys(keyList=['h', 'j', 'k', 'l'], waitRelease=False)
                _inandout_dec_resp_allKeys.extend(theseKeys)
                if len(_inandout_dec_resp_allKeys):
                    inandout_dec_resp.keys = _inandout_dec_resp_allKeys[-1].name  # just the last key pressed
                    inandout_dec_resp.rt = _inandout_dec_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inandout_decComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "inandout_decision"-------
        for thisComponent in inandout_decComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        encoding_trials_block.addData('inandout_dec_instruct.started', inandout_dec_instruct.tStartRefresh)
        encoding_trials_block.addData('inandout_dec_instruct.stopped', inandout_dec_instruct.tStartRefresh)
        # check responses
        if inandout_dec_resp.keys in ['', [], None]:  # No response was made
            inandout_dec_resp.keys = None

        # store data for encoding_trials_block (TrialHandler)
        encoding_trials_block.addData('inandout_dec_resp.keys',inandout_dec_resp.keys)
        encoding_trials_block.addData('inandout_dec_resp.corr', inandout_dec_resp.corr)
        if inandout_dec_resp.keys != None:  # we had a response
            encoding_trials_block.addData('inandout_dec_resp.rt', inandout_dec_resp.rt)
        encoding_trials_block.addData('inandout_dec_resp.started', inandout_dec_resp.tStartRefresh)
        encoding_trials_block.addData('inandout_dec_resp.stopped', inandout_dec_resp.tStopRefresh)
        encoding_trials_block.addData('inandout_dec_options.started', inandout_dec_options.tStartRefresh)
        encoding_trials_block.addData('inandout_dec_options.stopped', inandout_dec_options.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1.0 repeats of 'ecd_block'





    # ------Prepare to start Routine "sudoku_intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    sudoku_instruct_resp.keys = []
    sudoku_instruct_resp.rt = []
    _sudoku_instruct_resp_allKeys = []
    # keep track of which components have finished
    sudoku_instructComponents = [sudoku_instructions, sudoku_instruct_resp]
    for thisComponent in sudoku_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sudoku_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "sudoku_instructions"-------
    while continueRoutine:
        # get current time
        t = sudoku_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sudoku_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *before_sudoku* updates
        if sudoku_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sudoku_instructions.frameNStart = frameN  # exact frame index
            sudoku_instructions.tStart = t  # local t and not account for scr refresh
            sudoku_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sudoku_instructions, 'tStartRefresh')  # time at next scr refresh
            sudoku_instructions.setAutoDraw(True)

        # *key_resp_mk* updates
        waitOnFlip = False
        if sudoku_instruct_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sudoku_instruct_resp.frameNStart = frameN  # exact frame index
            sudoku_instruct_resp.tStart = t  # local t and not account for scr refresh
            sudoku_instruct_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sudoku_instruct_resp, 'tStartRefresh')  # time at next scr refresh
            sudoku_instruct_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sudoku_instruct_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sudoku_instruct_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sudoku_instruct_resp.status == STARTED and not waitOnFlip:
            theseKeys = sudoku_instruct_resp.getKeys(keyList=['r'], waitRelease=False)
            _sudoku_instruct_resp_allKeys.extend(theseKeys)
            if len(_sudoku_instruct_resp_allKeys):
                sudoku_instruct_resp.keys = _sudoku_instruct_resp_allKeys[-1].name  # just the last key pressed
                sudoku_instruct_resp.rt = _sudoku_instruct_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sudoku_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "sudoku_instructions"-------
    for thisComponent in sudoku_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if sudoku_instruct_resp.keys in ['', [], None]:  # No response was made
        sudoku_instruct_resp.keys = None
    # the Routine "sudoku_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "sudoku_timer"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    sudoku_timer = core.CountdownTimer(5)
    # keep track of which components have finished
    sudoku_timer_textComponents = [sudoku_timer_text]
    for thisComponent in sudoku_timer_textComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sudoku_timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "sudoku_timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sudoku_timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sudoku_timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        current_time = round(sudoku_timer.getTime())

        if current_time > 0:
            message = f'You have {current_time} s left.'
        if current_time == 0:
            message = 'Time is up!'

        # *text_timer* updates
        if sudoku_timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sudoku_timer_text.frameNStart = frameN  # exact frame index
            sudoku_timer_text.tStart = t  # local t and not account for scr refresh
            sudoku_timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sudoku_timer_text, 'tStartRefresh')  # time at next scr refresh
            sudoku_timer_text.setAutoDraw(True)
        if sudoku_timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sudoku_timer_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                sudoku_timer_text.tStop = t  # not accounting for scr refresh
                sudoku_timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sudoku_timer_text, 'tStopRefresh')  # time at next scr refresh
                sudoku_timer_text.setAutoDraw(False)
        if sudoku_timer_text.status == STARTED:  # only update if drawing
            sudoku_timer_text.setText(message, log=False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sudoku_timer_textComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "sudoku_timer"-------
    for thisComponent in sudoku_timer_textComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "recog_intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    recognition_instruct_resp.keys = []
    recognition_instruct_resp.rt = []
    _recognition_instruct_resp_allKeys = []
    # keep track of which components have finished
    recognition_instructComponents = [recognition_instruct, recognition_instruct_resp]
    for thisComponent in recognition_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recognition_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "recog_intro"-------
    while continueRoutine:
        # get current time
        t = recognition_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recognition_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *intro_recogtest* updates
        if recognition_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_instruct.frameNStart = frameN  # exact frame index
            recognition_instruct.tStart = t  # local t and not account for scr refresh
            recognition_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_instruct, 'tStartRefresh')  # time at next scr refresh
            recognition_instruct.setAutoDraw(True)

        # *key_resp_recog* updates
        waitOnFlip = False
        if recognition_instruct_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_instruct_resp.frameNStart = frameN  # exact frame index
            recognition_instruct_resp.tStart = t  # local t and not account for scr refresh
            recognition_instruct_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_instruct_resp, 'tStartRefresh')  # time at next scr refresh
            recognition_instruct_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(recognition_instruct_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(recognition_instruct_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if recognition_instruct_resp.status == STARTED and not waitOnFlip:
            theseKeys = recognition_instruct_resp.getKeys(keyList=['a'], waitRelease=False)
            _recognition_instruct_resp_allKeys.extend(theseKeys)
            if len(_recognition_instruct_resp_allKeys):
                recognition_instruct_resp.keys = _recognition_instruct_resp_allKeys[-1].name  # just the last key pressed
                recognition_instruct_resp.rt = _recognition_instruct_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recognition_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "recog_intro"-------
    for thisComponent in recognition_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # check responses
    if recognition_instruct_resp.keys in ['', [], None]:  # No response was made
        recognition_instruct_resp.keys = None
    # the Routine "recog_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # curr_rec_run = REC_RUN_TRIALS[_run] #ATM 7/7/2022 added
    # #set up handler to look after randomisation of conditions etc
    # recognition_trials_block = data.TrialHandler(
    #     nReps=1.0,
    #     method='sequential',
    #     extraInfo=expInfo,
    #     originPath=-1,
    #     trialList=curr_rec_run, #ATM 7/7/2022 added
    #     seed=None,
    #     name='rcg_block')
    # thisExp.addLoop(recognition_trials_block)  # add the loop to the experiment
    # thisRecognition_trials_block = recognition_trials_block.trialList[0]  # so we can initialise stimuli with some values
    # # abbreviate parameter names if possible (e.g. rgb = thisRcg_block.rgb)
    # if thisRecognition_trials_block != None:
    #     for paramName in thisRecognition_trials_block:
    #         exec('{} = thisRecognition_trials_block[paramName]'.format(paramName))
    #
    # for thisRecognition_trials_block in recognition_trials_block:
    #     currentLoop = recognition_trials_block
    #     # abbreviate parameter names if possible (e.g. rgb = thisRcg_block.rgb)
    #     if thisRecognition_trials_block != None:
    #         for paramName in thisRecognition_trials_block:
    #             exec('{} = thisRecognition_trials_block[paramName]'.format(paramName))

    # curr_rec_run = recognitionblocks_lists
    # #set up handler to look after randomisation of conditions etc ### added by HLee
    # recoglistloop = data.TrialHandler(nReps=1.0, method='sequential',
    #     extraInfo=expInfo, originPath=-1,
    #     trialList=curr_rec_run,
    #     seed=None, name='recoglistloop')
    # thisExp.addLoop(recoglistloop)  # add the loop to the experiment
    # thisRecoglistloop = recoglistloop.trialList[0]  # so we can initialise stimuli with some values
    # # abbreviate parameter names if possible (e.g. rgb = thisRecoglistloop.rgb)
    # if thisRecoglistloop != None:
    #     for paramName in thisRecoglistloop:
    #         exec('{} = thisRecoglistloop[paramName]'.format(paramName))
    #
    # for thisRecoglistloop in recoglistloop:
    #     currentLoop = recoglistloop
    #     # abbreviate parameter names if possible (e.g. rgb = thisRecoglistloop.rgb)
    #     if thisRecoglistloop != None:
    #         for paramName in thisRecoglistloop:
    #             exec('{} = thisRecoglistloop[paramName]'.format(paramName))


    #curr_rec_run = recognitionblocks_lists[_run]
        # set up handler to look after randomisation of conditions etc
    recognition_trials_block = data.TrialHandler(nReps=1.0, method='sequential',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(f"data/sub-{expInfo['participant']}/recognition{_run}.xlsx"), ### modified by HLee
        seed=None, name='recognition_trials_block')
    thisExp.addLoop(recognition_trials_block)  # add the loop to the experiment
    thisRecognition_trials_block = recognition_trials_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecognition_trials_block.rgb)
    if thisRecognition_trials_block != None:
        for paramName in thisRecognition_trials_block:
            exec('{} = thisRecognition_trials_block[paramName]'.format(paramName))

    for thisRecognition_trials_block in recognition_trials_block:
        currentLoop = recognition_trials_block
        # abbreviate parameter names if possible (e.g. rgb = thisRecognition_trials_block.rgb)
        if thisRecognition_trials_block != None:
            for paramName in thisRecognition_trials_block:
                exec('{} = thisRecognition_trials_block[paramName]'.format(paramName))

        # ------Prepare to start Routine "fixationcross"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixation]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationcrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "fixationcross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationcrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationcrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *polygon* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "fixationcross"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        recognition_trials_block.addData('fixation.started', fixation.tStartRefresh)
        recognition_trials_block.addData('fixation.stopped', fixation.tStopRefresh)

        # ------Prepare to start Routine "recognition_trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        #recognition_img.image = thisRecognition_trials_block.rec_stim # ATM 7/7/2022 added
        recognition_img.setImage(recog_stim) # modified by HLee
        recognition_img_resp.keys = []
        recognition_img_resp.rt = []
        _recognition_img_resp_allKeys = []
        # keep track of which components have finished
        recognition_trialComponents = []
        recognition_trialComponents.append(recognition_img)
        recognition_trialComponents.append(recognition_img_resp)
        recognition_trialComponents.append(recognition_resp_prompt_main)
        recognition_trialComponents.append(recognition_resp_prompt_options)
        for thisComponent in recognition_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        recognition_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "recognition_trial"-------
        while continueRoutine:
            # get current time
            t = recognition_imgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=recognition_imgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *recognition_img* updates
            if recognition_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recognition_img.frameNStart = frameN  # exact frame index
                recognition_img.tStart = t  # local t and not account for scr refresh
                recognition_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recognition_img, 'tStartRefresh')  # time at next scr refresh
                recognition_img.setAutoDraw(True)

            # *recognition_img_resp* updates
            waitOnFlip = False
            if recognition_img_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recognition_img_resp.frameNStart = frameN  # exact frame index
                recognition_img_resp.tStart = t  # local t and not account for scr refresh
                recognition_img_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recognition_img_resp, 'tStartRefresh')  # time at next scr refresh
                recognition_img_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(recognition_img_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(recognition_img_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if recognition_img_resp.status == STARTED and not waitOnFlip:
                theseKeys = recognition_img_resp.getKeys(keyList=['h','j','k'], waitRelease=False)
                _recognition_img_resp_allKeys.extend(theseKeys)
                if len(_recognition_img_resp_allKeys):
                    recognition_img_resp.keys = _recognition_img_resp_allKeys[-1].name  # just the last key pressed
                    recognition_img_resp.rt = _recognition_img_resp_allKeys[-1].rt
                    # was this correct?
                    if (recognition_img_resp.keys == str(cresp)) or (recognition_img_resp.keys == cresp):
                     recognition_img_resp.corr = 1
                    else:
                       recognition_img_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # *ecognition_resp_prompt_main* updates
            if recognition_resp_prompt_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recognition_resp_prompt_main.frameNStart = frameN  # exact frame index
                recognition_resp_prompt_main.tStart = t  # local t and not account for scr refresh
                recognition_resp_prompt_main.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recognition_resp_prompt_main, 'tStartRefresh')  # time at next scr refresh
                recognition_resp_prompt_main.setAutoDraw(True)

            # *recognition_resp_prompt_options* updates
            if recognition_resp_prompt_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recognition_resp_prompt_options.frameNStart = frameN  # exact frame index
                recognition_resp_prompt_options.tStart = t  # local t and not account for scr refresh
                recognition_resp_prompt_options.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recognition_resp_prompt_options, 'tStartRefresh')  # time at next scr refresh
                recognition_resp_prompt_options.setAutoDraw(True)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recognition_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "recognition_trial"-------
        for thisComponent in recognition_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        recognition_trials_block.addData('recognition_img.started', recognition_img.tStartRefresh)
        recognition_trials_block.addData('recognition_img.stopped', recognition_img.tStopRefresh)
        # check responses
        if recognition_img_resp.keys in ['', [], None]:  # No response was made
            recognition_img_resp.keys = None
            # was no response the correct answer?!
            if str(cresp).lower() == 'none':
               recognition_img_resp.corr = 1;  # correct non-response
            else:
               recognition_img_resp.corr = 0;  # failed to respond (incorrectly)

        # store data for recognition_trials_block (TrialHandler)
        recognition_trials_block.addData('recognition_img_resp.keys',recognition_img_resp.keys)
        recognition_trials_block.addData('recognition_img_resp.corr', recognition_img_resp.corr)
        if recognition_img_resp.keys != None:  # we had a response
            recognition_trials_block.addData('recognition_img_resp.rt', recognition_img_resp.rt)
        recognition_trials_block.addData('recognition_img_resp.started', recognition_img_resp.tStartRefresh)
        recognition_trials_block.addData('recognition_img_resp.stopped', recognition_img_resp.tStopRefresh)
        recognition_trials_block.addData('recognition_resp_prompt_main.started', recognition_resp_prompt_main.tStartRefresh)
        recognition_trials_block.addData('recognition_resp_prompt_main.stopped', recognition_resp_prompt_main.tStopRefresh)
        recognition_trials_block.addData('recognition_resp_prompt_options.started', recognition_resp_prompt_options.tStartRefresh)
        recognition_trials_block.addData('recognition_resp_prompt_options.stopped', recognition_resp_prompt_options.tStopRefresh)
        # the Routine "rcg_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "confidence"-------
        continueRoutine = True
        #routineTimer.add(5.000000)
        # update component parameters for each repeat
        confidence_resp.keys = []
        confidence_resp.rt = []
        _confidence_resp_allKeys = []
        # keep track of which components have finished
        confidenceComponents = [confidence_resp_prompt_main, confidence_ratebar, confidence_resp]
        for thisComponent in confidenceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        confidence_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "confidence"-------
        while continueRoutine:
        #while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = confidence_respClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=confidence_respClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *confidenceQ* updates
            if confidence_resp_prompt_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidence_resp_prompt_main.frameNStart = frameN  # exact frame index
                confidence_resp_prompt_main.tStart = t  # local t and not account for scr refresh
                confidence_resp_prompt_main.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_resp_prompt_main, 'tStartRefresh')  # time at next scr refresh
                confidence_resp_prompt_main.setAutoDraw(True)
            #if confidence_resp_prompt_main.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                #if tThisFlipGlobal > confidence_resp_prompt_main.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    #confidence_resp_prompt_main.tStop = t  # not accounting for scr refresh
                    #confidence_resp_prompt_main.frameNStop = frameN  # exact frame index
                    #win.timeOnFlip(confidence_resp_prompt_main, 'tStopRefresh')  # time at next scr refresh
                    #confidence_resp_prompt_main.setAutoDraw(False)

            # *ratebar* updates
            if confidence_ratebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidence_ratebar.frameNStart = frameN  # exact frame index
                confidence_ratebar.tStart = t  # local t and not account for scr refresh
                confidence_ratebar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_ratebar, 'tStartRefresh')  # time at next scr refresh
                confidence_ratebar.setAutoDraw(True)
            #if confidence_ratebar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                #if tThisFlipGlobal > confidence_ratebar.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    #confidence_ratebar.tStop = t  # not accounting for scr refresh
                    #confidence_ratebar.frameNStop = frameN  # exact frame index
                    #win.timeOnFlip(confidence_ratebar, 'tStopRefresh')  # time at next scr refresh
                    #confidence_ratebar.setAutoDraw(False)

            # *key_resp_conf* updates
            waitOnFlip = False
            if confidence_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidence_resp.frameNStart = frameN  # exact frame index
                confidence_resp.tStart = t  # local t and not account for scr refresh
                confidence_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_resp, 'tStartRefresh')  # time at next scr refresh
                confidence_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(confidence_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(confidence_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip

            #if confidence_resp.status == STARTED:
                ## is it time to stop? (based on global clock, using actual start)
                #if tThisFlipGlobal > confidence_resp.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    #confidence_resp.tStop = t  # not accounting for scr refresh
                    #confidence_resp.frameNStop = frameN  # exact frame index
                    #win.timeOnFlip(confidence_resp, 'tStopRefresh')  # time at next scr refresh
                    #confidence_resp.status = FINISHED
            if confidence_resp.status == STARTED and not waitOnFlip:
                theseKeys = confidence_resp.getKeys(keyList=['h','j','k','l'], waitRelease=False)
                _confidence_resp_allKeys.extend(theseKeys)
                if len(_confidence_resp_allKeys):
                    confidence_resp.keys = _confidence_resp_allKeys[-1].name  # just the last key pressed
                    confidence_resp.rt = _confidence_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in confidenceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "confidence"-------
        for thisComponent in confidenceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        recognition_trials_block.addData('confidence_resp_prompt_main.started', confidence_resp_prompt_main.tStartRefresh)
        recognition_trials_block.addData('confidence_resp_prompt_main.stopped', confidence_resp_prompt_main.tStopRefresh)
        recognition_trials_block.addData('confidence_ratebar.started', confidence_ratebar.tStartRefresh)
        recognition_trials_block.addData('confidence_ratebar.stopped', confidence_ratebar.tStopRefresh)
        # check responses
        if confidence_resp.keys in ['', [], None]:  # No response was made
            confidence_resp.keys = None
        recognition_trials_block.addData('confidence_resp.keys',confidence_resp.keys)
        if confidence_resp.keys != None:  # we had a response
            recognition_trials_block.addData('confidence_resp.rt', confidence_resp.rt)
        recognition_trials_block.addData('confidence_resp.started', confidence_resp.tStartRefresh)
        recognition_trials_block.addData('confidence_resp.stopped', confidence_resp.tStopRefresh)
        # the Routine "confidence" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

        # # datFile.write("trial_type\trecog_resp\trecog_resp_time\tconfi_resp\tconfi_resp_time\tstim_file\tperformance\n")
        # if thisRecognition_trials_block.type == 'target' and recognition_img_resp.keys == 'h':
        #     performance = 'correct'
        # elif thisRecognition_trials_block.type == 'lure' and recognition_img_resp.keys == 'j':
        #     performance = 'correct'
        # elif thisRecognition_trials_block.type == 'foil' and recognition_img_resp.keys == 'k':
        #     performance = 'correct'
        # else:
        #     performance = 'incorrect'
        #
        # datFile.write(
        #     "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format(
        #         thisRecognition_trials_block.type,
        #         recognition_img_resp.keys,
        #         recognition_img_resp.rt,
        #         confidence_resp.keys,
        #         confidence_resp.rt,
        #         thisRecognition_trials_block.rec_stim,
        #         #recognition_img.setImage(recog_stim),
        #         performance,
        #     )
        # )


        # completed 1.0 repeats of 'recognition_trials_block'

        thisExp.nextEntry()

    ## completed 1.0 repeats of 'recoglistloop'

    #thisExp.nextEntry()

# completed 1.0 repeats of 'total_loop'



# ------Prepare to start Routine "ExpEnd"-------
continueRoutine = True
# update component parameters for each repeat
bye_resp.keys = []
bye_resp.rt = []
_bye_resp_allKeys = []
# keep track of which components have finished
ExpEndComponents = [byebye, bye_resp]
for thisComponent in ExpEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExpEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ExpEnd"-------
while continueRoutine:
    # get current time
    t = ExpEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExpEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *byebye* updates
    if byebye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        byebye.frameNStart = frameN  # exact frame index
        byebye.tStart = t  # local t and not account for scr refresh
        byebye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(byebye, 'tStartRefresh')  # time at next scr refresh
        byebye.setAutoDraw(True)

    # *bye_resp* updates
    waitOnFlip = False
    if bye_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bye_resp.frameNStart = frameN  # exact frame index
        bye_resp.tStart = t  # local t and not account for scr refresh
        bye_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bye_resp, 'tStartRefresh')  # time at next scr refresh
        bye_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(bye_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(bye_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if bye_resp.status == STARTED and not waitOnFlip:
        theseKeys = bye_resp.getKeys(keyList=None, waitRelease=False)
        _bye_resp_allKeys.extend(theseKeys)
        if len(_bye_resp_allKeys):
            bye_resp.keys = _bye_resp_allKeys[-1].name  # just the last key pressed
            bye_resp.rt = _bye_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExpEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ExpEnd"-------
for thisComponent in ExpEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('byebye.started', byebye.tStartRefresh)
thisExp.addData('byebye.stopped', byebye.tStopRefresh)
# check responses
if bye_resp.keys in ['', [], None]:  # No response was made
    bye_resp.keys = None
thisExp.addData('bye_resp.keys',bye_resp.keys)
if bye_resp.keys != None:  # we had a response
    thisExp.addData('bye_resp.rt', bye_resp.rt)
thisExp.addData('bye_resp.started', bye_resp.tStartRefresh)
thisExp.addData('bye_resp.stopped', bye_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "ExpEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
