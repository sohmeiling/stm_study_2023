#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on March 03, 2021, at 09:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '4'
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

white = "white"
black = "black"
lightgrey = "lightgrey"

# Do not use auto-js conversion here

def createGrid(rows, cols, tiles, responseGrid=False):
    tileSize = 100 # pixels
    counter = 0
    # Starting position for grid
    xPos = 0 - ((rows * tileSize) / 2)
    yPos = 0 + ((cols * tileSize) / 2)
    
    # define tileColors
    tileColors = {
    0: None, 
    1: white, 
    2: black
}

    # Create grid
    grid = []
    for i in range(rows):
        for j in range(cols):
            tileCol = tileColors[tiles[counter]]
            counter += 1
            if tileCol is not None:
                if responseGrid == True:
                    tileCol = tileColors[1]
                grid.append(visual.Rect(
                    win=win, 
                    width=1,
                    height=1,
                    units='pix', 
                    fillColor=tileCol, 
                    size = tileSize, 
                    pos=[xPos, yPos], 
                    lineColor= black))
            xPos += tileSize
        yPos -= tileSize
        xPos = 0 - ((rows * tileSize) / 2)
    return grid

def drawGrid(grid, onOff):
    for i in grid:
        i.setAutoDraw(onOff)

# Compares tile color for two grids (g1 and g2)
def compareGrid(g1, g2):
    testCols = []
    for tile in range(len(g1)):
        if g1[tile].fillColor == g2[tile].fillColor:
            testCols.append(True)
        else:
            testCols.append(False)
    return False not in testCols


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'workingMemoryTest'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'group': ['ABC', 'ACB', 'BCA', 'BAC', 'CBA', 'CAB']}
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
    originPath='C:\\Users\\meige\\Desktop\\WorkingMemoryExpt\\workingMemoryTest_lastrun.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
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

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
welcomeTyping = visual.TextStim(win=win, name='welcomeTyping',
    text='**INSTRUCTIONS**\n\nWelcome to the typing task!\n\nIn this task, you will see a number presented on the screen. Please type in the number as quickly as you can. \n\nAfter typing the number, you will press RETURN to continue to the next number.\n\nIf you make any typing errors, you can use BACKSPACE to correct them.\n\nPlease note that you can only use the numbers on top of the keyboard.\n\nPress SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
welcomeResp = keyboard.Keyboard()

# Initialize components for Routine "warningMac"
warningMacClock = core.Clock()
text_41 = visual.TextStim(win=win, name='text_41',
    text="**ATTENTION MAC USERS**\n\nIf you are running this experiment on Safari, you will have to enable Auto-Play on this website.\n\n1) Press ESC once to access toolbar\n\n2) Click on Safari\n\n3) Go to Preferences\n\n4) Go to Websites\n\n5) Go to Auto-Play\n\n6) For pavlovia.org select 'Allow All Auto-Play' option\n\n\nPress SPACE to continue.",
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MACresp = keyboard.Keyboard()

# Initialize components for Routine "PracticeScreen_1"
PracticeScreen_1Clock = core.Clock()
PracticeInstruction = visual.TextStim(win=win, name='PracticeInstruction',
    text='We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PracticeScResp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
blankEmpty = visual.TextStim(win=win, name='blankEmpty',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TypingPrac"
TypingPracClock = core.Clock()
typeText = visual.TextStim(win=win, name='typeText',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
inputText = visual.TextStim(win=win, name='inputText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-0.498,-1.000,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
contText = visual.TextStim(win=win, name='contText',
    text='Press RETURN or ENTER to proceed. ',
    font='Arial',
    pos=(0, -0.3), height=0.035, wrapWidth=None, ori=0, 
    color=[-0.137,-0.137,-0.137], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "TypingFeedback"
TypingFeedbackClock = core.Clock()
msg = ''
rtFeedback = visual.TextStim(win=win, name='rtFeedback',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "BeginTrialScreen"
BeginTrialScreenClock = core.Clock()
beginTrialText = visual.TextStim(win=win, name='beginTrialText',
    text='You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beginResp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
blankEmpty = visual.TextStim(win=win, name='blankEmpty',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TypingPrac"
TypingPracClock = core.Clock()
typeText = visual.TextStim(win=win, name='typeText',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
inputText = visual.TextStim(win=win, name='inputText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-0.498,-1.000,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
contText = visual.TextStim(win=win, name='contText',
    text='Press RETURN or ENTER to proceed. ',
    font='Arial',
    pos=(0, -0.3), height=0.035, wrapWidth=None, ori=0, 
    color=[-0.137,-0.137,-0.137], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "BreakTime"
BreakTimeClock = core.Clock()
breakText = visual.TextStim(win=win, name='breakText',
    text='You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
breakResp = keyboard.Keyboard()

# Initialize components for Routine "MultiplyScreen"
MultiplyScreenClock = core.Clock()
practMultText = visual.TextStim(win=win, name='practMultText',
    text='**INSTRUCTIONS**\n\nWelcome to the multiplication task!\n\nIn this task, you will see a multiplication problem presented on the screen. Please type in your answer as quickly as you can. \n\nAfter typing the answer, you will press RETURN to continue to the next problem.\n\nIf you make any typing errors, you can use BACKSPACE to correct them.\n\nPlease note that you can only use the numbers on top of the keypad.\n\nPress SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
multiplyResp = keyboard.Keyboard()

# Initialize components for Routine "PracticeScreen_1"
PracticeScreen_1Clock = core.Clock()
PracticeInstruction = visual.TextStim(win=win, name='PracticeInstruction',
    text='We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PracticeScResp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
blankEmpty = visual.TextStim(win=win, name='blankEmpty',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MultiplyPrac"
MultiplyPracClock = core.Clock()
inputText2 = visual.TextStim(win=win, name='inputText2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-0.498,-1.000,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
productText = visual.TextStim(win=win, name='productText',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
contText2 = visual.TextStim(win=win, name='contText2',
    text='Press RETURN or ENTER to proceed. ',
    font='Arial',
    pos=(0, -0.3), height=0.035, wrapWidth=None, ori=0, 
    color=[-0.137,-0.137,-0.137], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "MultiplyFeedback"
MultiplyFeedbackClock = core.Clock()
message=''
mulFBText = visual.TextStim(win=win, name='mulFBText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "BeginTrialScreen"
BeginTrialScreenClock = core.Clock()
beginTrialText = visual.TextStim(win=win, name='beginTrialText',
    text='You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beginResp = keyboard.Keyboard()

# Initialize components for Routine "READY"
READYClock = core.Clock()
text_1 = visual.TextStim(win=win, name='text_1',
    text='When you are ready to start, press SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp1 = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
blankEmpty = visual.TextStim(win=win, name='blankEmpty',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MultiplyPrac"
MultiplyPracClock = core.Clock()
inputText2 = visual.TextStim(win=win, name='inputText2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-0.498,-1.000,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
productText = visual.TextStim(win=win, name='productText',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
contText2 = visual.TextStim(win=win, name='contText2',
    text='Press RETURN or ENTER to proceed. ',
    font='Arial',
    pos=(0, -0.3), height=0.035, wrapWidth=None, ori=0, 
    color=[-0.137,-0.137,-0.137], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "BreakTime"
BreakTimeClock = core.Clock()
breakText = visual.TextStim(win=win, name='breakText',
    text='You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
breakResp = keyboard.Keyboard()

# Initialize components for Routine "AdjustSoundInst"
AdjustSoundInstClock = core.Clock()
volumeText = visual.TextStim(win=win, name='volumeText',
    text='**INSTRUCTIONS**\n\nReminder, please put on your headphone/earphone now if you have not done so.\n\nBefore we start, we will need to adjust the volume of your sound input. \n\nYou will hear an audio playing when you press SPACE. Please adjust the audio to your desired volume. \n\nOnce you are done, press SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
volInstruResp = keyboard.Keyboard()

# Initialize components for Routine "AdjustSoundVol"
AdjustSoundVolClock = core.Clock()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
sampleSoundVol = sound.Sound('Audio/sample.wav', secs=-1, stereo=True, hamming=True,
    name='sampleSoundVol')
sampleSoundVol.setVolume(0.5)
sampleResp = keyboard.Keyboard()
sampleText = visual.TextStim(win=win, name='sampleText',
    text='Now, you should hear an audio playing. Please adjust your microphone/earphone volume accordingly. \n\nOnce you are done, please press SPACE to continue. [You do not have to wait till the audio finishes.]',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AuditoryScreen"
AuditoryScreenClock = core.Clock()
pracAuditoryText = visual.TextStim(win=win, name='pracAuditoryText',
    text="**INSTRUCTIONS**\n\nWelcome to the listening task!\n\nIn this task, you will hear a series of number presented to you through your earphone. Please remember the numbers in the exact order that they were presented.\n\nFollowing the presentation of audio, you will be asked to type in your response. Please key in the numbers as you hear it. For example, if you hear '3 ... 2 ... 1', key in '321.'\n\nAfter typing the answer, you will press RETURN/ENTER to continue to the next problem. If you make any typing errors, you can use BACKSPACE to correct them.\n\nIf you could not recall the series of numbers presented, take a guess, or press RETURN/ENTER to continue to the next set. When you answer correctly, the span (i.e., the number of digits to recall) increases.\n\nPress SPACE to continue. ",
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AuditoryResp = keyboard.Keyboard()

# Initialize components for Routine "PracticeScreen_1"
PracticeScreen_1Clock = core.Clock()
PracticeInstruction = visual.TextStim(win=win, name='PracticeInstruction',
    text='We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PracticeScResp = keyboard.Keyboard()

# Initialize components for Routine "Audio_Play"
Audio_PlayClock = core.Clock()
soundPresentation = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='soundPresentation')
soundPresentation.setVolume(1)
text1 = visual.TextStim(win=win, name='text1',
    text='Audio starts playing.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
crossFix1 = visual.TextStim(win=win, name='crossFix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AuditoryPracticeSet"
AuditoryPracticeSetClock = core.Clock()
inputText4 = visual.TextStim(win=win, name='inputText4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-0.498,-1.000,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
contText4 = visual.TextStim(win=win, name='contText4',
    text='Press RETURN or ENTER to proceed. ',
    font='Arial',
    pos=(0, -0.3), height=0.035, wrapWidth=None, ori=0, 
    color=[-0.137,-0.137,-0.137], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
RECALLtext2 = visual.TextStim(win=win, name='RECALLtext2',
    text='Recall',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AuditoryFeedback"
AuditoryFeedbackClock = core.Clock()
Feedback=''
AudioFBText = visual.TextStim(win=win, name='AudioFBText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "BeginTrialScreen"
BeginTrialScreenClock = core.Clock()
beginTrialText = visual.TextStim(win=win, name='beginTrialText',
    text='You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beginResp = keyboard.Keyboard()

# Initialize components for Routine "Audio_Play"
Audio_PlayClock = core.Clock()
soundPresentation = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='soundPresentation')
soundPresentation.setVolume(1)
text1 = visual.TextStim(win=win, name='text1',
    text='Audio starts playing.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
crossFix1 = visual.TextStim(win=win, name='crossFix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AuditoryTrialss"
AuditoryTrialssClock = core.Clock()
# Store responses
allResponses = []
current_resp='';
inputText3 = visual.TextStim(win=win, name='inputText3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-0.498,-1.000,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
contText3 = visual.TextStim(win=win, name='contText3',
    text='Press RETURN or ENTER to proceed. ',
    font='Arial',
    pos=(0, -0.3), height=0.035, wrapWidth=None, ori=0, 
    color=[-0.137,-0.137,-0.137], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
RECALLtext = visual.TextStim(win=win, name='RECALLtext',
    text='Recall',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
audioResp = keyboard.Keyboard()

# Initialize components for Routine "BreakTime"
BreakTimeClock = core.Clock()
breakText = visual.TextStim(win=win, name='breakText',
    text='You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
breakResp = keyboard.Keyboard()

# Initialize components for Routine "vptScreen"
vptScreenClock = core.Clock()
vptInstruct = visual.TextStim(win=win, name='vptInstruct',
    text='**INSTRUCTIONS**\n\nWelcome to the memory task!\n\nIn this task, you will see a checkerboard-like grid, with the squares in the grid each randomly colored (in either white or black colors). Please remember the patterns presented.\n\nFollowing the presentation of patterns, you are then shown a blank grid and must reproduce the pattern. You can click on the square to change its color. If you make any clicking errors, you can just click the square again to correct them.\n\nAfter you are done, you will click on the CONTINUE button to continue to the next problem. \n\nIf you could not recall the patterns presented, take a guess, or press CONTINUE to continue to the next set. The difficulty of the set increases with each correct answer.\n\nPress SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
vptResp = keyboard.Keyboard()

# Initialize components for Routine "PracticeScreen_1"
PracticeScreen_1Clock = core.Clock()
PracticeInstruction = visual.TextStim(win=win, name='PracticeInstruction',
    text='We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PracticeScResp = keyboard.Keyboard()

# Initialize components for Routine "patternGrid"
patternGridClock = core.Clock()
staticText = visual.TextStim(win=win, name='staticText',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank1000"
Blank1000Clock = core.Clock()
blankText = visual.TextStim(win=win, name='blankText',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "respGridPrac"
respGridPracClock = core.Clock()
respMousePrac = event.Mouse(win=win)
x, y = [None, None]
respMousePrac.mouseClock = core.Clock()
imagePrac = visual.ImageStim(
    win=win,
    name='imagePrac', 
    image='continueButton.png', mask=None,
    ori=0, pos=[0, -0.35], size=[0.35, 0.08],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "vptFeedback"
vptFeedbackClock = core.Clock()
vptTEXT = visual.TextStim(win=win, name='vptTEXT',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "BeginTrialScreen"
BeginTrialScreenClock = core.Clock()
beginTrialText = visual.TextStim(win=win, name='beginTrialText',
    text='You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beginResp = keyboard.Keyboard()

# Initialize components for Routine "counterRoutine"
counterRoutineClock = core.Clock()
readyText = visual.TextStim(win=win, name='readyText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "patternGrid"
patternGridClock = core.Clock()
staticText = visual.TextStim(win=win, name='staticText',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank1000"
Blank1000Clock = core.Clock()
blankText = visual.TextStim(win=win, name='blankText',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "responseGrid"
responseGridClock = core.Clock()
respMouse = event.Mouse(win=win)
x, y = [None, None]
respMouse.mouseClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='continueButton.png', mask=None,
    ori=0, pos=[0, -0.35], size=[0.35, 0.08],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "BreakTime"
BreakTimeClock = core.Clock()
breakText = visual.TextStim(win=win, name='breakText',
    text='You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
breakResp = keyboard.Keyboard()

# Initialize components for Routine "ENDING"
ENDINGClock = core.Clock()
ENDtext = visual.TextStim(win=win, name='ENDtext',
    text='This is the end of the experiment. Thank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
welcomeResp.keys = []
welcomeResp.rt = []
_welcomeResp_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [welcomeTyping, welcomeResp]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeTyping* updates
    if welcomeTyping.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeTyping.frameNStart = frameN  # exact frame index
        welcomeTyping.tStart = t  # local t and not account for scr refresh
        welcomeTyping.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeTyping, 'tStartRefresh')  # time at next scr refresh
        welcomeTyping.setAutoDraw(True)
    
    # *welcomeResp* updates
    waitOnFlip = False
    if welcomeResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeResp.frameNStart = frameN  # exact frame index
        welcomeResp.tStart = t  # local t and not account for scr refresh
        welcomeResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeResp, 'tStartRefresh')  # time at next scr refresh
        welcomeResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeResp.status == STARTED and not waitOnFlip:
        theseKeys = welcomeResp.getKeys(keyList=['o', 'space'], waitRelease=False)
        _welcomeResp_allKeys.extend(theseKeys)
        if len(_welcomeResp_allKeys):
            welcomeResp.keys = _welcomeResp_allKeys[-1].name  # just the last key pressed
            welcomeResp.rt = _welcomeResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcomeTyping.started', welcomeTyping.tStartRefresh)
thisExp.addData('welcomeTyping.stopped', welcomeTyping.tStopRefresh)
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "warningMac"-------
continueRoutine = True
# update component parameters for each repeat
MACresp.keys = []
MACresp.rt = []
_MACresp_allKeys = []
# keep track of which components have finished
warningMacComponents = [text_41, MACresp]
for thisComponent in warningMacComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
warningMacClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "warningMac"-------
while continueRoutine:
    # get current time
    t = warningMacClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=warningMacClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_41* updates
    if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_41.frameNStart = frameN  # exact frame index
        text_41.tStart = t  # local t and not account for scr refresh
        text_41.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
        text_41.setAutoDraw(True)
    
    # *MACresp* updates
    waitOnFlip = False
    if MACresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MACresp.frameNStart = frameN  # exact frame index
        MACresp.tStart = t  # local t and not account for scr refresh
        MACresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MACresp, 'tStartRefresh')  # time at next scr refresh
        MACresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(MACresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(MACresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if MACresp.status == STARTED and not waitOnFlip:
        theseKeys = MACresp.getKeys(keyList=['o', 'space'], waitRelease=False)
        _MACresp_allKeys.extend(theseKeys)
        if len(_MACresp_allKeys):
            MACresp.keys = _MACresp_allKeys[-1].name  # just the last key pressed
            MACresp.rt = _MACresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in warningMacComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "warningMac"-------
for thisComponent in warningMacComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_41.started', text_41.tStartRefresh)
thisExp.addData('text_41.stopped', text_41.tStopRefresh)
# the Routine "warningMac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracticeScreen_1"-------
continueRoutine = True
# update component parameters for each repeat
PracticeScResp.keys = []
PracticeScResp.rt = []
_PracticeScResp_allKeys = []
# keep track of which components have finished
PracticeScreen_1Components = [PracticeInstruction, PracticeScResp]
for thisComponent in PracticeScreen_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeScreen_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracticeScreen_1"-------
while continueRoutine:
    # get current time
    t = PracticeScreen_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeScreen_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PracticeInstruction* updates
    if PracticeInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PracticeInstruction.frameNStart = frameN  # exact frame index
        PracticeInstruction.tStart = t  # local t and not account for scr refresh
        PracticeInstruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PracticeInstruction, 'tStartRefresh')  # time at next scr refresh
        PracticeInstruction.setAutoDraw(True)
    
    # *PracticeScResp* updates
    waitOnFlip = False
    if PracticeScResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PracticeScResp.frameNStart = frameN  # exact frame index
        PracticeScResp.tStart = t  # local t and not account for scr refresh
        PracticeScResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PracticeScResp, 'tStartRefresh')  # time at next scr refresh
        PracticeScResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PracticeScResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PracticeScResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PracticeScResp.status == STARTED and not waitOnFlip:
        theseKeys = PracticeScResp.getKeys(keyList=['o', 'space'], waitRelease=False)
        _PracticeScResp_allKeys.extend(theseKeys)
        if len(_PracticeScResp_allKeys):
            PracticeScResp.keys = _PracticeScResp_allKeys[-1].name  # just the last key pressed
            PracticeScResp.rt = _PracticeScResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeScreen_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeScreen_1"-------
for thisComponent in PracticeScreen_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PracticeInstruction.started', PracticeInstruction.tStartRefresh)
thisExp.addData('PracticeInstruction.stopped', PracticeInstruction.tStopRefresh)
# the Routine "PracticeScreen_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
typingLoopPract = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('typingPractice.xlsx'),
    seed=None, name='typingLoopPract')
thisExp.addLoop(typingLoopPract)  # add the loop to the experiment
thisTypingLoopPract = typingLoopPract.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTypingLoopPract.rgb)
if thisTypingLoopPract != None:
    for paramName in thisTypingLoopPract:
        exec('{} = thisTypingLoopPract[paramName]'.format(paramName))

for thisTypingLoopPract in typingLoopPract:
    currentLoop = typingLoopPract
    # abbreviate parameter names if possible (e.g. rgb = thisTypingLoopPract.rgb)
    if thisTypingLoopPract != None:
        for paramName in thisTypingLoopPract:
            exec('{} = thisTypingLoopPract[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [blankEmpty]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankEmpty* updates
        if blankEmpty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blankEmpty.frameNStart = frameN  # exact frame index
            blankEmpty.tStart = t  # local t and not account for scr refresh
            blankEmpty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankEmpty, 'tStartRefresh')  # time at next scr refresh
            blankEmpty.setAutoDraw(True)
        if blankEmpty.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blankEmpty.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                blankEmpty.tStop = t  # not accounting for scr refresh
                blankEmpty.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blankEmpty, 'tStopRefresh')  # time at next scr refresh
                blankEmpty.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    typingLoopPract.addData('blankEmpty.started', blankEmpty.tStartRefresh)
    typingLoopPract.addData('blankEmpty.stopped', blankEmpty.tStopRefresh)
    
    # ------Prepare to start Routine "TypingPrac"-------
    continueRoutine = True
    # update component parameters for each repeat
    modify = False
    inputText.text = ''
    event.clearEvents('keyboard')
    t=0
    
    typeText.setText(productNo)
    # keep track of which components have finished
    TypingPracComponents = [typeText, inputText, contText]
    for thisComponent in TypingPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TypingPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TypingPrac"-------
    while continueRoutine:
        # get current time
        t = TypingPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TypingPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        keys = event.getKeys(keyList =['backspace','return','1','2','3','4','5','6','7','8','9','0'])
        if len(keys):
            if 'backspace' in keys:
                inputText.text = inputText.text[:-1]
            elif 'return' in keys:
                continueRoutine = False
                thisExp.addData("typedNumber", inputText.text)
                thisExp.addData('typingRT', t)
            else:
                if modify:
                    inputText.text = inputText.text + keys[0].upper()
                    modify = False
                else:
                    inputText.text = inputText.text + keys[0]
        
        
        
        # *typeText* updates
        if typeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            typeText.frameNStart = frameN  # exact frame index
            typeText.tStart = t  # local t and not account for scr refresh
            typeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(typeText, 'tStartRefresh')  # time at next scr refresh
            typeText.setAutoDraw(True)
        
        # *inputText* updates
        if inputText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inputText.frameNStart = frameN  # exact frame index
            inputText.tStart = t  # local t and not account for scr refresh
            inputText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inputText, 'tStartRefresh')  # time at next scr refresh
            inputText.setAutoDraw(True)
        
        # *contText* updates
        if contText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            contText.frameNStart = frameN  # exact frame index
            contText.tStart = t  # local t and not account for scr refresh
            contText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(contText, 'tStartRefresh')  # time at next scr refresh
            contText.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TypingPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TypingPrac"-------
    for thisComponent in TypingPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if int(inputText.text) ==productNo:
        # store in the data file manually:
        thisExp.addData('answerCorr', 1) # or True or 'Yes', or whatever
    else:
        thisExp.addData('answerCorr', 0)
    
    typingLoopPract.addData('typeText.started', typeText.tStartRefresh)
    typingLoopPract.addData('typeText.stopped', typeText.tStopRefresh)
    typingLoopPract.addData('inputText.started', inputText.tStartRefresh)
    typingLoopPract.addData('inputText.stopped', inputText.tStopRefresh)
    typingLoopPract.addData('contText.started', contText.tStartRefresh)
    typingLoopPract.addData('contText.stopped', contText.tStopRefresh)
    # the Routine "TypingPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TypingFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if int(inputText.text) ==productNo:
        msg='Correct!' 
    else:
        msg = 'Wrong!'
    rtFeedback.setText(msg)
    # keep track of which components have finished
    TypingFeedbackComponents = [rtFeedback]
    for thisComponent in TypingFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TypingFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TypingFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TypingFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TypingFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rtFeedback* updates
        if rtFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rtFeedback.frameNStart = frameN  # exact frame index
            rtFeedback.tStart = t  # local t and not account for scr refresh
            rtFeedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rtFeedback, 'tStartRefresh')  # time at next scr refresh
            rtFeedback.setAutoDraw(True)
        if rtFeedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rtFeedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                rtFeedback.tStop = t  # not accounting for scr refresh
                rtFeedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rtFeedback, 'tStopRefresh')  # time at next scr refresh
                rtFeedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TypingFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TypingFeedback"-------
    for thisComponent in TypingFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    typingLoopPract.addData('rtFeedback.started', rtFeedback.tStartRefresh)
    typingLoopPract.addData('rtFeedback.stopped', rtFeedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'typingLoopPract'


# ------Prepare to start Routine "BeginTrialScreen"-------
continueRoutine = True
# update component parameters for each repeat
beginResp.keys = []
beginResp.rt = []
_beginResp_allKeys = []
# keep track of which components have finished
BeginTrialScreenComponents = [beginTrialText, beginResp]
for thisComponent in BeginTrialScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginTrialScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BeginTrialScreen"-------
while continueRoutine:
    # get current time
    t = BeginTrialScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginTrialScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *beginTrialText* updates
    if beginTrialText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beginTrialText.frameNStart = frameN  # exact frame index
        beginTrialText.tStart = t  # local t and not account for scr refresh
        beginTrialText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginTrialText, 'tStartRefresh')  # time at next scr refresh
        beginTrialText.setAutoDraw(True)
    
    # *beginResp* updates
    waitOnFlip = False
    if beginResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beginResp.frameNStart = frameN  # exact frame index
        beginResp.tStart = t  # local t and not account for scr refresh
        beginResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginResp, 'tStartRefresh')  # time at next scr refresh
        beginResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(beginResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(beginResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if beginResp.status == STARTED and not waitOnFlip:
        theseKeys = beginResp.getKeys(keyList=['o', 'space'], waitRelease=False)
        _beginResp_allKeys.extend(theseKeys)
        if len(_beginResp_allKeys):
            beginResp.keys = _beginResp_allKeys[-1].name  # just the last key pressed
            beginResp.rt = _beginResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginTrialScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BeginTrialScreen"-------
for thisComponent in BeginTrialScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('beginTrialText.started', beginTrialText.tStartRefresh)
thisExp.addData('beginTrialText.stopped', beginTrialText.tStopRefresh)
# the Routine "BeginTrialScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
typingRTrial = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('typingTest_stimuli.xlsx'),
    seed=None, name='typingRTrial')
thisExp.addLoop(typingRTrial)  # add the loop to the experiment
thisTypingRTrial = typingRTrial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTypingRTrial.rgb)
if thisTypingRTrial != None:
    for paramName in thisTypingRTrial:
        exec('{} = thisTypingRTrial[paramName]'.format(paramName))

for thisTypingRTrial in typingRTrial:
    currentLoop = typingRTrial
    # abbreviate parameter names if possible (e.g. rgb = thisTypingRTrial.rgb)
    if thisTypingRTrial != None:
        for paramName in thisTypingRTrial:
            exec('{} = thisTypingRTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [blankEmpty]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankEmpty* updates
        if blankEmpty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blankEmpty.frameNStart = frameN  # exact frame index
            blankEmpty.tStart = t  # local t and not account for scr refresh
            blankEmpty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankEmpty, 'tStartRefresh')  # time at next scr refresh
            blankEmpty.setAutoDraw(True)
        if blankEmpty.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blankEmpty.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                blankEmpty.tStop = t  # not accounting for scr refresh
                blankEmpty.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blankEmpty, 'tStopRefresh')  # time at next scr refresh
                blankEmpty.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    typingRTrial.addData('blankEmpty.started', blankEmpty.tStartRefresh)
    typingRTrial.addData('blankEmpty.stopped', blankEmpty.tStopRefresh)
    
    # ------Prepare to start Routine "TypingPrac"-------
    continueRoutine = True
    # update component parameters for each repeat
    modify = False
    inputText.text = ''
    event.clearEvents('keyboard')
    t=0
    
    typeText.setText(productNo)
    # keep track of which components have finished
    TypingPracComponents = [typeText, inputText, contText]
    for thisComponent in TypingPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TypingPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TypingPrac"-------
    while continueRoutine:
        # get current time
        t = TypingPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TypingPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        keys = event.getKeys(keyList =['backspace','return','1','2','3','4','5','6','7','8','9','0'])
        if len(keys):
            if 'backspace' in keys:
                inputText.text = inputText.text[:-1]
            elif 'return' in keys:
                continueRoutine = False
                thisExp.addData("typedNumber", inputText.text)
                thisExp.addData('typingRT', t)
            else:
                if modify:
                    inputText.text = inputText.text + keys[0].upper()
                    modify = False
                else:
                    inputText.text = inputText.text + keys[0]
        
        
        
        # *typeText* updates
        if typeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            typeText.frameNStart = frameN  # exact frame index
            typeText.tStart = t  # local t and not account for scr refresh
            typeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(typeText, 'tStartRefresh')  # time at next scr refresh
            typeText.setAutoDraw(True)
        
        # *inputText* updates
        if inputText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inputText.frameNStart = frameN  # exact frame index
            inputText.tStart = t  # local t and not account for scr refresh
            inputText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inputText, 'tStartRefresh')  # time at next scr refresh
            inputText.setAutoDraw(True)
        
        # *contText* updates
        if contText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            contText.frameNStart = frameN  # exact frame index
            contText.tStart = t  # local t and not account for scr refresh
            contText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(contText, 'tStartRefresh')  # time at next scr refresh
            contText.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TypingPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TypingPrac"-------
    for thisComponent in TypingPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if int(inputText.text) ==productNo:
        # store in the data file manually:
        thisExp.addData('answerCorr', 1) # or True or 'Yes', or whatever
    else:
        thisExp.addData('answerCorr', 0)
    
    typingRTrial.addData('typeText.started', typeText.tStartRefresh)
    typingRTrial.addData('typeText.stopped', typeText.tStopRefresh)
    typingRTrial.addData('inputText.started', inputText.tStartRefresh)
    typingRTrial.addData('inputText.stopped', inputText.tStopRefresh)
    typingRTrial.addData('contText.started', contText.tStartRefresh)
    typingRTrial.addData('contText.stopped', contText.tStopRefresh)
    # the Routine "TypingPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'typingRTrial'


# ------Prepare to start Routine "BreakTime"-------
continueRoutine = True
# update component parameters for each repeat
breakResp.keys = []
breakResp.rt = []
_breakResp_allKeys = []
# keep track of which components have finished
BreakTimeComponents = [breakText, breakResp]
for thisComponent in BreakTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BreakTime"-------
while continueRoutine:
    # get current time
    t = BreakTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breakText* updates
    if breakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakText.frameNStart = frameN  # exact frame index
        breakText.tStart = t  # local t and not account for scr refresh
        breakText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
        breakText.setAutoDraw(True)
    
    # *breakResp* updates
    waitOnFlip = False
    if breakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakResp.frameNStart = frameN  # exact frame index
        breakResp.tStart = t  # local t and not account for scr refresh
        breakResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakResp, 'tStartRefresh')  # time at next scr refresh
        breakResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(breakResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(breakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if breakResp.status == STARTED and not waitOnFlip:
        theseKeys = breakResp.getKeys(keyList=['o', 'space'], waitRelease=False)
        _breakResp_allKeys.extend(theseKeys)
        if len(_breakResp_allKeys):
            breakResp.keys = _breakResp_allKeys[-1].name  # just the last key pressed
            breakResp.rt = _breakResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BreakTime"-------
for thisComponent in BreakTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('breakText.started', breakText.tStartRefresh)
thisExp.addData('breakText.stopped', breakText.tStopRefresh)
# the Routine "BreakTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TaskOrderCond = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions'+expInfo['group']+'.xlsx'),
    seed=None, name='TaskOrderCond')
thisExp.addLoop(TaskOrderCond)  # add the loop to the experiment
thisTaskOrderCond = TaskOrderCond.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTaskOrderCond.rgb)
if thisTaskOrderCond != None:
    for paramName in thisTaskOrderCond:
        exec('{} = thisTaskOrderCond[paramName]'.format(paramName))

for thisTaskOrderCond in TaskOrderCond:
    currentLoop = TaskOrderCond
    # abbreviate parameter names if possible (e.g. rgb = thisTaskOrderCond.rgb)
    if thisTaskOrderCond != None:
        for paramName in thisTaskOrderCond:
            exec('{} = thisTaskOrderCond[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    TaskA = data.TrialHandler(nReps=nRepsTask1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TaskA')
    thisExp.addLoop(TaskA)  # add the loop to the experiment
    thisTaskA = TaskA.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTaskA.rgb)
    if thisTaskA != None:
        for paramName in thisTaskA:
            exec('{} = thisTaskA[paramName]'.format(paramName))
    
    for thisTaskA in TaskA:
        currentLoop = TaskA
        # abbreviate parameter names if possible (e.g. rgb = thisTaskA.rgb)
        if thisTaskA != None:
            for paramName in thisTaskA:
                exec('{} = thisTaskA[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MultiplyScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        multiplyResp.keys = []
        multiplyResp.rt = []
        _multiplyResp_allKeys = []
        # keep track of which components have finished
        MultiplyScreenComponents = [practMultText, multiplyResp]
        for thisComponent in MultiplyScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MultiplyScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MultiplyScreen"-------
        while continueRoutine:
            # get current time
            t = MultiplyScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MultiplyScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practMultText* updates
            if practMultText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practMultText.frameNStart = frameN  # exact frame index
                practMultText.tStart = t  # local t and not account for scr refresh
                practMultText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practMultText, 'tStartRefresh')  # time at next scr refresh
                practMultText.setAutoDraw(True)
            
            # *multiplyResp* updates
            waitOnFlip = False
            if multiplyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                multiplyResp.frameNStart = frameN  # exact frame index
                multiplyResp.tStart = t  # local t and not account for scr refresh
                multiplyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(multiplyResp, 'tStartRefresh')  # time at next scr refresh
                multiplyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(multiplyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(multiplyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if multiplyResp.status == STARTED and not waitOnFlip:
                theseKeys = multiplyResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _multiplyResp_allKeys.extend(theseKeys)
                if len(_multiplyResp_allKeys):
                    multiplyResp.keys = _multiplyResp_allKeys[-1].name  # just the last key pressed
                    multiplyResp.rt = _multiplyResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MultiplyScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MultiplyScreen"-------
        for thisComponent in MultiplyScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskA.addData('practMultText.started', practMultText.tStartRefresh)
        TaskA.addData('practMultText.stopped', practMultText.tStopRefresh)
        # the Routine "MultiplyScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "PracticeScreen_1"-------
        continueRoutine = True
        # update component parameters for each repeat
        PracticeScResp.keys = []
        PracticeScResp.rt = []
        _PracticeScResp_allKeys = []
        # keep track of which components have finished
        PracticeScreen_1Components = [PracticeInstruction, PracticeScResp]
        for thisComponent in PracticeScreen_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeScreen_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeScreen_1"-------
        while continueRoutine:
            # get current time
            t = PracticeScreen_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeScreen_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PracticeInstruction* updates
            if PracticeInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeInstruction.frameNStart = frameN  # exact frame index
                PracticeInstruction.tStart = t  # local t and not account for scr refresh
                PracticeInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeInstruction, 'tStartRefresh')  # time at next scr refresh
                PracticeInstruction.setAutoDraw(True)
            
            # *PracticeScResp* updates
            waitOnFlip = False
            if PracticeScResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeScResp.frameNStart = frameN  # exact frame index
                PracticeScResp.tStart = t  # local t and not account for scr refresh
                PracticeScResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeScResp, 'tStartRefresh')  # time at next scr refresh
                PracticeScResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracticeScResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracticeScResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracticeScResp.status == STARTED and not waitOnFlip:
                theseKeys = PracticeScResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _PracticeScResp_allKeys.extend(theseKeys)
                if len(_PracticeScResp_allKeys):
                    PracticeScResp.keys = _PracticeScResp_allKeys[-1].name  # just the last key pressed
                    PracticeScResp.rt = _PracticeScResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeScreen_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeScreen_1"-------
        for thisComponent in PracticeScreen_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskA.addData('PracticeInstruction.started', PracticeInstruction.tStartRefresh)
        TaskA.addData('PracticeInstruction.stopped', PracticeInstruction.tStopRefresh)
        # the Routine "PracticeScreen_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        multiLoopPrac = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('multiplicationPract.xlsx'),
            seed=None, name='multiLoopPrac')
        thisExp.addLoop(multiLoopPrac)  # add the loop to the experiment
        thisMultiLoopPrac = multiLoopPrac.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMultiLoopPrac.rgb)
        if thisMultiLoopPrac != None:
            for paramName in thisMultiLoopPrac:
                exec('{} = thisMultiLoopPrac[paramName]'.format(paramName))
        
        for thisMultiLoopPrac in multiLoopPrac:
            currentLoop = multiLoopPrac
            # abbreviate parameter names if possible (e.g. rgb = thisMultiLoopPrac.rgb)
            if thisMultiLoopPrac != None:
                for paramName in thisMultiLoopPrac:
                    exec('{} = thisMultiLoopPrac[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.250000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [blankEmpty]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blankEmpty* updates
                if blankEmpty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blankEmpty.frameNStart = frameN  # exact frame index
                    blankEmpty.tStart = t  # local t and not account for scr refresh
                    blankEmpty.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blankEmpty, 'tStartRefresh')  # time at next scr refresh
                    blankEmpty.setAutoDraw(True)
                if blankEmpty.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blankEmpty.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        blankEmpty.tStop = t  # not accounting for scr refresh
                        blankEmpty.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blankEmpty, 'tStopRefresh')  # time at next scr refresh
                        blankEmpty.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            multiLoopPrac.addData('blankEmpty.started', blankEmpty.tStartRefresh)
            multiLoopPrac.addData('blankEmpty.stopped', blankEmpty.tStopRefresh)
            
            # ------Prepare to start Routine "MultiplyPrac"-------
            continueRoutine = True
            # update component parameters for each repeat
            modify = False
            inputText2.text = ''
            event.clearEvents('keyboard')
            t=0
            productText.setText(problem)
            # keep track of which components have finished
            MultiplyPracComponents = [inputText2, productText, contText2]
            for thisComponent in MultiplyPracComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            MultiplyPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "MultiplyPrac"-------
            while continueRoutine:
                # get current time
                t = MultiplyPracClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=MultiplyPracClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                keys = event.getKeys(keyList =['backspace','return','1','2','3','4','5','6','7','8','9','0'])
                if len(keys):
                    if 'backspace' in keys:
                        inputText2.text = inputText2.text[:-1]
                    elif 'return' in keys:
                        continueRoutine = False
                        thisExp.addData("typedAnswer", inputText2.text)
                        thisExp.addData('multiplyRT', t)
                    else:
                        if modify:
                            inputText2.text = inputText2.text + keys[0].upper()
                            modify = False
                        else:
                            inputText2.text = inputText2.text + keys[0]
                
                # *inputText2* updates
                if inputText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inputText2.frameNStart = frameN  # exact frame index
                    inputText2.tStart = t  # local t and not account for scr refresh
                    inputText2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inputText2, 'tStartRefresh')  # time at next scr refresh
                    inputText2.setAutoDraw(True)
                
                # *productText* updates
                if productText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    productText.frameNStart = frameN  # exact frame index
                    productText.tStart = t  # local t and not account for scr refresh
                    productText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(productText, 'tStartRefresh')  # time at next scr refresh
                    productText.setAutoDraw(True)
                
                # *contText2* updates
                if contText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    contText2.frameNStart = frameN  # exact frame index
                    contText2.tStart = t  # local t and not account for scr refresh
                    contText2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(contText2, 'tStartRefresh')  # time at next scr refresh
                    contText2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MultiplyPracComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "MultiplyPrac"-------
            for thisComponent in MultiplyPracComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            if int(inputText2.text) == Answer:
                # store in the data file manually:
                thisExp.addData('multiplyCorr', 1) 
            else:
                thisExp.addData('multiplyCorr', 0)
            multiLoopPrac.addData('inputText2.started', inputText2.tStartRefresh)
            multiLoopPrac.addData('inputText2.stopped', inputText2.tStopRefresh)
            multiLoopPrac.addData('productText.started', productText.tStartRefresh)
            multiLoopPrac.addData('productText.stopped', productText.tStopRefresh)
            multiLoopPrac.addData('contText2.started', contText2.tStartRefresh)
            multiLoopPrac.addData('contText2.stopped', contText2.tStopRefresh)
            # the Routine "MultiplyPrac" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "MultiplyFeedback"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            if int(inputText2.text) ==Answer:
                message='Correct!' 
            else:
                message = 'Wrong!'
            mulFBText.setText(message)
            # keep track of which components have finished
            MultiplyFeedbackComponents = [mulFBText]
            for thisComponent in MultiplyFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            MultiplyFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "MultiplyFeedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = MultiplyFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=MultiplyFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *mulFBText* updates
                if mulFBText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mulFBText.frameNStart = frameN  # exact frame index
                    mulFBText.tStart = t  # local t and not account for scr refresh
                    mulFBText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mulFBText, 'tStartRefresh')  # time at next scr refresh
                    mulFBText.setAutoDraw(True)
                if mulFBText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mulFBText.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        mulFBText.tStop = t  # not accounting for scr refresh
                        mulFBText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(mulFBText, 'tStopRefresh')  # time at next scr refresh
                        mulFBText.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MultiplyFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "MultiplyFeedback"-------
            for thisComponent in MultiplyFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            multiLoopPrac.addData('mulFBText.started', mulFBText.tStartRefresh)
            multiLoopPrac.addData('mulFBText.stopped', mulFBText.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'multiLoopPrac'
        
        
        # ------Prepare to start Routine "BeginTrialScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        beginResp.keys = []
        beginResp.rt = []
        _beginResp_allKeys = []
        # keep track of which components have finished
        BeginTrialScreenComponents = [beginTrialText, beginResp]
        for thisComponent in BeginTrialScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BeginTrialScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BeginTrialScreen"-------
        while continueRoutine:
            # get current time
            t = BeginTrialScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BeginTrialScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *beginTrialText* updates
            if beginTrialText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beginTrialText.frameNStart = frameN  # exact frame index
                beginTrialText.tStart = t  # local t and not account for scr refresh
                beginTrialText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beginTrialText, 'tStartRefresh')  # time at next scr refresh
                beginTrialText.setAutoDraw(True)
            
            # *beginResp* updates
            waitOnFlip = False
            if beginResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beginResp.frameNStart = frameN  # exact frame index
                beginResp.tStart = t  # local t and not account for scr refresh
                beginResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beginResp, 'tStartRefresh')  # time at next scr refresh
                beginResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(beginResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(beginResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if beginResp.status == STARTED and not waitOnFlip:
                theseKeys = beginResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _beginResp_allKeys.extend(theseKeys)
                if len(_beginResp_allKeys):
                    beginResp.keys = _beginResp_allKeys[-1].name  # just the last key pressed
                    beginResp.rt = _beginResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BeginTrialScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BeginTrialScreen"-------
        for thisComponent in BeginTrialScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskA.addData('beginTrialText.started', beginTrialText.tStartRefresh)
        TaskA.addData('beginTrialText.stopped', beginTrialText.tStopRefresh)
        # the Routine "BeginTrialScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('multiplyConds.xlsx'),
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "READY"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp1.keys = []
            key_resp1.rt = []
            _key_resp1_allKeys = []
            # keep track of which components have finished
            READYComponents = [text_1, key_resp1]
            for thisComponent in READYComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            READYClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "READY"-------
            while continueRoutine:
                # get current time
                t = READYClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=READYClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_1* updates
                if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_1.frameNStart = frameN  # exact frame index
                    text_1.tStart = t  # local t and not account for scr refresh
                    text_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                    text_1.setAutoDraw(True)
                
                # *key_resp1* updates
                waitOnFlip = False
                if key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp1.frameNStart = frameN  # exact frame index
                    key_resp1.tStart = t  # local t and not account for scr refresh
                    key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
                    key_resp1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp1.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp1.getKeys(keyList=['o', 'space'], waitRelease=False)
                    _key_resp1_allKeys.extend(theseKeys)
                    if len(_key_resp1_allKeys):
                        key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                        key_resp1.rt = _key_resp1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in READYComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "READY"-------
            for thisComponent in READYComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('text_1.started', text_1.tStartRefresh)
            trials_2.addData('text_1.stopped', text_1.tStopRefresh)
            # the Routine "READY" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            multiRTrial = data.TrialHandler(nReps=1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(fileee),
                seed=None, name='multiRTrial')
            thisExp.addLoop(multiRTrial)  # add the loop to the experiment
            thisMultiRTrial = multiRTrial.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisMultiRTrial.rgb)
            if thisMultiRTrial != None:
                for paramName in thisMultiRTrial:
                    exec('{} = thisMultiRTrial[paramName]'.format(paramName))
            
            for thisMultiRTrial in multiRTrial:
                currentLoop = multiRTrial
                # abbreviate parameter names if possible (e.g. rgb = thisMultiRTrial.rgb)
                if thisMultiRTrial != None:
                    for paramName in thisMultiRTrial:
                        exec('{} = thisMultiRTrial[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "Blank500"-------
                continueRoutine = True
                routineTimer.add(0.250000)
                # update component parameters for each repeat
                # keep track of which components have finished
                Blank500Components = [blankEmpty]
                for thisComponent in Blank500Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Blank500"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = Blank500Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blankEmpty* updates
                    if blankEmpty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blankEmpty.frameNStart = frameN  # exact frame index
                        blankEmpty.tStart = t  # local t and not account for scr refresh
                        blankEmpty.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blankEmpty, 'tStartRefresh')  # time at next scr refresh
                        blankEmpty.setAutoDraw(True)
                    if blankEmpty.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blankEmpty.tStartRefresh + 0.25-frameTolerance:
                            # keep track of stop time/frame for later
                            blankEmpty.tStop = t  # not accounting for scr refresh
                            blankEmpty.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(blankEmpty, 'tStopRefresh')  # time at next scr refresh
                            blankEmpty.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Blank500Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Blank500"-------
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                multiRTrial.addData('blankEmpty.started', blankEmpty.tStartRefresh)
                multiRTrial.addData('blankEmpty.stopped', blankEmpty.tStopRefresh)
                
                # ------Prepare to start Routine "MultiplyPrac"-------
                continueRoutine = True
                # update component parameters for each repeat
                modify = False
                inputText2.text = ''
                event.clearEvents('keyboard')
                t=0
                productText.setText(problem)
                # keep track of which components have finished
                MultiplyPracComponents = [inputText2, productText, contText2]
                for thisComponent in MultiplyPracComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                MultiplyPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "MultiplyPrac"-------
                while continueRoutine:
                    # get current time
                    t = MultiplyPracClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=MultiplyPracClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    keys = event.getKeys(keyList =['backspace','return','1','2','3','4','5','6','7','8','9','0'])
                    if len(keys):
                        if 'backspace' in keys:
                            inputText2.text = inputText2.text[:-1]
                        elif 'return' in keys:
                            continueRoutine = False
                            thisExp.addData("typedAnswer", inputText2.text)
                            thisExp.addData('multiplyRT', t)
                        else:
                            if modify:
                                inputText2.text = inputText2.text + keys[0].upper()
                                modify = False
                            else:
                                inputText2.text = inputText2.text + keys[0]
                    
                    # *inputText2* updates
                    if inputText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        inputText2.frameNStart = frameN  # exact frame index
                        inputText2.tStart = t  # local t and not account for scr refresh
                        inputText2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(inputText2, 'tStartRefresh')  # time at next scr refresh
                        inputText2.setAutoDraw(True)
                    
                    # *productText* updates
                    if productText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        productText.frameNStart = frameN  # exact frame index
                        productText.tStart = t  # local t and not account for scr refresh
                        productText.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(productText, 'tStartRefresh')  # time at next scr refresh
                        productText.setAutoDraw(True)
                    
                    # *contText2* updates
                    if contText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        contText2.frameNStart = frameN  # exact frame index
                        contText2.tStart = t  # local t and not account for scr refresh
                        contText2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(contText2, 'tStartRefresh')  # time at next scr refresh
                        contText2.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in MultiplyPracComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "MultiplyPrac"-------
                for thisComponent in MultiplyPracComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                if int(inputText2.text) == Answer:
                    # store in the data file manually:
                    thisExp.addData('multiplyCorr', 1) 
                else:
                    thisExp.addData('multiplyCorr', 0)
                multiRTrial.addData('inputText2.started', inputText2.tStartRefresh)
                multiRTrial.addData('inputText2.stopped', inputText2.tStopRefresh)
                multiRTrial.addData('productText.started', productText.tStartRefresh)
                multiRTrial.addData('productText.stopped', productText.tStopRefresh)
                multiRTrial.addData('contText2.started', contText2.tStartRefresh)
                multiRTrial.addData('contText2.stopped', contText2.tStopRefresh)
                # the Routine "MultiplyPrac" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'multiRTrial'
            
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_2'
        
        
        # ------Prepare to start Routine "BreakTime"-------
        continueRoutine = True
        # update component parameters for each repeat
        breakResp.keys = []
        breakResp.rt = []
        _breakResp_allKeys = []
        # keep track of which components have finished
        BreakTimeComponents = [breakText, breakResp]
        for thisComponent in BreakTimeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BreakTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BreakTime"-------
        while continueRoutine:
            # get current time
            t = BreakTimeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BreakTimeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *breakText* updates
            if breakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breakText.frameNStart = frameN  # exact frame index
                breakText.tStart = t  # local t and not account for scr refresh
                breakText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
                breakText.setAutoDraw(True)
            
            # *breakResp* updates
            waitOnFlip = False
            if breakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breakResp.frameNStart = frameN  # exact frame index
                breakResp.tStart = t  # local t and not account for scr refresh
                breakResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breakResp, 'tStartRefresh')  # time at next scr refresh
                breakResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(breakResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(breakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if breakResp.status == STARTED and not waitOnFlip:
                theseKeys = breakResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _breakResp_allKeys.extend(theseKeys)
                if len(_breakResp_allKeys):
                    breakResp.keys = _breakResp_allKeys[-1].name  # just the last key pressed
                    breakResp.rt = _breakResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BreakTimeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BreakTime"-------
        for thisComponent in BreakTimeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskA.addData('breakText.started', breakText.tStartRefresh)
        TaskA.addData('breakText.stopped', breakText.tStopRefresh)
        # the Routine "BreakTime" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsTask1 repeats of 'TaskA'
    
    
    # set up handler to look after randomisation of conditions etc
    TaskB = data.TrialHandler(nReps=nRepsTask2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TaskB')
    thisExp.addLoop(TaskB)  # add the loop to the experiment
    thisTaskB = TaskB.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTaskB.rgb)
    if thisTaskB != None:
        for paramName in thisTaskB:
            exec('{} = thisTaskB[paramName]'.format(paramName))
    
    for thisTaskB in TaskB:
        currentLoop = TaskB
        # abbreviate parameter names if possible (e.g. rgb = thisTaskB.rgb)
        if thisTaskB != None:
            for paramName in thisTaskB:
                exec('{} = thisTaskB[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AdjustSoundInst"-------
        continueRoutine = True
        # update component parameters for each repeat
        volInstruResp.keys = []
        volInstruResp.rt = []
        _volInstruResp_allKeys = []
        # keep track of which components have finished
        AdjustSoundInstComponents = [volumeText, volInstruResp]
        for thisComponent in AdjustSoundInstComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AdjustSoundInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AdjustSoundInst"-------
        while continueRoutine:
            # get current time
            t = AdjustSoundInstClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AdjustSoundInstClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *volumeText* updates
            if volumeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                volumeText.frameNStart = frameN  # exact frame index
                volumeText.tStart = t  # local t and not account for scr refresh
                volumeText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(volumeText, 'tStartRefresh')  # time at next scr refresh
                volumeText.setAutoDraw(True)
            
            # *volInstruResp* updates
            waitOnFlip = False
            if volInstruResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                volInstruResp.frameNStart = frameN  # exact frame index
                volInstruResp.tStart = t  # local t and not account for scr refresh
                volInstruResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(volInstruResp, 'tStartRefresh')  # time at next scr refresh
                volInstruResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(volInstruResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(volInstruResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if volInstruResp.status == STARTED and not waitOnFlip:
                theseKeys = volInstruResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _volInstruResp_allKeys.extend(theseKeys)
                if len(_volInstruResp_allKeys):
                    volInstruResp.keys = _volInstruResp_allKeys[-1].name  # just the last key pressed
                    volInstruResp.rt = _volInstruResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AdjustSoundInstComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AdjustSoundInst"-------
        for thisComponent in AdjustSoundInstComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskB.addData('volumeText.started', volumeText.tStartRefresh)
        TaskB.addData('volumeText.stopped', volumeText.tStopRefresh)
        # the Routine "AdjustSoundInst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AdjustSoundVol"-------
        continueRoutine = True
        # update component parameters for each repeat
        sampleSoundVol.setSound('Audio/sample.wav', hamming=True)
        sampleSoundVol.setVolume(0.5, log=False)
        sampleResp.keys = []
        sampleResp.rt = []
        _sampleResp_allKeys = []
        # keep track of which components have finished
        AdjustSoundVolComponents = [ISI_2, sampleSoundVol, sampleResp, sampleText]
        for thisComponent in AdjustSoundVolComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AdjustSoundVolClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AdjustSoundVol"-------
        while continueRoutine:
            # get current time
            t = AdjustSoundVolClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AdjustSoundVolClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sampleSoundVol
            if sampleSoundVol.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleSoundVol.frameNStart = frameN  # exact frame index
                sampleSoundVol.tStart = t  # local t and not account for scr refresh
                sampleSoundVol.tStartRefresh = tThisFlipGlobal  # on global time
                sampleSoundVol.play(when=win)  # sync with win flip
            
            # *sampleResp* updates
            waitOnFlip = False
            if sampleResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleResp.frameNStart = frameN  # exact frame index
                sampleResp.tStart = t  # local t and not account for scr refresh
                sampleResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleResp, 'tStartRefresh')  # time at next scr refresh
                sampleResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(sampleResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(sampleResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if sampleResp.status == STARTED and not waitOnFlip:
                theseKeys = sampleResp.getKeys(keyList=['0', 'space'], waitRelease=False)
                _sampleResp_allKeys.extend(theseKeys)
                if len(_sampleResp_allKeys):
                    sampleResp.keys = _sampleResp_allKeys[-1].name  # just the last key pressed
                    sampleResp.rt = _sampleResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *sampleText* updates
            if sampleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleText.frameNStart = frameN  # exact frame index
                sampleText.tStart = t  # local t and not account for scr refresh
                sampleText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleText, 'tStartRefresh')  # time at next scr refresh
                sampleText.setAutoDraw(True)
            # *ISI_2* period
            if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI_2.frameNStart = frameN  # exact frame index
                ISI_2.tStart = t  # local t and not account for scr refresh
                ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
                ISI_2.start(1)
            elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                ISI_2.complete()  # finish the static period
                ISI_2.tStop = ISI_2.tStart + 1  # record stop time
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AdjustSoundVolComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AdjustSoundVol"-------
        for thisComponent in AdjustSoundVolComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskB.addData('ISI_2.started', ISI_2.tStart)
        TaskB.addData('ISI_2.stopped', ISI_2.tStop)
        sampleSoundVol.stop()  # ensure sound has stopped at end of routine
        TaskB.addData('sampleSoundVol.started', sampleSoundVol.tStartRefresh)
        TaskB.addData('sampleSoundVol.stopped', sampleSoundVol.tStopRefresh)
        TaskB.addData('sampleText.started', sampleText.tStartRefresh)
        TaskB.addData('sampleText.stopped', sampleText.tStopRefresh)
        # the Routine "AdjustSoundVol" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AuditoryScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        AuditoryResp.keys = []
        AuditoryResp.rt = []
        _AuditoryResp_allKeys = []
        # keep track of which components have finished
        AuditoryScreenComponents = [pracAuditoryText, AuditoryResp]
        for thisComponent in AuditoryScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AuditoryScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AuditoryScreen"-------
        while continueRoutine:
            # get current time
            t = AuditoryScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AuditoryScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pracAuditoryText* updates
            if pracAuditoryText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pracAuditoryText.frameNStart = frameN  # exact frame index
                pracAuditoryText.tStart = t  # local t and not account for scr refresh
                pracAuditoryText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pracAuditoryText, 'tStartRefresh')  # time at next scr refresh
                pracAuditoryText.setAutoDraw(True)
            
            # *AuditoryResp* updates
            waitOnFlip = False
            if AuditoryResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AuditoryResp.frameNStart = frameN  # exact frame index
                AuditoryResp.tStart = t  # local t and not account for scr refresh
                AuditoryResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AuditoryResp, 'tStartRefresh')  # time at next scr refresh
                AuditoryResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(AuditoryResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(AuditoryResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if AuditoryResp.status == STARTED and not waitOnFlip:
                theseKeys = AuditoryResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _AuditoryResp_allKeys.extend(theseKeys)
                if len(_AuditoryResp_allKeys):
                    AuditoryResp.keys = _AuditoryResp_allKeys[-1].name  # just the last key pressed
                    AuditoryResp.rt = _AuditoryResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AuditoryScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AuditoryScreen"-------
        for thisComponent in AuditoryScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskB.addData('pracAuditoryText.started', pracAuditoryText.tStartRefresh)
        TaskB.addData('pracAuditoryText.stopped', pracAuditoryText.tStopRefresh)
        # the Routine "AuditoryScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "PracticeScreen_1"-------
        continueRoutine = True
        # update component parameters for each repeat
        PracticeScResp.keys = []
        PracticeScResp.rt = []
        _PracticeScResp_allKeys = []
        # keep track of which components have finished
        PracticeScreen_1Components = [PracticeInstruction, PracticeScResp]
        for thisComponent in PracticeScreen_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeScreen_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeScreen_1"-------
        while continueRoutine:
            # get current time
            t = PracticeScreen_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeScreen_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PracticeInstruction* updates
            if PracticeInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeInstruction.frameNStart = frameN  # exact frame index
                PracticeInstruction.tStart = t  # local t and not account for scr refresh
                PracticeInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeInstruction, 'tStartRefresh')  # time at next scr refresh
                PracticeInstruction.setAutoDraw(True)
            
            # *PracticeScResp* updates
            waitOnFlip = False
            if PracticeScResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeScResp.frameNStart = frameN  # exact frame index
                PracticeScResp.tStart = t  # local t and not account for scr refresh
                PracticeScResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeScResp, 'tStartRefresh')  # time at next scr refresh
                PracticeScResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracticeScResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracticeScResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracticeScResp.status == STARTED and not waitOnFlip:
                theseKeys = PracticeScResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _PracticeScResp_allKeys.extend(theseKeys)
                if len(_PracticeScResp_allKeys):
                    PracticeScResp.keys = _PracticeScResp_allKeys[-1].name  # just the last key pressed
                    PracticeScResp.rt = _PracticeScResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeScreen_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeScreen_1"-------
        for thisComponent in PracticeScreen_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskB.addData('PracticeInstruction.started', PracticeInstruction.tStartRefresh)
        TaskB.addData('PracticeInstruction.stopped', PracticeInstruction.tStopRefresh)
        # the Routine "PracticeScreen_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        audioLoopPrac = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('auditoryPract.xlsx'),
            seed=None, name='audioLoopPrac')
        thisExp.addLoop(audioLoopPrac)  # add the loop to the experiment
        thisAudioLoopPrac = audioLoopPrac.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAudioLoopPrac.rgb)
        if thisAudioLoopPrac != None:
            for paramName in thisAudioLoopPrac:
                exec('{} = thisAudioLoopPrac[paramName]'.format(paramName))
        
        for thisAudioLoopPrac in audioLoopPrac:
            currentLoop = audioLoopPrac
            # abbreviate parameter names if possible (e.g. rgb = thisAudioLoopPrac.rgb)
            if thisAudioLoopPrac != None:
                for paramName in thisAudioLoopPrac:
                    exec('{} = thisAudioLoopPrac[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Audio_Play"-------
            continueRoutine = True
            # update component parameters for each repeat
            soundPresentation.setSound(soundsJS, hamming=True)
            soundPresentation.setVolume(1, log=False)
            # keep track of which components have finished
            Audio_PlayComponents = [soundPresentation, text1, ISI, crossFix1]
            for thisComponent in Audio_PlayComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Audio_PlayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Audio_Play"-------
            while continueRoutine:
                # get current time
                t = Audio_PlayClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Audio_PlayClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop soundPresentation
                if soundPresentation.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    soundPresentation.frameNStart = frameN  # exact frame index
                    soundPresentation.tStart = t  # local t and not account for scr refresh
                    soundPresentation.tStartRefresh = tThisFlipGlobal  # on global time
                    soundPresentation.play()  # start the sound (it finishes automatically)
                
                # *text1* updates
                if text1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    text1.frameNStart = frameN  # exact frame index
                    text1.tStart = t  # local t and not account for scr refresh
                    text1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
                    text1.setAutoDraw(True)
                if text1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text1.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        text1.tStop = t  # not accounting for scr refresh
                        text1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                        text1.setAutoDraw(False)
                
                # *crossFix1* updates
                if crossFix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crossFix1.frameNStart = frameN  # exact frame index
                    crossFix1.tStart = t  # local t and not account for scr refresh
                    crossFix1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crossFix1, 'tStartRefresh')  # time at next scr refresh
                    crossFix1.setAutoDraw(True)
                if crossFix1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crossFix1.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        crossFix1.tStop = t  # not accounting for scr refresh
                        crossFix1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(crossFix1, 'tStopRefresh')  # time at next scr refresh
                        crossFix1.setAutoDraw(False)
                # *ISI* period
                if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.tStart = t  # local t and not account for scr refresh
                    ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                    ISI.start(1)
                elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                    ISI.complete()  # finish the static period
                    ISI.tStop = ISI.tStart + 1  # record stop time
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Audio_PlayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Audio_Play"-------
            for thisComponent in Audio_PlayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            soundPresentation.stop()  # ensure sound has stopped at end of routine
            audioLoopPrac.addData('soundPresentation.started', soundPresentation.tStart)
            audioLoopPrac.addData('soundPresentation.stopped', soundPresentation.tStop)
            audioLoopPrac.addData('text1.started', text1.tStartRefresh)
            audioLoopPrac.addData('text1.stopped', text1.tStopRefresh)
            audioLoopPrac.addData('ISI.started', ISI.tStart)
            audioLoopPrac.addData('ISI.stopped', ISI.tStop)
            audioLoopPrac.addData('crossFix1.started', crossFix1.tStartRefresh)
            audioLoopPrac.addData('crossFix1.stopped', crossFix1.tStopRefresh)
            # the Routine "Audio_Play" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "AuditoryPracticeSet"-------
            continueRoutine = True
            # update component parameters for each repeat
            modify = False
            inputText4.text = ''
            event.clearEvents('keyboard')
            t=0
            # keep track of which components have finished
            AuditoryPracticeSetComponents = [inputText4, contText4, RECALLtext2]
            for thisComponent in AuditoryPracticeSetComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AuditoryPracticeSetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AuditoryPracticeSet"-------
            while continueRoutine:
                # get current time
                t = AuditoryPracticeSetClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AuditoryPracticeSetClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                keys = event.getKeys(keyList =['backspace','return','1','2','3','4','5','6','7','8','9','0'])
                if len(keys):
                    if 'backspace' in keys:
                        inputText4.text = inputText4.text[:-1]
                    elif 'return' in keys:
                        continueRoutine = False
                        thisExp.addData("typedAudioPrac", inputText4.text)
                        thisExp.addData('audioPracRT', t)
                    else:
                        if modify:
                            inputText4.text = inputText4.text + keys[0].upper()
                            modify = False
                        else:
                            inputText4.text = inputText4.text + keys[0]
                
                # *inputText4* updates
                if inputText4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inputText4.frameNStart = frameN  # exact frame index
                    inputText4.tStart = t  # local t and not account for scr refresh
                    inputText4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inputText4, 'tStartRefresh')  # time at next scr refresh
                    inputText4.setAutoDraw(True)
                
                # *contText4* updates
                if contText4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    contText4.frameNStart = frameN  # exact frame index
                    contText4.tStart = t  # local t and not account for scr refresh
                    contText4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(contText4, 'tStartRefresh')  # time at next scr refresh
                    contText4.setAutoDraw(True)
                
                # *RECALLtext2* updates
                if RECALLtext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RECALLtext2.frameNStart = frameN  # exact frame index
                    RECALLtext2.tStart = t  # local t and not account for scr refresh
                    RECALLtext2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RECALLtext2, 'tStartRefresh')  # time at next scr refresh
                    RECALLtext2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AuditoryPracticeSetComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AuditoryPracticeSet"-------
            for thisComponent in AuditoryPracticeSetComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            if int(inputText4.text) ==digits_audio:
                # store in the data file manually:
                thisExp.addData('audioPrCorr', 1) # or True or 'Yes', or whatever
            else:
                thisExp.addData('audioPrCorr', 0)
            audioLoopPrac.addData('inputText4.started', inputText4.tStartRefresh)
            audioLoopPrac.addData('inputText4.stopped', inputText4.tStopRefresh)
            audioLoopPrac.addData('contText4.started', contText4.tStartRefresh)
            audioLoopPrac.addData('contText4.stopped', contText4.tStopRefresh)
            audioLoopPrac.addData('RECALLtext2.started', RECALLtext2.tStartRefresh)
            audioLoopPrac.addData('RECALLtext2.stopped', RECALLtext2.tStopRefresh)
            # the Routine "AuditoryPracticeSet" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "AuditoryFeedback"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            if int(inputText4.text) ==digits_audio:
                Feedback='Correct!' 
            else:
                Feedback = 'Wrong!'
            AudioFBText.setText(Feedback)
            # keep track of which components have finished
            AuditoryFeedbackComponents = [AudioFBText]
            for thisComponent in AuditoryFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AuditoryFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AuditoryFeedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AuditoryFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AuditoryFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *AudioFBText* updates
                if AudioFBText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AudioFBText.frameNStart = frameN  # exact frame index
                    AudioFBText.tStart = t  # local t and not account for scr refresh
                    AudioFBText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AudioFBText, 'tStartRefresh')  # time at next scr refresh
                    AudioFBText.setAutoDraw(True)
                if AudioFBText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > AudioFBText.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        AudioFBText.tStop = t  # not accounting for scr refresh
                        AudioFBText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(AudioFBText, 'tStopRefresh')  # time at next scr refresh
                        AudioFBText.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AuditoryFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AuditoryFeedback"-------
            for thisComponent in AuditoryFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            audioLoopPrac.addData('AudioFBText.started', AudioFBText.tStartRefresh)
            audioLoopPrac.addData('AudioFBText.stopped', AudioFBText.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'audioLoopPrac'
        
        
        # ------Prepare to start Routine "BeginTrialScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        beginResp.keys = []
        beginResp.rt = []
        _beginResp_allKeys = []
        # keep track of which components have finished
        BeginTrialScreenComponents = [beginTrialText, beginResp]
        for thisComponent in BeginTrialScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BeginTrialScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BeginTrialScreen"-------
        while continueRoutine:
            # get current time
            t = BeginTrialScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BeginTrialScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *beginTrialText* updates
            if beginTrialText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beginTrialText.frameNStart = frameN  # exact frame index
                beginTrialText.tStart = t  # local t and not account for scr refresh
                beginTrialText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beginTrialText, 'tStartRefresh')  # time at next scr refresh
                beginTrialText.setAutoDraw(True)
            
            # *beginResp* updates
            waitOnFlip = False
            if beginResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beginResp.frameNStart = frameN  # exact frame index
                beginResp.tStart = t  # local t and not account for scr refresh
                beginResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beginResp, 'tStartRefresh')  # time at next scr refresh
                beginResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(beginResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(beginResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if beginResp.status == STARTED and not waitOnFlip:
                theseKeys = beginResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _beginResp_allKeys.extend(theseKeys)
                if len(_beginResp_allKeys):
                    beginResp.keys = _beginResp_allKeys[-1].name  # just the last key pressed
                    beginResp.rt = _beginResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BeginTrialScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BeginTrialScreen"-------
        for thisComponent in BeginTrialScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskB.addData('beginTrialText.started', beginTrialText.tStartRefresh)
        TaskB.addData('beginTrialText.stopped', beginTrialText.tStopRefresh)
        # the Routine "BeginTrialScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        audioCondLoop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('choose_digitSpan.xlsx'),
            seed=None, name='audioCondLoop')
        thisExp.addLoop(audioCondLoop)  # add the loop to the experiment
        thisAudioCondLoop = audioCondLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAudioCondLoop.rgb)
        if thisAudioCondLoop != None:
            for paramName in thisAudioCondLoop:
                exec('{} = thisAudioCondLoop[paramName]'.format(paramName))
        
        for thisAudioCondLoop in audioCondLoop:
            currentLoop = audioCondLoop
            # abbreviate parameter names if possible (e.g. rgb = thisAudioCondLoop.rgb)
            if thisAudioCondLoop != None:
                for paramName in thisAudioCondLoop:
                    exec('{} = thisAudioCondLoop[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            audioRTrial = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(Condition),
                seed=None, name='audioRTrial')
            thisExp.addLoop(audioRTrial)  # add the loop to the experiment
            thisAudioRTrial = audioRTrial.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisAudioRTrial.rgb)
            if thisAudioRTrial != None:
                for paramName in thisAudioRTrial:
                    exec('{} = thisAudioRTrial[paramName]'.format(paramName))
            
            for thisAudioRTrial in audioRTrial:
                currentLoop = audioRTrial
                # abbreviate parameter names if possible (e.g. rgb = thisAudioRTrial.rgb)
                if thisAudioRTrial != None:
                    for paramName in thisAudioRTrial:
                        exec('{} = thisAudioRTrial[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "Audio_Play"-------
                continueRoutine = True
                # update component parameters for each repeat
                soundPresentation.setSound(soundsJS, hamming=True)
                soundPresentation.setVolume(1, log=False)
                # keep track of which components have finished
                Audio_PlayComponents = [soundPresentation, text1, ISI, crossFix1]
                for thisComponent in Audio_PlayComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                Audio_PlayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Audio_Play"-------
                while continueRoutine:
                    # get current time
                    t = Audio_PlayClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=Audio_PlayClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # start/stop soundPresentation
                    if soundPresentation.status == NOT_STARTED and t >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        soundPresentation.frameNStart = frameN  # exact frame index
                        soundPresentation.tStart = t  # local t and not account for scr refresh
                        soundPresentation.tStartRefresh = tThisFlipGlobal  # on global time
                        soundPresentation.play()  # start the sound (it finishes automatically)
                    
                    # *text1* updates
                    if text1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        text1.frameNStart = frameN  # exact frame index
                        text1.tStart = t  # local t and not account for scr refresh
                        text1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
                        text1.setAutoDraw(True)
                    if text1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text1.tStartRefresh + 3-frameTolerance:
                            # keep track of stop time/frame for later
                            text1.tStop = t  # not accounting for scr refresh
                            text1.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                            text1.setAutoDraw(False)
                    
                    # *crossFix1* updates
                    if crossFix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        crossFix1.frameNStart = frameN  # exact frame index
                        crossFix1.tStart = t  # local t and not account for scr refresh
                        crossFix1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(crossFix1, 'tStartRefresh')  # time at next scr refresh
                        crossFix1.setAutoDraw(True)
                    if crossFix1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > crossFix1.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            crossFix1.tStop = t  # not accounting for scr refresh
                            crossFix1.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(crossFix1, 'tStopRefresh')  # time at next scr refresh
                            crossFix1.setAutoDraw(False)
                    # *ISI* period
                    if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        ISI.frameNStart = frameN  # exact frame index
                        ISI.tStart = t  # local t and not account for scr refresh
                        ISI.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                        ISI.start(1)
                    elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                        ISI.complete()  # finish the static period
                        ISI.tStop = ISI.tStart + 1  # record stop time
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Audio_PlayComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Audio_Play"-------
                for thisComponent in Audio_PlayComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                soundPresentation.stop()  # ensure sound has stopped at end of routine
                audioRTrial.addData('soundPresentation.started', soundPresentation.tStart)
                audioRTrial.addData('soundPresentation.stopped', soundPresentation.tStop)
                audioRTrial.addData('text1.started', text1.tStartRefresh)
                audioRTrial.addData('text1.stopped', text1.tStopRefresh)
                audioRTrial.addData('ISI.started', ISI.tStart)
                audioRTrial.addData('ISI.stopped', ISI.tStop)
                audioRTrial.addData('crossFix1.started', crossFix1.tStartRefresh)
                audioRTrial.addData('crossFix1.stopped', crossFix1.tStopRefresh)
                # the Routine "Audio_Play" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "AuditoryTrialss"-------
                continueRoutine = True
                # update component parameters for each repeat
                audioResp.rt = []
                audioResp.keys = []
                audioResp.rt = []
                _audioResp_allKeys = []
                # keep track of which components have finished
                AuditoryTrialssComponents = [inputText3, contText3, RECALLtext, audioResp]
                for thisComponent in AuditoryTrialssComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                AuditoryTrialssClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "AuditoryTrialss"-------
                while continueRoutine:
                    # get current time
                    t = AuditoryTrialssClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=AuditoryTrialssClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    if len(audioResp.keys) > 0: #to prevent list index error
                        if audioResp.keys[-1] == 'backspace': #allow backspacing
                            try: #to avoid list index errors when backspacing
                                audioResp.keys.pop(len(audioResp.keys)-1)
                                audioResp.keys.pop(len(audioResp.keys)-1)
                                audioResp.keys.remove("backspace")
                            except:
                                print('No need to backspace')
                        elif audioResp.keys[-1] == 'return': #allows return to end routine
                            audioResp.keys.pop(len(audioResp.keys)-1)
                            continueRoutine = False
                    
                    current_resp = ''.join(audioResp.keys)
                    
                    # *inputText3* updates
                    if inputText3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        inputText3.frameNStart = frameN  # exact frame index
                        inputText3.tStart = t  # local t and not account for scr refresh
                        inputText3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(inputText3, 'tStartRefresh')  # time at next scr refresh
                        inputText3.setAutoDraw(True)
                    if inputText3.status == STARTED:  # only update if drawing
                        inputText3.setText(current_resp)
                    
                    # *contText3* updates
                    if contText3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        contText3.frameNStart = frameN  # exact frame index
                        contText3.tStart = t  # local t and not account for scr refresh
                        contText3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(contText3, 'tStartRefresh')  # time at next scr refresh
                        contText3.setAutoDraw(True)
                    
                    # *RECALLtext* updates
                    if RECALLtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        RECALLtext.frameNStart = frameN  # exact frame index
                        RECALLtext.tStart = t  # local t and not account for scr refresh
                        RECALLtext.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(RECALLtext, 'tStartRefresh')  # time at next scr refresh
                        RECALLtext.setAutoDraw(True)
                    
                    # *audioResp* updates
                    waitOnFlip = False
                    if audioResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        audioResp.frameNStart = frameN  # exact frame index
                        audioResp.tStart = t  # local t and not account for scr refresh
                        audioResp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(audioResp, 'tStartRefresh')  # time at next scr refresh
                        audioResp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(audioResp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(audioResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if audioResp.status == STARTED and not waitOnFlip:
                        theseKeys = audioResp.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'return', 'backspace'], waitRelease=False)
                        _audioResp_allKeys.extend(theseKeys)
                        if len(_audioResp_allKeys):
                            audioResp.keys = [key.name for key in _audioResp_allKeys]  # storing all keys
                            audioResp.rt = [key.rt for key in _audioResp_allKeys]
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in AuditoryTrialssComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "AuditoryTrialss"-------
                for thisComponent in AuditoryTrialssComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                correct = 0
                if int(current_resp) == digits_audio:
                    correct = 1
                    trials.addData('correct', correct) #where trials is the name of the loop
                else:
                    trials.addData('Incorrect', correct) #store for accuracy
                trials.addData('response', current_resp) #store full response
                
                # Store each response in list
                allResponses.append(correct)
                
                # for incorrect, check that two responses exist
                # and that their sum of last two responses is zero
                if len(allResponses) >= 2 and sum(allResponses[-2:]) == 0:
                    audioCondLoop.finished = True
                # If sum of last two responses is 2, move to next sequence
                elif sum(allResponses[-2:]) >= 1:
                    audioRTrial.finished = True
                    allResponses = []
                audioRTrial.addData('inputText3.started', inputText3.tStartRefresh)
                audioRTrial.addData('inputText3.stopped', inputText3.tStopRefresh)
                audioRTrial.addData('contText3.started', contText3.tStartRefresh)
                audioRTrial.addData('contText3.stopped', contText3.tStopRefresh)
                audioRTrial.addData('RECALLtext.started', RECALLtext.tStartRefresh)
                audioRTrial.addData('RECALLtext.stopped', RECALLtext.tStopRefresh)
                # check responses
                if audioResp.keys in ['', [], None]:  # No response was made
                    audioResp.keys = None
                audioRTrial.addData('audioResp.keys',audioResp.keys)
                if audioResp.keys != None:  # we had a response
                    audioRTrial.addData('audioResp.rt', audioResp.rt)
                audioRTrial.addData('audioResp.started', audioResp.tStartRefresh)
                audioRTrial.addData('audioResp.stopped', audioResp.tStopRefresh)
                # the Routine "AuditoryTrialss" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'audioRTrial'
            
            thisExp.nextEntry()
            
        # completed 1 repeats of 'audioCondLoop'
        
        
        # ------Prepare to start Routine "BreakTime"-------
        continueRoutine = True
        # update component parameters for each repeat
        breakResp.keys = []
        breakResp.rt = []
        _breakResp_allKeys = []
        # keep track of which components have finished
        BreakTimeComponents = [breakText, breakResp]
        for thisComponent in BreakTimeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BreakTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BreakTime"-------
        while continueRoutine:
            # get current time
            t = BreakTimeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BreakTimeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *breakText* updates
            if breakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breakText.frameNStart = frameN  # exact frame index
                breakText.tStart = t  # local t and not account for scr refresh
                breakText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
                breakText.setAutoDraw(True)
            
            # *breakResp* updates
            waitOnFlip = False
            if breakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breakResp.frameNStart = frameN  # exact frame index
                breakResp.tStart = t  # local t and not account for scr refresh
                breakResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breakResp, 'tStartRefresh')  # time at next scr refresh
                breakResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(breakResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(breakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if breakResp.status == STARTED and not waitOnFlip:
                theseKeys = breakResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _breakResp_allKeys.extend(theseKeys)
                if len(_breakResp_allKeys):
                    breakResp.keys = _breakResp_allKeys[-1].name  # just the last key pressed
                    breakResp.rt = _breakResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BreakTimeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BreakTime"-------
        for thisComponent in BreakTimeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskB.addData('breakText.started', breakText.tStartRefresh)
        TaskB.addData('breakText.stopped', breakText.tStopRefresh)
        # the Routine "BreakTime" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsTask2 repeats of 'TaskB'
    
    
    # set up handler to look after randomisation of conditions etc
    TaskC = data.TrialHandler(nReps=nRepsTask3, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TaskC')
    thisExp.addLoop(TaskC)  # add the loop to the experiment
    thisTaskC = TaskC.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTaskC.rgb)
    if thisTaskC != None:
        for paramName in thisTaskC:
            exec('{} = thisTaskC[paramName]'.format(paramName))
    
    for thisTaskC in TaskC:
        currentLoop = TaskC
        # abbreviate parameter names if possible (e.g. rgb = thisTaskC.rgb)
        if thisTaskC != None:
            for paramName in thisTaskC:
                exec('{} = thisTaskC[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "vptScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        vptResp.keys = []
        vptResp.rt = []
        _vptResp_allKeys = []
        # keep track of which components have finished
        vptScreenComponents = [vptInstruct, vptResp]
        for thisComponent in vptScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        vptScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "vptScreen"-------
        while continueRoutine:
            # get current time
            t = vptScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=vptScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *vptInstruct* updates
            if vptInstruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vptInstruct.frameNStart = frameN  # exact frame index
                vptInstruct.tStart = t  # local t and not account for scr refresh
                vptInstruct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vptInstruct, 'tStartRefresh')  # time at next scr refresh
                vptInstruct.setAutoDraw(True)
            
            # *vptResp* updates
            waitOnFlip = False
            if vptResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vptResp.frameNStart = frameN  # exact frame index
                vptResp.tStart = t  # local t and not account for scr refresh
                vptResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vptResp, 'tStartRefresh')  # time at next scr refresh
                vptResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(vptResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(vptResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if vptResp.status == STARTED and not waitOnFlip:
                theseKeys = vptResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _vptResp_allKeys.extend(theseKeys)
                if len(_vptResp_allKeys):
                    vptResp.keys = _vptResp_allKeys[-1].name  # just the last key pressed
                    vptResp.rt = _vptResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in vptScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "vptScreen"-------
        for thisComponent in vptScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskC.addData('vptInstruct.started', vptInstruct.tStartRefresh)
        TaskC.addData('vptInstruct.stopped', vptInstruct.tStopRefresh)
        # the Routine "vptScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "PracticeScreen_1"-------
        continueRoutine = True
        # update component parameters for each repeat
        PracticeScResp.keys = []
        PracticeScResp.rt = []
        _PracticeScResp_allKeys = []
        # keep track of which components have finished
        PracticeScreen_1Components = [PracticeInstruction, PracticeScResp]
        for thisComponent in PracticeScreen_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeScreen_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeScreen_1"-------
        while continueRoutine:
            # get current time
            t = PracticeScreen_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeScreen_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PracticeInstruction* updates
            if PracticeInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeInstruction.frameNStart = frameN  # exact frame index
                PracticeInstruction.tStart = t  # local t and not account for scr refresh
                PracticeInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeInstruction, 'tStartRefresh')  # time at next scr refresh
                PracticeInstruction.setAutoDraw(True)
            
            # *PracticeScResp* updates
            waitOnFlip = False
            if PracticeScResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeScResp.frameNStart = frameN  # exact frame index
                PracticeScResp.tStart = t  # local t and not account for scr refresh
                PracticeScResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeScResp, 'tStartRefresh')  # time at next scr refresh
                PracticeScResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracticeScResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracticeScResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracticeScResp.status == STARTED and not waitOnFlip:
                theseKeys = PracticeScResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _PracticeScResp_allKeys.extend(theseKeys)
                if len(_PracticeScResp_allKeys):
                    PracticeScResp.keys = _PracticeScResp_allKeys[-1].name  # just the last key pressed
                    PracticeScResp.rt = _PracticeScResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeScreen_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeScreen_1"-------
        for thisComponent in PracticeScreen_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskC.addData('PracticeInstruction.started', PracticeInstruction.tStartRefresh)
        TaskC.addData('PracticeInstruction.stopped', PracticeInstruction.tStopRefresh)
        # the Routine "PracticeScreen_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        vptLoopPrac = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('practiceVPT.xlsx'),
            seed=None, name='vptLoopPrac')
        thisExp.addLoop(vptLoopPrac)  # add the loop to the experiment
        thisVptLoopPrac = vptLoopPrac.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVptLoopPrac.rgb)
        if thisVptLoopPrac != None:
            for paramName in thisVptLoopPrac:
                exec('{} = thisVptLoopPrac[paramName]'.format(paramName))
        
        for thisVptLoopPrac in vptLoopPrac:
            currentLoop = vptLoopPrac
            # abbreviate parameter names if possible (e.g. rgb = thisVptLoopPrac.rgb)
            if thisVptLoopPrac != None:
                for paramName in thisVptLoopPrac:
                    exec('{} = thisVptLoopPrac[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "patternGrid"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            patternGrid = createGrid(rows, cols, tiles)
            drawGrid(patternGrid, True)
            # keep track of which components have finished
            patternGridComponents = [staticText]
            for thisComponent in patternGridComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            patternGridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "patternGrid"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = patternGridClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=patternGridClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *staticText* updates
                if staticText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    staticText.frameNStart = frameN  # exact frame index
                    staticText.tStart = t  # local t and not account for scr refresh
                    staticText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(staticText, 'tStartRefresh')  # time at next scr refresh
                    staticText.setAutoDraw(True)
                if staticText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > staticText.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        staticText.tStop = t  # not accounting for scr refresh
                        staticText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(staticText, 'tStopRefresh')  # time at next scr refresh
                        staticText.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in patternGridComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "patternGrid"-------
            for thisComponent in patternGridComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            drawGrid(patternGrid, False)
            vptLoopPrac.addData('staticText.started', staticText.tStartRefresh)
            vptLoopPrac.addData('staticText.stopped', staticText.tStopRefresh)
            
            # ------Prepare to start Routine "Blank1000"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank1000Components = [blankText]
            for thisComponent in Blank1000Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank1000Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank1000"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank1000Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank1000Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blankText* updates
                if blankText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blankText.frameNStart = frameN  # exact frame index
                    blankText.tStart = t  # local t and not account for scr refresh
                    blankText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blankText, 'tStartRefresh')  # time at next scr refresh
                    blankText.setAutoDraw(True)
                if blankText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blankText.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        blankText.tStop = t  # not accounting for scr refresh
                        blankText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blankText, 'tStopRefresh')  # time at next scr refresh
                        blankText.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank1000Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank1000"-------
            for thisComponent in Blank1000Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            vptLoopPrac.addData('blankText.started', blankText.tStartRefresh)
            vptLoopPrac.addData('blankText.stopped', blankText.tStopRefresh)
            
            # ------Prepare to start Routine "respGridPrac"-------
            continueRoutine = True
            # update component parameters for each repeat
            respGrid = createGrid(rows, cols, tiles, True)
            correct = False
            drawGrid(respGrid, True)
            mouseDown = False
            # setup some python lists for storing info about the respMousePrac
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            respGridPracComponents = [respMousePrac, imagePrac]
            for thisComponent in respGridPracComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            respGridPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "respGridPrac"-------
            while continueRoutine:
                # get current time
                t = respGridPracClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=respGridPracClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                currentTile = 0
                patternTile = 0
                
                for tileN in range(len(respGrid)):
                    # Get clicked tile and corresponding pattern tile
                    currentTile = respGrid[tileN]
                    patternTile = patternGrid[tileN]
                    
                    if respMousePrac.isPressedIn(currentTile) and currentTile.fillColor == white and not mouseDown:
                        respGrid[tileN].fillColor = black
                        mouseDown = True
                
                    elif respMousePrac.isPressedIn(currentTile) and currentTile.fillColor == black and not mouseDown:
                        respGrid[tileN].fillColor = white
                        mouseDown = True
                    # has mouse button been released?
                    if not respMousePrac.getPressed()[0] == 1:
                        mouseDown = False
                
                if respMousePrac.isPressedIn(imagePrac):
                    # compare grids
                    correct = compareGrid(respGrid, patternGrid)
                    # save result
                    thisExp.addData("correct", correct)
                    
                    if not correct:
                        thisExp.addData("correct", correct)
                        continueRoutine = False
                    
                    # End the trial
                    continueRoutine = False
                
                # *imagePrac* updates
                if imagePrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    imagePrac.frameNStart = frameN  # exact frame index
                    imagePrac.tStart = t  # local t and not account for scr refresh
                    imagePrac.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(imagePrac, 'tStartRefresh')  # time at next scr refresh
                    imagePrac.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in respGridPracComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "respGridPrac"-------
            for thisComponent in respGridPracComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            drawGrid(respGrid, False)
            # store data for vptLoopPrac (TrialHandler)
            x, y = respMousePrac.getPos()
            buttons = respMousePrac.getPressed()
            vptLoopPrac.addData('respMousePrac.x', x)
            vptLoopPrac.addData('respMousePrac.y', y)
            vptLoopPrac.addData('respMousePrac.leftButton', buttons[0])
            vptLoopPrac.addData('respMousePrac.midButton', buttons[1])
            vptLoopPrac.addData('respMousePrac.rightButton', buttons[2])
            vptLoopPrac.addData('respMousePrac.started', respMousePrac.tStart)
            vptLoopPrac.addData('respMousePrac.stopped', respMousePrac.tStop)
            vptLoopPrac.addData('imagePrac.started', imagePrac.tStartRefresh)
            vptLoopPrac.addData('imagePrac.stopped', imagePrac.tStopRefresh)
            # the Routine "respGridPrac" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "vptFeedback"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            fb = "You were incorrect."
            if correct == True:
                fb = "You were correct!"
            vptTEXT.setText(fb)
            # keep track of which components have finished
            vptFeedbackComponents = [vptTEXT]
            for thisComponent in vptFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            vptFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "vptFeedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = vptFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=vptFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *vptTEXT* updates
                if vptTEXT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vptTEXT.frameNStart = frameN  # exact frame index
                    vptTEXT.tStart = t  # local t and not account for scr refresh
                    vptTEXT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vptTEXT, 'tStartRefresh')  # time at next scr refresh
                    vptTEXT.setAutoDraw(True)
                if vptTEXT.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > vptTEXT.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        vptTEXT.tStop = t  # not accounting for scr refresh
                        vptTEXT.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(vptTEXT, 'tStopRefresh')  # time at next scr refresh
                        vptTEXT.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in vptFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "vptFeedback"-------
            for thisComponent in vptFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            vptLoopPrac.addData('vptTEXT.started', vptTEXT.tStartRefresh)
            vptLoopPrac.addData('vptTEXT.stopped', vptTEXT.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'vptLoopPrac'
        
        
        # ------Prepare to start Routine "BeginTrialScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        beginResp.keys = []
        beginResp.rt = []
        _beginResp_allKeys = []
        # keep track of which components have finished
        BeginTrialScreenComponents = [beginTrialText, beginResp]
        for thisComponent in BeginTrialScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BeginTrialScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BeginTrialScreen"-------
        while continueRoutine:
            # get current time
            t = BeginTrialScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BeginTrialScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *beginTrialText* updates
            if beginTrialText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beginTrialText.frameNStart = frameN  # exact frame index
                beginTrialText.tStart = t  # local t and not account for scr refresh
                beginTrialText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beginTrialText, 'tStartRefresh')  # time at next scr refresh
                beginTrialText.setAutoDraw(True)
            
            # *beginResp* updates
            waitOnFlip = False
            if beginResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beginResp.frameNStart = frameN  # exact frame index
                beginResp.tStart = t  # local t and not account for scr refresh
                beginResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beginResp, 'tStartRefresh')  # time at next scr refresh
                beginResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(beginResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(beginResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if beginResp.status == STARTED and not waitOnFlip:
                theseKeys = beginResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _beginResp_allKeys.extend(theseKeys)
                if len(_beginResp_allKeys):
                    beginResp.keys = _beginResp_allKeys[-1].name  # just the last key pressed
                    beginResp.rt = _beginResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BeginTrialScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BeginTrialScreen"-------
        for thisComponent in BeginTrialScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskC.addData('beginTrialText.started', beginTrialText.tStartRefresh)
        TaskC.addData('beginTrialText.stopped', beginTrialText.tStopRefresh)
        # the Routine "BeginTrialScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        conditionLoop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('condsLoop.xlsx'),
            seed=None, name='conditionLoop')
        thisExp.addLoop(conditionLoop)  # add the loop to the experiment
        thisConditionLoop = conditionLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisConditionLoop.rgb)
        if thisConditionLoop != None:
            for paramName in thisConditionLoop:
                exec('{} = thisConditionLoop[paramName]'.format(paramName))
        
        for thisConditionLoop in conditionLoop:
            currentLoop = conditionLoop
            # abbreviate parameter names if possible (e.g. rgb = thisConditionLoop.rgb)
            if thisConditionLoop != None:
                for paramName in thisConditionLoop:
                    exec('{} = thisConditionLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "counterRoutine"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            totalWrong = 0
            readyText.setText(readyMsg)
            # keep track of which components have finished
            counterRoutineComponents = [readyText]
            for thisComponent in counterRoutineComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            counterRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "counterRoutine"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = counterRoutineClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=counterRoutineClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *readyText* updates
                if readyText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    readyText.frameNStart = frameN  # exact frame index
                    readyText.tStart = t  # local t and not account for scr refresh
                    readyText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(readyText, 'tStartRefresh')  # time at next scr refresh
                    readyText.setAutoDraw(True)
                if readyText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > readyText.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        readyText.tStop = t  # not accounting for scr refresh
                        readyText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(readyText, 'tStopRefresh')  # time at next scr refresh
                        readyText.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in counterRoutineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "counterRoutine"-------
            for thisComponent in counterRoutineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            conditionLoop.addData('readyText.started', readyText.tStartRefresh)
            conditionLoop.addData('readyText.stopped', readyText.tStopRefresh)
            
            # set up handler to look after randomisation of conditions etc
            trials = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(sheet),
                seed=None, name='trials')
            thisExp.addLoop(trials)  # add the loop to the experiment
            thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            for thisTrial in trials:
                currentLoop = trials
                # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                if thisTrial != None:
                    for paramName in thisTrial:
                        exec('{} = thisTrial[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "patternGrid"-------
                continueRoutine = True
                routineTimer.add(2.000000)
                # update component parameters for each repeat
                patternGrid = createGrid(rows, cols, tiles)
                drawGrid(patternGrid, True)
                # keep track of which components have finished
                patternGridComponents = [staticText]
                for thisComponent in patternGridComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                patternGridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "patternGrid"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = patternGridClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=patternGridClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *staticText* updates
                    if staticText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        staticText.frameNStart = frameN  # exact frame index
                        staticText.tStart = t  # local t and not account for scr refresh
                        staticText.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(staticText, 'tStartRefresh')  # time at next scr refresh
                        staticText.setAutoDraw(True)
                    if staticText.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > staticText.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            staticText.tStop = t  # not accounting for scr refresh
                            staticText.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(staticText, 'tStopRefresh')  # time at next scr refresh
                            staticText.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in patternGridComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "patternGrid"-------
                for thisComponent in patternGridComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                drawGrid(patternGrid, False)
                trials.addData('staticText.started', staticText.tStartRefresh)
                trials.addData('staticText.stopped', staticText.tStopRefresh)
                
                # ------Prepare to start Routine "Blank1000"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                # keep track of which components have finished
                Blank1000Components = [blankText]
                for thisComponent in Blank1000Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                Blank1000Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Blank1000"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = Blank1000Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=Blank1000Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blankText* updates
                    if blankText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blankText.frameNStart = frameN  # exact frame index
                        blankText.tStart = t  # local t and not account for scr refresh
                        blankText.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blankText, 'tStartRefresh')  # time at next scr refresh
                        blankText.setAutoDraw(True)
                    if blankText.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blankText.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            blankText.tStop = t  # not accounting for scr refresh
                            blankText.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(blankText, 'tStopRefresh')  # time at next scr refresh
                            blankText.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Blank1000Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Blank1000"-------
                for thisComponent in Blank1000Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials.addData('blankText.started', blankText.tStartRefresh)
                trials.addData('blankText.stopped', blankText.tStopRefresh)
                
                # ------Prepare to start Routine "responseGrid"-------
                continueRoutine = True
                # update component parameters for each repeat
                respGrid = createGrid(rows, cols, tiles, True)
                correct = False
                drawGrid(respGrid, True)
                mouseDown = False
                # setup some python lists for storing info about the respMouse
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                responseGridComponents = [respMouse, image]
                for thisComponent in responseGridComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                responseGridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "responseGrid"-------
                while continueRoutine:
                    # get current time
                    t = responseGridClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=responseGridClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    currentTile = 0
                    patternTile = 0
                    
                    for tileN in range(len(respGrid)):
                        # Get clicked tile and corresponding pattern tile
                        currentTile = respGrid[tileN]
                        patternTile = patternGrid[tileN]
                        
                        if respMouse.isPressedIn(currentTile) and currentTile.fillColor == white and not mouseDown:
                            respGrid[tileN].fillColor = black
                            mouseDown = True
                    
                        elif respMouse.isPressedIn(currentTile) and currentTile.fillColor == black and not mouseDown:
                            respGrid[tileN].fillColor = white
                            mouseDown = True
                        # has mouse button been released?
                        if not respMouse.getPressed()[0] == 1:
                            mouseDown = False
                    
                    if respMouse.isPressedIn(image):
                        # compare grids
                        correct = compareGrid(respGrid, patternGrid)
                        # save result
                        thisExp.addData("vptCorrect", correct)
                        
                        if not correct:
                            totalWrong += 1
                            
                        if totalWrong >= 2:
                            continueRoutine = False
                            trials.finished = True
                            conditionLoop.finished = True
                        
                        # End the trial
                        continueRoutine = False
                    
                    # *image* updates
                    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image.frameNStart = frameN  # exact frame index
                        image.tStart = t  # local t and not account for scr refresh
                        image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                        image.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in responseGridComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "responseGrid"-------
                for thisComponent in responseGridComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                drawGrid(respGrid, False)
                # store data for trials (TrialHandler)
                x, y = respMouse.getPos()
                buttons = respMouse.getPressed()
                trials.addData('respMouse.x', x)
                trials.addData('respMouse.y', y)
                trials.addData('respMouse.leftButton', buttons[0])
                trials.addData('respMouse.midButton', buttons[1])
                trials.addData('respMouse.rightButton', buttons[2])
                trials.addData('respMouse.started', respMouse.tStart)
                trials.addData('respMouse.stopped', respMouse.tStop)
                trials.addData('image.started', image.tStartRefresh)
                trials.addData('image.stopped', image.tStopRefresh)
                # the Routine "responseGrid" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'trials'
            
            thisExp.nextEntry()
            
        # completed 1 repeats of 'conditionLoop'
        
        
        # ------Prepare to start Routine "BreakTime"-------
        continueRoutine = True
        # update component parameters for each repeat
        breakResp.keys = []
        breakResp.rt = []
        _breakResp_allKeys = []
        # keep track of which components have finished
        BreakTimeComponents = [breakText, breakResp]
        for thisComponent in BreakTimeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BreakTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BreakTime"-------
        while continueRoutine:
            # get current time
            t = BreakTimeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BreakTimeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *breakText* updates
            if breakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breakText.frameNStart = frameN  # exact frame index
                breakText.tStart = t  # local t and not account for scr refresh
                breakText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
                breakText.setAutoDraw(True)
            
            # *breakResp* updates
            waitOnFlip = False
            if breakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breakResp.frameNStart = frameN  # exact frame index
                breakResp.tStart = t  # local t and not account for scr refresh
                breakResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breakResp, 'tStartRefresh')  # time at next scr refresh
                breakResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(breakResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(breakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if breakResp.status == STARTED and not waitOnFlip:
                theseKeys = breakResp.getKeys(keyList=['o', 'space'], waitRelease=False)
                _breakResp_allKeys.extend(theseKeys)
                if len(_breakResp_allKeys):
                    breakResp.keys = _breakResp_allKeys[-1].name  # just the last key pressed
                    breakResp.rt = _breakResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BreakTimeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BreakTime"-------
        for thisComponent in BreakTimeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TaskC.addData('breakText.started', breakText.tStartRefresh)
        TaskC.addData('breakText.stopped', breakText.tStopRefresh)
        # the Routine "BreakTime" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsTask3 repeats of 'TaskC'
    
# completed 1 repeats of 'TaskOrderCond'


# ------Prepare to start Routine "ENDING"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
ENDINGComponents = [ENDtext]
for thisComponent in ENDINGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ENDINGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ENDING"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ENDINGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ENDINGClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ENDtext* updates
    if ENDtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ENDtext.frameNStart = frameN  # exact frame index
        ENDtext.tStart = t  # local t and not account for scr refresh
        ENDtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ENDtext, 'tStartRefresh')  # time at next scr refresh
        ENDtext.setAutoDraw(True)
    if ENDtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ENDtext.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            ENDtext.tStop = t  # not accounting for scr refresh
            ENDtext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ENDtext, 'tStopRefresh')  # time at next scr refresh
            ENDtext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDINGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ENDING"-------
for thisComponent in ENDINGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ENDtext.started', ENDtext.tStartRefresh)
thisExp.addData('ENDtext.stopped', ENDtext.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
