#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 23, 2020, at 16:01
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'vSearchAlpha'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\v-search-alpha\\vSearchAlpha_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='In this task you will see sets of shapes made of four different shapes as outlined below. Only press space if you see the “T” shape, which is the last shape. Otherwise, do not respond. Press space to continue.',
    font='Arial',
    pos=[0,0.15], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp1 = keyboard.Keyboard()
l11ex = visual.ImageStim(
    win=win,
    name='l11ex', 
    image='L11.png', mask=None,
    ori=0, pos=(-0.3, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
l21ex = visual.ImageStim(
    win=win,
    name='l21ex', 
    image='L21.png', mask=None,
    ori=0, pos=(-0.1, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
t11ex = visual.ImageStim(
    win=win,
    name='t11ex', 
    image='T11.png', mask=None,
    ori=0, pos=(0.1, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tTex = visual.ImageStim(
    win=win,
    name='tTex', 
    image='TT.png', mask=None,
    ori=0, pos=(0.3, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
trial1Fix = visual.TextStim(win=win, name='trial1Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial1L11 = visual.ImageStim(
    win=win,
    name='trial1L11', 
    image='L11.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial1L12 = visual.ImageStim(
    win=win,
    name='trial1L12', 
    image='L12.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial1L21 = visual.ImageStim(
    win=win,
    name='trial1L21', 
    image='L21.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial1L22 = visual.ImageStim(
    win=win,
    name='trial1L22', 
    image='L22.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial1T11 = visual.ImageStim(
    win=win,
    name='trial1T11', 
    image='T11.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trial1T12 = visual.ImageStim(
    win=win,
    name='trial1T12', 
    image='T12.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trial1TT = visual.ImageStim(
    win=win,
    name='trial1TT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trial1Resp = keyboard.Keyboard()

# Initialize components for Routine "breakTime"
breakTimeClock = core.Clock()
breakTimeText = visual.TextStim(win=win, name='breakTimeText',
    text='A quick break before the next set of trials.\nPress space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
breakBreak = keyboard.Keyboard()

# Initialize components for Routine "fixation2"
fixation2Clock = core.Clock()
fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
trial2Fix = visual.TextStim(win=win, name='trial2Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial2L11 = visual.ImageStim(
    win=win,
    name='trial2L11', 
    image='L11.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial2L12 = visual.ImageStim(
    win=win,
    name='trial2L12', 
    image='L12.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial2L21 = visual.ImageStim(
    win=win,
    name='trial2L21', 
    image='L21.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial2L22 = visual.ImageStim(
    win=win,
    name='trial2L22', 
    image='L22.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial2T11 = visual.ImageStim(
    win=win,
    name='trial2T11', 
    image='T11.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trial2T12 = visual.ImageStim(
    win=win,
    name='trial2T12', 
    image='T12.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trial2TT = visual.ImageStim(
    win=win,
    name='trial2TT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trial2Resp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='This is the end of the experiment.\nThank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction1"-------
continueRoutine = True
# update component parameters for each repeat
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
instruction1Components = [instr1, keyResp1, l11ex, l21ex, t11ex, tTex]
for thisComponent in instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction1"-------
while continueRoutine:
    # get current time
    t = instruction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['space'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *l11ex* updates
    if l11ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l11ex.frameNStart = frameN  # exact frame index
        l11ex.tStart = t  # local t and not account for scr refresh
        l11ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l11ex, 'tStartRefresh')  # time at next scr refresh
        l11ex.setAutoDraw(True)
    
    # *l21ex* updates
    if l21ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l21ex.frameNStart = frameN  # exact frame index
        l21ex.tStart = t  # local t and not account for scr refresh
        l21ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l21ex, 'tStartRefresh')  # time at next scr refresh
        l21ex.setAutoDraw(True)
    
    # *t11ex* updates
    if t11ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        t11ex.frameNStart = frameN  # exact frame index
        t11ex.tStart = t  # local t and not account for scr refresh
        t11ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(t11ex, 'tStartRefresh')  # time at next scr refresh
        t11ex.setAutoDraw(True)
    
    # *tTex* updates
    if tTex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tTex.frameNStart = frameN  # exact frame index
        tTex.tStart = t  # local t and not account for scr refresh
        tTex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tTex, 'tStartRefresh')  # time at next scr refresh
        tTex.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction1"-------
for thisComponent in instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if keyResp1.keys in ['', [], None]:  # No response was made
    keyResp1.keys = None
thisExp.addData('keyResp1.keys',keyResp1.keys)
if keyResp1.keys != None:  # we had a response
    thisExp.addData('keyResp1.rt', keyResp1.rt)
thisExp.addData('keyResp1.started', keyResp1.tStartRefresh)
thisExp.addData('keyResp1.stopped', keyResp1.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('l11ex.started', l11ex.tStartRefresh)
thisExp.addData('l11ex.stopped', l11ex.tStopRefresh)
thisExp.addData('l21ex.started', l21ex.tStartRefresh)
thisExp.addData('l21ex.stopped', l21ex.tStopRefresh)
thisExp.addData('t11ex.started', t11ex.tStartRefresh)
thisExp.addData('t11ex.stopped', t11ex.tStopRefresh)
thisExp.addData('tTex.started', tTex.tStartRefresh)
thisExp.addData('tTex.stopped', tTex.tStopRefresh)
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [fix1]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation1"-------
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchAlpha1.xlsx'),
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1:
        exec('{} = thisTrials1[paramName]'.format(paramName))

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    trial1L11.setPos([loc1,loc2])
    trial1L12.setPos([loc3,loc4])
    trial1L21.setPos([loc5,loc6])
    trial1L22.setPos([loc7,loc8])
    trial1T11.setPos([loc9,loc10])
    trial1T12.setPos([loc11,loc12])
    trial1TT.setPos([loc13,loc14])
    trial1Resp.keys = []
    trial1Resp.rt = []
    _trial1Resp_allKeys = []
    # keep track of which components have finished
    trial1Components = [trial1Fix, trial1L11, trial1L12, trial1L21, trial1L22, trial1T11, trial1T12, trial1TT, trial1Resp]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial1Fix* updates
        if trial1Fix.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Fix.frameNStart = frameN  # exact frame index
            trial1Fix.tStart = t  # local t and not account for scr refresh
            trial1Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Fix, 'tStartRefresh')  # time at next scr refresh
            trial1Fix.setAutoDraw(True)
        if trial1Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1Fix.tStop = t  # not accounting for scr refresh
                trial1Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1Fix, 'tStopRefresh')  # time at next scr refresh
                trial1Fix.setAutoDraw(False)
        
        # *trial1L11* updates
        if trial1L11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L11.frameNStart = frameN  # exact frame index
            trial1L11.tStart = t  # local t and not account for scr refresh
            trial1L11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L11, 'tStartRefresh')  # time at next scr refresh
            trial1L11.setAutoDraw(True)
        if trial1L11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1L11.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1L11.tStop = t  # not accounting for scr refresh
                trial1L11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1L11, 'tStopRefresh')  # time at next scr refresh
                trial1L11.setAutoDraw(False)
        
        # *trial1L12* updates
        if trial1L12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L12.frameNStart = frameN  # exact frame index
            trial1L12.tStart = t  # local t and not account for scr refresh
            trial1L12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L12, 'tStartRefresh')  # time at next scr refresh
            trial1L12.setAutoDraw(True)
        if trial1L12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1L12.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1L12.tStop = t  # not accounting for scr refresh
                trial1L12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1L12, 'tStopRefresh')  # time at next scr refresh
                trial1L12.setAutoDraw(False)
        
        # *trial1L21* updates
        if trial1L21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L21.frameNStart = frameN  # exact frame index
            trial1L21.tStart = t  # local t and not account for scr refresh
            trial1L21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L21, 'tStartRefresh')  # time at next scr refresh
            trial1L21.setAutoDraw(True)
        if trial1L21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1L21.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1L21.tStop = t  # not accounting for scr refresh
                trial1L21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1L21, 'tStopRefresh')  # time at next scr refresh
                trial1L21.setAutoDraw(False)
        
        # *trial1L22* updates
        if trial1L22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L22.frameNStart = frameN  # exact frame index
            trial1L22.tStart = t  # local t and not account for scr refresh
            trial1L22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L22, 'tStartRefresh')  # time at next scr refresh
            trial1L22.setAutoDraw(True)
        if trial1L22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1L22.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1L22.tStop = t  # not accounting for scr refresh
                trial1L22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1L22, 'tStopRefresh')  # time at next scr refresh
                trial1L22.setAutoDraw(False)
        
        # *trial1T11* updates
        if trial1T11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T11.frameNStart = frameN  # exact frame index
            trial1T11.tStart = t  # local t and not account for scr refresh
            trial1T11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T11, 'tStartRefresh')  # time at next scr refresh
            trial1T11.setAutoDraw(True)
        if trial1T11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1T11.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1T11.tStop = t  # not accounting for scr refresh
                trial1T11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1T11, 'tStopRefresh')  # time at next scr refresh
                trial1T11.setAutoDraw(False)
        
        # *trial1T12* updates
        if trial1T12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T12.frameNStart = frameN  # exact frame index
            trial1T12.tStart = t  # local t and not account for scr refresh
            trial1T12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T12, 'tStartRefresh')  # time at next scr refresh
            trial1T12.setAutoDraw(True)
        if trial1T12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1T12.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1T12.tStop = t  # not accounting for scr refresh
                trial1T12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1T12, 'tStopRefresh')  # time at next scr refresh
                trial1T12.setAutoDraw(False)
        
        # *trial1TT* updates
        if trial1TT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1TT.frameNStart = frameN  # exact frame index
            trial1TT.tStart = t  # local t and not account for scr refresh
            trial1TT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1TT, 'tStartRefresh')  # time at next scr refresh
            trial1TT.setAutoDraw(True)
        if trial1TT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1TT.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1TT.tStop = t  # not accounting for scr refresh
                trial1TT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1TT, 'tStopRefresh')  # time at next scr refresh
                trial1TT.setAutoDraw(False)
        
        # *trial1Resp* updates
        waitOnFlip = False
        if trial1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Resp.frameNStart = frameN  # exact frame index
            trial1Resp.tStart = t  # local t and not account for scr refresh
            trial1Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Resp, 'tStartRefresh')  # time at next scr refresh
            trial1Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial1Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial1Resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1Resp.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1Resp.tStop = t  # not accounting for scr refresh
                trial1Resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1Resp, 'tStopRefresh')  # time at next scr refresh
                trial1Resp.status = FINISHED
        if trial1Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial1Resp.getKeys(keyList=['space'], waitRelease=False)
            _trial1Resp_allKeys.extend(theseKeys)
            if len(_trial1Resp_allKeys):
                trial1Resp.keys = _trial1Resp_allKeys[-1].name  # just the last key pressed
                trial1Resp.rt = _trial1Resp_allKeys[-1].rt
                # was this correct?
                if (trial1Resp.keys == str(corrAns)) or (trial1Resp.keys == corrAns):
                    trial1Resp.corr = 1
                else:
                    trial1Resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials1.addData('trial1Fix.started', trial1Fix.tStartRefresh)
    trials1.addData('trial1Fix.stopped', trial1Fix.tStopRefresh)
    trials1.addData('trial1L11.started', trial1L11.tStartRefresh)
    trials1.addData('trial1L11.stopped', trial1L11.tStopRefresh)
    trials1.addData('trial1L12.started', trial1L12.tStartRefresh)
    trials1.addData('trial1L12.stopped', trial1L12.tStopRefresh)
    trials1.addData('trial1L21.started', trial1L21.tStartRefresh)
    trials1.addData('trial1L21.stopped', trial1L21.tStopRefresh)
    trials1.addData('trial1L22.started', trial1L22.tStartRefresh)
    trials1.addData('trial1L22.stopped', trial1L22.tStopRefresh)
    trials1.addData('trial1T11.started', trial1T11.tStartRefresh)
    trials1.addData('trial1T11.stopped', trial1T11.tStopRefresh)
    trials1.addData('trial1T12.started', trial1T12.tStartRefresh)
    trials1.addData('trial1T12.stopped', trial1T12.tStopRefresh)
    trials1.addData('trial1TT.started', trial1TT.tStartRefresh)
    trials1.addData('trial1TT.stopped', trial1TT.tStopRefresh)
    # check responses
    if trial1Resp.keys in ['', [], None]:  # No response was made
        trial1Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial1Resp.corr = 1;  # correct non-response
        else:
           trial1Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials1 (TrialHandler)
    trials1.addData('trial1Resp.keys',trial1Resp.keys)
    trials1.addData('trial1Resp.corr', trial1Resp.corr)
    if trial1Resp.keys != None:  # we had a response
        trials1.addData('trial1Resp.rt', trial1Resp.rt)
    trials1.addData('trial1Resp.started', trial1Resp.tStartRefresh)
    trials1.addData('trial1Resp.stopped', trial1Resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "breakTime"-------
continueRoutine = True
# update component parameters for each repeat
breakBreak.keys = []
breakBreak.rt = []
_breakBreak_allKeys = []
# keep track of which components have finished
breakTimeComponents = [breakTimeText, breakBreak]
for thisComponent in breakTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
breakTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "breakTime"-------
while continueRoutine:
    # get current time
    t = breakTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=breakTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breakTimeText* updates
    if breakTimeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakTimeText.frameNStart = frameN  # exact frame index
        breakTimeText.tStart = t  # local t and not account for scr refresh
        breakTimeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakTimeText, 'tStartRefresh')  # time at next scr refresh
        breakTimeText.setAutoDraw(True)
    
    # *breakBreak* updates
    waitOnFlip = False
    if breakBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakBreak.frameNStart = frameN  # exact frame index
        breakBreak.tStart = t  # local t and not account for scr refresh
        breakBreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakBreak, 'tStartRefresh')  # time at next scr refresh
        breakBreak.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(breakBreak.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(breakBreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if breakBreak.status == STARTED and not waitOnFlip:
        theseKeys = breakBreak.getKeys(keyList=['space'], waitRelease=False)
        _breakBreak_allKeys.extend(theseKeys)
        if len(_breakBreak_allKeys):
            breakBreak.keys = _breakBreak_allKeys[-1].name  # just the last key pressed
            breakBreak.rt = _breakBreak_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in breakTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "breakTime"-------
for thisComponent in breakTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('breakTimeText.started', breakTimeText.tStartRefresh)
thisExp.addData('breakTimeText.stopped', breakTimeText.tStopRefresh)
# check responses
if breakBreak.keys in ['', [], None]:  # No response was made
    breakBreak.keys = None
thisExp.addData('breakBreak.keys',breakBreak.keys)
if breakBreak.keys != None:  # we had a response
    thisExp.addData('breakBreak.rt', breakBreak.rt)
thisExp.addData('breakBreak.started', breakBreak.tStartRefresh)
thisExp.addData('breakBreak.stopped', breakBreak.tStopRefresh)
thisExp.nextEntry()
# the Routine "breakTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation2Components = [fix2]
for thisComponent in fixation2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix2* updates
    if fix2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix2.frameNStart = frameN  # exact frame index
        fix2.tStart = t  # local t and not account for scr refresh
        fix2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
        fix2.setAutoDraw(True)
    if fix2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix2.tStop = t  # not accounting for scr refresh
            fix2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
            fix2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation2"-------
for thisComponent in fixation2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix2.started', fix2.tStartRefresh)
thisExp.addData('fix2.stopped', fix2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchAlpha2.xlsx'),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    trial2L11.setPos([loc1,loc2])
    trial2L12.setPos([loc3,loc4])
    trial2L21.setPos([loc5,loc6])
    trial2L22.setPos([loc7,loc8])
    trial2T11.setPos([loc9,loc10])
    trial2T12.setPos([loc11,loc12])
    trial2TT.setPos([loc13,loc14])
    trial2Resp.keys = []
    trial2Resp.rt = []
    _trial2Resp_allKeys = []
    # keep track of which components have finished
    trial2Components = [trial2Fix, trial2L11, trial2L12, trial2L21, trial2L22, trial2T11, trial2T12, trial2TT, trial2Resp]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial2Fix* updates
        if trial2Fix.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Fix.frameNStart = frameN  # exact frame index
            trial2Fix.tStart = t  # local t and not account for scr refresh
            trial2Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Fix, 'tStartRefresh')  # time at next scr refresh
            trial2Fix.setAutoDraw(True)
        if trial2Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2Fix.tStop = t  # not accounting for scr refresh
                trial2Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2Fix, 'tStopRefresh')  # time at next scr refresh
                trial2Fix.setAutoDraw(False)
        
        # *trial2L11* updates
        if trial2L11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L11.frameNStart = frameN  # exact frame index
            trial2L11.tStart = t  # local t and not account for scr refresh
            trial2L11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L11, 'tStartRefresh')  # time at next scr refresh
            trial2L11.setAutoDraw(True)
        if trial2L11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2L11.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2L11.tStop = t  # not accounting for scr refresh
                trial2L11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2L11, 'tStopRefresh')  # time at next scr refresh
                trial2L11.setAutoDraw(False)
        
        # *trial2L12* updates
        if trial2L12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L12.frameNStart = frameN  # exact frame index
            trial2L12.tStart = t  # local t and not account for scr refresh
            trial2L12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L12, 'tStartRefresh')  # time at next scr refresh
            trial2L12.setAutoDraw(True)
        if trial2L12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2L12.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2L12.tStop = t  # not accounting for scr refresh
                trial2L12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2L12, 'tStopRefresh')  # time at next scr refresh
                trial2L12.setAutoDraw(False)
        
        # *trial2L21* updates
        if trial2L21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L21.frameNStart = frameN  # exact frame index
            trial2L21.tStart = t  # local t and not account for scr refresh
            trial2L21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L21, 'tStartRefresh')  # time at next scr refresh
            trial2L21.setAutoDraw(True)
        if trial2L21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2L21.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2L21.tStop = t  # not accounting for scr refresh
                trial2L21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2L21, 'tStopRefresh')  # time at next scr refresh
                trial2L21.setAutoDraw(False)
        
        # *trial2L22* updates
        if trial2L22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L22.frameNStart = frameN  # exact frame index
            trial2L22.tStart = t  # local t and not account for scr refresh
            trial2L22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L22, 'tStartRefresh')  # time at next scr refresh
            trial2L22.setAutoDraw(True)
        if trial2L22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2L22.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2L22.tStop = t  # not accounting for scr refresh
                trial2L22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2L22, 'tStopRefresh')  # time at next scr refresh
                trial2L22.setAutoDraw(False)
        
        # *trial2T11* updates
        if trial2T11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T11.frameNStart = frameN  # exact frame index
            trial2T11.tStart = t  # local t and not account for scr refresh
            trial2T11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T11, 'tStartRefresh')  # time at next scr refresh
            trial2T11.setAutoDraw(True)
        if trial2T11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2T11.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2T11.tStop = t  # not accounting for scr refresh
                trial2T11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2T11, 'tStopRefresh')  # time at next scr refresh
                trial2T11.setAutoDraw(False)
        
        # *trial2T12* updates
        if trial2T12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T12.frameNStart = frameN  # exact frame index
            trial2T12.tStart = t  # local t and not account for scr refresh
            trial2T12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T12, 'tStartRefresh')  # time at next scr refresh
            trial2T12.setAutoDraw(True)
        if trial2T12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2T12.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2T12.tStop = t  # not accounting for scr refresh
                trial2T12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2T12, 'tStopRefresh')  # time at next scr refresh
                trial2T12.setAutoDraw(False)
        
        # *trial2TT* updates
        if trial2TT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2TT.frameNStart = frameN  # exact frame index
            trial2TT.tStart = t  # local t and not account for scr refresh
            trial2TT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2TT, 'tStartRefresh')  # time at next scr refresh
            trial2TT.setAutoDraw(True)
        if trial2TT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2TT.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2TT.tStop = t  # not accounting for scr refresh
                trial2TT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2TT, 'tStopRefresh')  # time at next scr refresh
                trial2TT.setAutoDraw(False)
        
        # *trial2Resp* updates
        waitOnFlip = False
        if trial2Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Resp.frameNStart = frameN  # exact frame index
            trial2Resp.tStart = t  # local t and not account for scr refresh
            trial2Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Resp, 'tStartRefresh')  # time at next scr refresh
            trial2Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial2Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial2Resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2Resp.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2Resp.tStop = t  # not accounting for scr refresh
                trial2Resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2Resp, 'tStopRefresh')  # time at next scr refresh
                trial2Resp.status = FINISHED
        if trial2Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial2Resp.getKeys(keyList=['space'], waitRelease=False)
            _trial2Resp_allKeys.extend(theseKeys)
            if len(_trial2Resp_allKeys):
                trial2Resp.keys = _trial2Resp_allKeys[-1].name  # just the last key pressed
                trial2Resp.rt = _trial2Resp_allKeys[-1].rt
                # was this correct?
                if (trial2Resp.keys == str(corrAns)) or (trial2Resp.keys == corrAns):
                    trial2Resp.corr = 1
                else:
                    trial2Resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('trial2Fix.started', trial2Fix.tStartRefresh)
    trials2.addData('trial2Fix.stopped', trial2Fix.tStopRefresh)
    trials2.addData('trial2L11.started', trial2L11.tStartRefresh)
    trials2.addData('trial2L11.stopped', trial2L11.tStopRefresh)
    trials2.addData('trial2L12.started', trial2L12.tStartRefresh)
    trials2.addData('trial2L12.stopped', trial2L12.tStopRefresh)
    trials2.addData('trial2L21.started', trial2L21.tStartRefresh)
    trials2.addData('trial2L21.stopped', trial2L21.tStopRefresh)
    trials2.addData('trial2L22.started', trial2L22.tStartRefresh)
    trials2.addData('trial2L22.stopped', trial2L22.tStopRefresh)
    trials2.addData('trial2T11.started', trial2T11.tStartRefresh)
    trials2.addData('trial2T11.stopped', trial2T11.tStopRefresh)
    trials2.addData('trial2T12.started', trial2T12.tStartRefresh)
    trials2.addData('trial2T12.stopped', trial2T12.tStopRefresh)
    trials2.addData('trial2TT.started', trial2TT.tStartRefresh)
    trials2.addData('trial2TT.stopped', trial2TT.tStopRefresh)
    # check responses
    if trial2Resp.keys in ['', [], None]:  # No response was made
        trial2Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial2Resp.corr = 1;  # correct non-response
        else:
           trial2Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials2 (TrialHandler)
    trials2.addData('trial2Resp.keys',trial2Resp.keys)
    trials2.addData('trial2Resp.corr', trial2Resp.corr)
    if trial2Resp.keys != None:  # we had a response
        trials2.addData('trial2Resp.rt', trial2Resp.rt)
    trials2.addData('trial2Resp.started', trial2Resp.tStartRefresh)
    trials2.addData('trial2Resp.stopped', trial2Resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
