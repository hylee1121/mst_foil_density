#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on Tue Jul  5 15:42:46 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'sub'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expName, expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/hlee/Documents/foilmemoryexp/mnemonicproj.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Hello, thanks for your participation.\n\n\n\nThis experiment consists of a total of FOUR blocks.\n\nIn each block, you see 24 objects, play a simple Sudoku game, \nand do a memory test.\n\nPlease try to remember the objects as much as possible.\n\n\n\nPress “M” to move on to the next screen.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp = keyboard.Keyboard()

# Initialize components for Routine "ready_block"
ready_blockClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Now, you will see 24 objects for 2 seconds each.\n\nPlease try to remember as much as possible.\n\n\n\nWhen you are ready, press “R” button.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "fixationcross"
fixationcrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "ecd_trial"
ecd_trialClock = core.Clock()
ecd_img = visual.ImageStim(
    win=win,
    name='ecd_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "sudoku_intro"
sudoku_introClock = core.Clock()
before_sudoku = visual.TextStim(win=win, name='before_sudoku',
    text='Now, you will play Sudoku for 5 minutes.\n\nPlease bring a paper and pen on the left side of the monitor in front of you.\n\n\n\nIf you don’t know how to play Sudoku, refer to the paper on the right side of the monitor.\n\nPlease do your best!\n\nYour play results will be analyzed.\n\n\n\nWhen you are ready, press “R” button.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_mk = keyboard.Keyboard()

# Initialize components for Routine "sudoku_timer"
sudoku_timerClock = core.Clock()
text_timer = visual.TextStim(win=win, name='text_timer',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "recog_intro"
recog_introClock = core.Clock()
intro_recogtest = visual.TextStim(win=win, name='intro_recogtest',
    text="Now, you are going to do a memory test.\n\nIf the object that appears is what you saw (old), press H.\n\nIf the object that appears is similar to what you saw (similar), press J.\n\nIf the object that appears is not what you saw (new), press K.\n\n\n\nThen, rate how confident you are about your answer.\n\nH = very uncertain, \n\nJ = somewhat uncertain, \n\nK = somewhat certain\n\nL = very certain\n\n\n\nAll responses have a 2s timeout. \n\nDon't lose your concentration and respond in time.\n\n\n\nWhen you are ready to test, press A to start.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_recog = keyboard.Keyboard()

# Initialize components for Routine "fixationcross"
fixationcrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "rcg_trial"
rcg_trialClock = core.Clock()
image_stim_rcg = visual.ImageStim(
    win=win,
    name='image_stim_rcg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_rcg = keyboard.Keyboard()
rcg_q = visual.TextStim(win=win, name='rcg_q',
    text='Please answer your status for the picture below.',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
rcg_a = visual.TextStim(win=win, name='rcg_a',
    text='H = old,   J = similar,   K = new',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "confidence"
confidenceClock = core.Clock()
confidenceQ = visual.TextStim(win=win, name='confidenceQ',
    text='Please rate your confidence in your answer.',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ratebar = visual.ImageStim(
    win=win,
    name='ratebar', 
    image='ratebar.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(1.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_conf = keyboard.Keyboard()

# Initialize components for Routine "ExpEnd"
ExpEndClock = core.Clock()
byebye = visual.TextStim(win=win, name='byebye',
    text='Thank you for your participation.\nPlease enter any key to exit this screen.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bye_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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

# set up handler to look after randomisation of conditions etc
total_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ecdrcg_list.xlsx'),
    seed=None, name='total_loop')
thisExp.addLoop(total_loop)  # add the loop to the experiment
thisTotal_loop = total_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTotal_loop.rgb)
if thisTotal_loop != None:
    for paramName in thisTotal_loop:
        exec('{} = thisTotal_loop[paramName]'.format(paramName))

for thisTotal_loop in total_loop:
    currentLoop = total_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTotal_loop.rgb)
    if thisTotal_loop != None:
        for paramName in thisTotal_loop:
            exec('{} = thisTotal_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ready_block"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ready_blockComponents = [text, key_resp]
    for thisComponent in ready_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ready_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ready_block"-------
    while continueRoutine:
        # get current time
        t = ready_blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ready_blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['r'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready_block"-------
    for thisComponent in ready_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    total_loop.addData('text.started', text.tStartRefresh)
    total_loop.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    total_loop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        total_loop.addData('key_resp.rt', key_resp.rt)
    total_loop.addData('key_resp.started', key_resp.tStartRefresh)
    total_loop.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "ready_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ecd_block = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(ecd_list),
        seed=None, name='ecd_block')
    thisExp.addLoop(ecd_block)  # add the loop to the experiment
    thisEcd_block = ecd_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEcd_block.rgb)
    if thisEcd_block != None:
        for paramName in thisEcd_block:
            exec('{} = thisEcd_block[paramName]'.format(paramName))
    
    for thisEcd_block in ecd_block:
        currentLoop = ecd_block
        # abbreviate parameter names if possible (e.g. rgb = thisEcd_block.rgb)
        if thisEcd_block != None:
            for paramName in thisEcd_block:
                exec('{} = thisEcd_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixationcross"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationcrossComponents = [polygon]
        for thisComponent in fixationcrossComponents:
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
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationcrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixationcross"-------
        for thisComponent in fixationcrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ecd_block.addData('polygon.started', polygon.tStartRefresh)
        ecd_block.addData('polygon.stopped', polygon.tStopRefresh)
        
        # ------Prepare to start Routine "ecd_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        ecd_img.setImage(ecd_image)
        # keep track of which components have finished
        ecd_trialComponents = [ecd_img]
        for thisComponent in ecd_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ecd_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ecd_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ecd_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ecd_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ecd_img* updates
            if ecd_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ecd_img.frameNStart = frameN  # exact frame index
                ecd_img.tStart = t  # local t and not account for scr refresh
                ecd_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ecd_img, 'tStartRefresh')  # time at next scr refresh
                ecd_img.setAutoDraw(True)
            if ecd_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ecd_img.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ecd_img.tStop = t  # not accounting for scr refresh
                    ecd_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ecd_img, 'tStopRefresh')  # time at next scr refresh
                    ecd_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ecd_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ecd_trial"-------
        for thisComponent in ecd_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ecd_block.addData('ecd_img.started', ecd_img.tStartRefresh)
        ecd_block.addData('ecd_img.stopped', ecd_img.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'ecd_block'
    
    
    # ------Prepare to start Routine "sudoku_intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_mk.keys = []
    key_resp_mk.rt = []
    _key_resp_mk_allKeys = []
    # keep track of which components have finished
    sudoku_introComponents = [before_sudoku, key_resp_mk]
    for thisComponent in sudoku_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sudoku_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sudoku_intro"-------
    while continueRoutine:
        # get current time
        t = sudoku_introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sudoku_introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *before_sudoku* updates
        if before_sudoku.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            before_sudoku.frameNStart = frameN  # exact frame index
            before_sudoku.tStart = t  # local t and not account for scr refresh
            before_sudoku.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(before_sudoku, 'tStartRefresh')  # time at next scr refresh
            before_sudoku.setAutoDraw(True)
        
        # *key_resp_mk* updates
        waitOnFlip = False
        if key_resp_mk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_mk.frameNStart = frameN  # exact frame index
            key_resp_mk.tStart = t  # local t and not account for scr refresh
            key_resp_mk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_mk, 'tStartRefresh')  # time at next scr refresh
            key_resp_mk.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_mk.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_mk.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_mk.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_mk.getKeys(keyList=['r'], waitRelease=False)
            _key_resp_mk_allKeys.extend(theseKeys)
            if len(_key_resp_mk_allKeys):
                key_resp_mk.keys = _key_resp_mk_allKeys[-1].name  # just the last key pressed
                key_resp_mk.rt = _key_resp_mk_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sudoku_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sudoku_intro"-------
    for thisComponent in sudoku_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    total_loop.addData('before_sudoku.started', before_sudoku.tStartRefresh)
    total_loop.addData('before_sudoku.stopped', before_sudoku.tStopRefresh)
    # check responses
    if key_resp_mk.keys in ['', [], None]:  # No response was made
        key_resp_mk.keys = None
    total_loop.addData('key_resp_mk.keys',key_resp_mk.keys)
    if key_resp_mk.keys != None:  # we had a response
        total_loop.addData('key_resp_mk.rt', key_resp_mk.rt)
    total_loop.addData('key_resp_mk.started', key_resp_mk.tStartRefresh)
    total_loop.addData('key_resp_mk.stopped', key_resp_mk.tStopRefresh)
    # the Routine "sudoku_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sudoku_timer"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    sudoku_timer = core.CountdownTimer(5)
    # keep track of which components have finished
    sudoku_timerComponents = [text_timer]
    for thisComponent in sudoku_timerComponents:
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
        if text_timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_timer.frameNStart = frameN  # exact frame index
            text_timer.tStart = t  # local t and not account for scr refresh
            text_timer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_timer, 'tStartRefresh')  # time at next scr refresh
            text_timer.setAutoDraw(True)
        if text_timer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_timer.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text_timer.tStop = t  # not accounting for scr refresh
                text_timer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_timer, 'tStopRefresh')  # time at next scr refresh
                text_timer.setAutoDraw(False)
        if text_timer.status == STARTED:  # only update if drawing
            text_timer.setText(message, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sudoku_timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sudoku_timer"-------
    for thisComponent in sudoku_timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    total_loop.addData('text_timer.started', text_timer.tStartRefresh)
    total_loop.addData('text_timer.stopped', text_timer.tStopRefresh)
    
    # ------Prepare to start Routine "recog_intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_recog.keys = []
    key_resp_recog.rt = []
    _key_resp_recog_allKeys = []
    # keep track of which components have finished
    recog_introComponents = [intro_recogtest, key_resp_recog]
    for thisComponent in recog_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recog_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "recog_intro"-------
    while continueRoutine:
        # get current time
        t = recog_introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recog_introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_recogtest* updates
        if intro_recogtest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_recogtest.frameNStart = frameN  # exact frame index
            intro_recogtest.tStart = t  # local t and not account for scr refresh
            intro_recogtest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_recogtest, 'tStartRefresh')  # time at next scr refresh
            intro_recogtest.setAutoDraw(True)
        
        # *key_resp_recog* updates
        waitOnFlip = False
        if key_resp_recog.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_recog.frameNStart = frameN  # exact frame index
            key_resp_recog.tStart = t  # local t and not account for scr refresh
            key_resp_recog.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_recog, 'tStartRefresh')  # time at next scr refresh
            key_resp_recog.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_recog.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_recog.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_recog.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_recog.getKeys(keyList=['a'], waitRelease=False)
            _key_resp_recog_allKeys.extend(theseKeys)
            if len(_key_resp_recog_allKeys):
                key_resp_recog.keys = _key_resp_recog_allKeys[-1].name  # just the last key pressed
                key_resp_recog.rt = _key_resp_recog_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recog_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recog_intro"-------
    for thisComponent in recog_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    total_loop.addData('intro_recogtest.started', intro_recogtest.tStartRefresh)
    total_loop.addData('intro_recogtest.stopped', intro_recogtest.tStopRefresh)
    # check responses
    if key_resp_recog.keys in ['', [], None]:  # No response was made
        key_resp_recog.keys = None
    total_loop.addData('key_resp_recog.keys',key_resp_recog.keys)
    if key_resp_recog.keys != None:  # we had a response
        total_loop.addData('key_resp_recog.rt', key_resp_recog.rt)
    total_loop.addData('key_resp_recog.started', key_resp_recog.tStartRefresh)
    total_loop.addData('key_resp_recog.stopped', key_resp_recog.tStopRefresh)
    # the Routine "recog_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    rcg_block = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(rcg_list),
        seed=None, name='rcg_block')
    thisExp.addLoop(rcg_block)  # add the loop to the experiment
    thisRcg_block = rcg_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRcg_block.rgb)
    if thisRcg_block != None:
        for paramName in thisRcg_block:
            exec('{} = thisRcg_block[paramName]'.format(paramName))
    
    for thisRcg_block in rcg_block:
        currentLoop = rcg_block
        # abbreviate parameter names if possible (e.g. rgb = thisRcg_block.rgb)
        if thisRcg_block != None:
            for paramName in thisRcg_block:
                exec('{} = thisRcg_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixationcross"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationcrossComponents = [polygon]
        for thisComponent in fixationcrossComponents:
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
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationcrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixationcross"-------
        for thisComponent in fixationcrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rcg_block.addData('polygon.started', polygon.tStartRefresh)
        rcg_block.addData('polygon.stopped', polygon.tStopRefresh)
        
        # ------Prepare to start Routine "rcg_trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_stim_rcg.setImage(rcg_image)
        key_resp_rcg.keys = []
        key_resp_rcg.rt = []
        _key_resp_rcg_allKeys = []
        # keep track of which components have finished
        rcg_trialComponents = [image_stim_rcg, key_resp_rcg, rcg_q, rcg_a]
        for thisComponent in rcg_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rcg_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rcg_trial"-------
        while continueRoutine:
            # get current time
            t = rcg_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rcg_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_stim_rcg* updates
            if image_stim_rcg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_stim_rcg.frameNStart = frameN  # exact frame index
                image_stim_rcg.tStart = t  # local t and not account for scr refresh
                image_stim_rcg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_stim_rcg, 'tStartRefresh')  # time at next scr refresh
                image_stim_rcg.setAutoDraw(True)
            
            # *key_resp_rcg* updates
            waitOnFlip = False
            if key_resp_rcg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_rcg.frameNStart = frameN  # exact frame index
                key_resp_rcg.tStart = t  # local t and not account for scr refresh
                key_resp_rcg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_rcg, 'tStartRefresh')  # time at next scr refresh
                key_resp_rcg.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_rcg.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_rcg.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_rcg.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_rcg.getKeys(keyList=['h','j','k'], waitRelease=False)
                _key_resp_rcg_allKeys.extend(theseKeys)
                if len(_key_resp_rcg_allKeys):
                    key_resp_rcg.keys = _key_resp_rcg_allKeys[-1].name  # just the last key pressed
                    key_resp_rcg.rt = _key_resp_rcg_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_rcg.keys == str(cresp)) or (key_resp_rcg.keys == cresp):
                        key_resp_rcg.corr = 1
                    else:
                        key_resp_rcg.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *rcg_q* updates
            if rcg_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rcg_q.frameNStart = frameN  # exact frame index
                rcg_q.tStart = t  # local t and not account for scr refresh
                rcg_q.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rcg_q, 'tStartRefresh')  # time at next scr refresh
                rcg_q.setAutoDraw(True)
            
            # *rcg_a* updates
            if rcg_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rcg_a.frameNStart = frameN  # exact frame index
                rcg_a.tStart = t  # local t and not account for scr refresh
                rcg_a.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rcg_a, 'tStartRefresh')  # time at next scr refresh
                rcg_a.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rcg_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rcg_trial"-------
        for thisComponent in rcg_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rcg_block.addData('image_stim_rcg.started', image_stim_rcg.tStartRefresh)
        rcg_block.addData('image_stim_rcg.stopped', image_stim_rcg.tStopRefresh)
        # check responses
        if key_resp_rcg.keys in ['', [], None]:  # No response was made
            key_resp_rcg.keys = None
            # was no response the correct answer?!
            if str(cresp).lower() == 'none':
               key_resp_rcg.corr = 1;  # correct non-response
            else:
               key_resp_rcg.corr = 0;  # failed to respond (incorrectly)
        # store data for rcg_block (TrialHandler)
        rcg_block.addData('key_resp_rcg.keys',key_resp_rcg.keys)
        rcg_block.addData('key_resp_rcg.corr', key_resp_rcg.corr)
        if key_resp_rcg.keys != None:  # we had a response
            rcg_block.addData('key_resp_rcg.rt', key_resp_rcg.rt)
        rcg_block.addData('key_resp_rcg.started', key_resp_rcg.tStartRefresh)
        rcg_block.addData('key_resp_rcg.stopped', key_resp_rcg.tStopRefresh)
        rcg_block.addData('rcg_q.started', rcg_q.tStartRefresh)
        rcg_block.addData('rcg_q.stopped', rcg_q.tStopRefresh)
        rcg_block.addData('rcg_a.started', rcg_a.tStartRefresh)
        rcg_block.addData('rcg_a.stopped', rcg_a.tStopRefresh)
        # the Routine "rcg_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "confidence"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        key_resp_conf.keys = []
        key_resp_conf.rt = []
        _key_resp_conf_allKeys = []
        # keep track of which components have finished
        confidenceComponents = [confidenceQ, ratebar, key_resp_conf]
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
        confidenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "confidence"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = confidenceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=confidenceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *confidenceQ* updates
            if confidenceQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidenceQ.frameNStart = frameN  # exact frame index
                confidenceQ.tStart = t  # local t and not account for scr refresh
                confidenceQ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidenceQ, 'tStartRefresh')  # time at next scr refresh
                confidenceQ.setAutoDraw(True)
            if confidenceQ.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > confidenceQ.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    confidenceQ.tStop = t  # not accounting for scr refresh
                    confidenceQ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(confidenceQ, 'tStopRefresh')  # time at next scr refresh
                    confidenceQ.setAutoDraw(False)
            
            # *ratebar* updates
            if ratebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratebar.frameNStart = frameN  # exact frame index
                ratebar.tStart = t  # local t and not account for scr refresh
                ratebar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratebar, 'tStartRefresh')  # time at next scr refresh
                ratebar.setAutoDraw(True)
            if ratebar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ratebar.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ratebar.tStop = t  # not accounting for scr refresh
                    ratebar.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratebar, 'tStopRefresh')  # time at next scr refresh
                    ratebar.setAutoDraw(False)
            
            # *key_resp_conf* updates
            waitOnFlip = False
            if key_resp_conf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_conf.frameNStart = frameN  # exact frame index
                key_resp_conf.tStart = t  # local t and not account for scr refresh
                key_resp_conf.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_conf, 'tStartRefresh')  # time at next scr refresh
                key_resp_conf.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_conf.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_conf.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_conf.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_conf.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_conf.tStop = t  # not accounting for scr refresh
                    key_resp_conf.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_conf, 'tStopRefresh')  # time at next scr refresh
                    key_resp_conf.status = FINISHED
            if key_resp_conf.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_conf.getKeys(keyList=['h','j','k','l'], waitRelease=False)
                _key_resp_conf_allKeys.extend(theseKeys)
                if len(_key_resp_conf_allKeys):
                    key_resp_conf.keys = _key_resp_conf_allKeys[-1].name  # just the last key pressed
                    key_resp_conf.rt = _key_resp_conf_allKeys[-1].rt
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
        rcg_block.addData('confidenceQ.started', confidenceQ.tStartRefresh)
        rcg_block.addData('confidenceQ.stopped', confidenceQ.tStopRefresh)
        rcg_block.addData('ratebar.started', ratebar.tStartRefresh)
        rcg_block.addData('ratebar.stopped', ratebar.tStopRefresh)
        # check responses
        if key_resp_conf.keys in ['', [], None]:  # No response was made
            key_resp_conf.keys = None
        rcg_block.addData('key_resp_conf.keys',key_resp_conf.keys)
        if key_resp_conf.keys != None:  # we had a response
            rcg_block.addData('key_resp_conf.rt', key_resp_conf.rt)
        rcg_block.addData('key_resp_conf.started', key_resp_conf.tStartRefresh)
        rcg_block.addData('key_resp_conf.stopped', key_resp_conf.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'rcg_block'
    
    thisExp.nextEntry()
    
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
