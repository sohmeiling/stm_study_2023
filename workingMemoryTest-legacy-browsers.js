/************************** 
 * Workingmemorytest Test *
 **************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'workingMemoryTest';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001', 'group': ['ACB', 'BCA', 'BAC', 'CBA', 'CAB']};

// Start code blocks for 'Before Experiment'
var white = new util.Color("white")
var black = new util.Color("black")
var lightgrey = new util.Color("lightgrey")

Array.prototype.append = [].push;
var win = psychoJS.window

var _pj;

function _pj_snippets(container) {
    function in_es6(left, right) {
        if (((right instanceof Array) || ((typeof right) === "string"))) {
            return (right.indexOf(left) > (- 1));
        } else {
            if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                return right.has(left);
            } else {
                return (left in right);
            }
        }
    }
    container["in_es6"] = in_es6;
    return container;
}
_pj = {};
_pj_snippets(_pj);

var tileSize;
var counter;
var xPos;
var yPos;
var tileColors;
var grid;
function createGrid(rows, cols, tiles, responseGrid = false) {
    var counter, grid, tileCol, tileColors, tileSize, xPos, yPos;
    tileSize = 100;
    counter = 0;
    xPos = (0 - ((rows * tileSize) / 2));
    yPos = (0 + ((cols * tileSize) / 2));
    tileColors = {[0]: null, [1]: white, [2]: black};
    grid = [];
    for (var i = 0, _pj_a = rows; (i < _pj_a); i += 1) {
        for (var j = 0, _pj_b = cols; (j < _pj_b); j += 1) {
            tileCol = tileColors[tiles[counter]];
            counter += 1;
            if ((tileCol !== null)) {
                if ((responseGrid === true)) {
                    tileCol = tileColors[1];
                }
                grid.append(new visual.Rect({"win": win, "width": 1, "height": 1, "units": "pix", "fillColor": tileCol, "size": tileSize, "pos": [xPos, yPos], "lineColor": black}));
            }
            xPos += tileSize;
        }
        yPos -= tileSize;
        xPos = (0 - ((rows * tileSize) / 2));
    }
    return grid;
}

function drawGrid(grid, onOff) {
    for (var i, _pj_c = 0, _pj_a = grid, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        i.setAutoDraw(onOff);
    }
}

var testCols;
function compareGrid(g1, g2) {
    var testCols;
    testCols = [];
    for (var tile = 0, _pj_a = g1.length; (tile < _pj_a); tile += 1) {
        if ((g1[tile].fillColor === g2[tile].fillColor)) {
            testCols.append(true);
        } else {
            testCols.append(false);
        }
    }
    return (! _pj.in_es6(false, testCols));
}

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
flowScheduler.add(warningMacRoutineBegin());
flowScheduler.add(warningMacRoutineEachFrame());
flowScheduler.add(warningMacRoutineEnd());
flowScheduler.add(PracticeScreen_1RoutineBegin());
flowScheduler.add(PracticeScreen_1RoutineEachFrame());
flowScheduler.add(PracticeScreen_1RoutineEnd());
const typingLoopPractLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(typingLoopPractLoopBegin, typingLoopPractLoopScheduler);
flowScheduler.add(typingLoopPractLoopScheduler);
flowScheduler.add(typingLoopPractLoopEnd);
flowScheduler.add(BeginTrialScreenRoutineBegin());
flowScheduler.add(BeginTrialScreenRoutineEachFrame());
flowScheduler.add(BeginTrialScreenRoutineEnd());
const typingRTrialLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(typingRTrialLoopBegin, typingRTrialLoopScheduler);
flowScheduler.add(typingRTrialLoopScheduler);
flowScheduler.add(typingRTrialLoopEnd);
flowScheduler.add(BreakTimeRoutineBegin());
flowScheduler.add(BreakTimeRoutineEachFrame());
flowScheduler.add(BreakTimeRoutineEnd());
const TaskOrderCondLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TaskOrderCondLoopBegin, TaskOrderCondLoopScheduler);
flowScheduler.add(TaskOrderCondLoopScheduler);
flowScheduler.add(TaskOrderCondLoopEnd);
flowScheduler.add(ENDINGRoutineBegin());
flowScheduler.add(ENDINGRoutineEachFrame());
flowScheduler.add(ENDINGRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Audio/75836.mp3', 'path': 'Audio/75836.mp3'},
    {'name': 'Audio/64738.mp3', 'path': 'Audio/64738.mp3'},
    {'name': 'Audio/58132647.mp3', 'path': 'Audio/58132647.mp3'},
    {'name': 'Audio/6352.mp3', 'path': 'Audio/6352.mp3'},
    {'name': 'multiplOne.xlsx', 'path': 'multiplOne.xlsx'},
    {'name': 'Audio/275863194.mp3', 'path': 'Audio/275863194.mp3'},
    {'name': 'conditionsCBA.xlsx', 'path': 'conditionsCBA.xlsx'},
    {'name': 'nineWAIS.xlsx', 'path': 'nineWAIS.xlsx'},
    {'name': 'Audio/38296174.mp3', 'path': 'Audio/38296174.mp3'},
    {'name': 'conditionsABC.xlsx', 'path': 'conditionsABC.xlsx'},
    {'name': 'Audio/713942568.mp3', 'path': 'Audio/713942568.mp3'},
    {'name': 'sevenWAIS.xlsx', 'path': 'sevenWAIS.xlsx'},
    {'name': 'nineAudio.xlsx', 'path': 'nineAudio.xlsx'},
    {'name': 'Audio/682594316.mp3', 'path': 'Audio/682594316.mp3'},
    {'name': 'Audio/157.mp3', 'path': 'Audio/157.mp3'},
    {'name': 'Audio/sample.mp3', 'path': 'Audio/sample.mp3'},
    {'name': 'continueButton.png', 'path': 'continueButton.png'},
    {'name': 'sixAudio.xlsx', 'path': 'sixAudio.xlsx'},
    {'name': 'Audio/7286.mp3', 'path': 'Audio/7286.mp3'},
    {'name': 'multiplyConds.xlsx', 'path': 'multiplyConds.xlsx'},
    {'name': 'threeAudio.xlsx', 'path': 'threeAudio.xlsx'},
    {'name': 'threeWAIS.xlsx', 'path': 'threeWAIS.xlsx'},
    {'name': 'Audio/582.mp3', 'path': 'Audio/582.mp3'},
    {'name': 'blockEight.xlsx', 'path': 'blockEight.xlsx'},
    {'name': 'blockTen.xlsx', 'path': 'blockTen.xlsx'},
    {'name': 'eightAudio.xlsx', 'path': 'eightAudio.xlsx'},
    {'name': 'Audio/59281.mp3', 'path': 'Audio/59281.mp3'},
    {'name': 'eightWAIS.xlsx', 'path': 'eightWAIS.xlsx'},
    {'name': 'Audio/4179386.mp3', 'path': 'Audio/4179386.mp3'},
    {'name': 'fourAudio.xlsx', 'path': 'fourAudio.xlsx'},
    {'name': 'blockThirteen.xlsx', 'path': 'blockThirteen.xlsx'},
    {'name': 'Audio/9184.mp3', 'path': 'Audio/9184.mp3'},
    {'name': 'blockTwelve.xlsx', 'path': 'blockTwelve.xlsx'},
    {'name': 'blockSeven.xlsx', 'path': 'blockSeven.xlsx'},
    {'name': 'Audio/46.mp3', 'path': 'Audio/46.mp3'},
    {'name': 'blockFour.xlsx', 'path': 'blockFour.xlsx'},
    {'name': 'Audio/396172.mp3', 'path': 'Audio/396172.mp3'},
    {'name': 'fiveWAIS.xlsx', 'path': 'fiveWAIS.xlsx'},
    {'name': 'Audio/42731.mp3', 'path': 'Audio/42731.mp3'},
    {'name': 'fiveAudio.xlsx', 'path': 'fiveAudio.xlsx'},
    {'name': 'multiplicationPract.xlsx', 'path': 'multiplicationPract.xlsx'},
    {'name': 'twoAudio.xlsx', 'path': 'twoAudio.xlsx'},
    {'name': 'Audio/75241739.mp3', 'path': 'Audio/75241739.mp3'},
    {'name': 'conditionsCAB.xlsx', 'path': 'conditionsCAB.xlsx'},
    {'name': 'Audio/6917428.mp3', 'path': 'Audio/6917428.mp3'},
    {'name': 'blockFifteen.xlsx', 'path': 'blockFifteen.xlsx'},
    {'name': 'blockThree.xlsx', 'path': 'blockThree.xlsx'},
    {'name': 'typingTest_stimuli.xlsx', 'path': 'typingTest_stimuli.xlsx'},
    {'name': 'conditionsACB.xlsx', 'path': 'conditionsACB.xlsx'},
    {'name': 'Audio/82.mp3', 'path': 'Audio/82.mp3'},
    {'name': 'Audio/8241973.mp3', 'path': 'Audio/8241973.mp3'},
    {'name': 'Audio/53827164.mp3', 'path': 'Audio/53827164.mp3'},
    {'name': 'Audio/6439.mp3', 'path': 'Audio/6439.mp3'},
    {'name': 'practiceVPT.xlsx', 'path': 'practiceVPT.xlsx'},
    {'name': 'Audio/392487.mp3', 'path': 'Audio/392487.mp3'},
    {'name': 'multiplTwo.xlsx', 'path': 'multiplTwo.xlsx'},
    {'name': 'sevenAudio.xlsx', 'path': 'sevenAudio.xlsx'},
    {'name': 'typingPractice.xlsx', 'path': 'typingPractice.xlsx'},
    {'name': 'auditoryPract.xlsx', 'path': 'auditoryPract.xlsx'},
    {'name': 'blockFive.xlsx', 'path': 'blockFive.xlsx'},
    {'name': 'condsLoop.xlsx', 'path': 'condsLoop.xlsx'},
    {'name': 'Audio/594631.mp3', 'path': 'Audio/594631.mp3'},
    {'name': 'WAIS.xlsx', 'path': 'WAIS.xlsx'},
    {'name': 'Audio/397.mp3', 'path': 'Audio/397.mp3'},
    {'name': 'blockTwo.xlsx', 'path': 'blockTwo.xlsx'},
    {'name': 'Audio/97.mp3', 'path': 'Audio/97.mp3'},
    {'name': 'blockFourteen.xlsx', 'path': 'blockFourteen.xlsx'},
    {'name': 'Audio/911.mp3', 'path': 'Audio/911.mp3'},
    {'name': 'Audio/2814367.mp3', 'path': 'Audio/2814367.mp3'},
    {'name': 'Audio/142963758.mp3', 'path': 'Audio/142963758.mp3'},
    {'name': 'sixWAIS.xlsx', 'path': 'sixWAIS.xlsx'},
    {'name': 'Audio/694.mp3', 'path': 'Audio/694.mp3'},
    {'name': 'conditionsBAC.xlsx', 'path': 'conditionsBAC.xlsx'},
    {'name': 'Audio/123.mp3', 'path': 'Audio/123.mp3'},
    {'name': 'twoWAIS.xlsx', 'path': 'twoWAIS.xlsx'},
    {'name': 'blockEleven.xlsx', 'path': 'blockEleven.xlsx'},
    {'name': 'blockSix.xlsx', 'path': 'blockSix.xlsx'},
    {'name': 'Audio/619473.mp3', 'path': 'Audio/619473.mp3'},
    {'name': 'Audio/321.mp3', 'path': 'Audio/321.mp3'},
    {'name': 'Egner.xlsx', 'path': 'Egner.xlsx'},
    {'name': 'conditionsBCA.xlsx', 'path': 'conditionsBCA.xlsx'},
    {'name': 'blockNine.xlsx', 'path': 'blockNine.xlsx'},
    {'name': 'fourWAIS.xlsx', 'path': 'fourWAIS.xlsx'},
    {'name': 'Audio/63.mp3', 'path': 'Audio/63.mp3'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://nottinghammy.asia.qualtrics.com/jfe/form/SV_5mylepiD5LFyRjU', 'https://nottinghammy.asia.qualtrics.com/jfe/form/SV_8pulKfjmsnk7pPw');

  return Scheduler.Event.NEXT;
}


var WelcomeScreenClock;
var event;
var thisExp;
var win;
var welcomeTyping;
var welcomeResp;
var warningMacClock;
var text_41;
var MACresp;
var PracticeScreen_1Clock;
var PracticeInstruction;
var PracticeScResp;
var Blank500Clock;
var blankEmpty;
var TypingPracClock;
var typeText;
var inputText;
var contText;
var TypingFeedbackClock;
var msg;
var rtFeedback;
var BeginTrialScreenClock;
var beginTrialText;
var beginResp;
var BreakTimeClock;
var breakText;
var breakResp;
var MultiplyScreenClock;
var practMultText;
var multiplyResp;
var MultiplyPracClock;
var inputText2;
var productText;
var contText2;
var MultiplyFeedbackClock;
var message;
var mulFBText;
var READYClock;
var text_1;
var key_resp1;
var AdjustSoundInstClock;
var volumeText;
var volInstruResp;
var AdjustSoundVolClock;
var sampleSoundVol;
var sampleResp;
var sampleText;
var AuditoryScreenClock;
var pracAuditoryText;
var AuditoryResp;
var Audio_PlayClock;
var soundPresentation;
var text1;
var crossFix1;
var AuditoryPracticeSetClock;
var inputText4;
var contText4;
var RECALLtext2;
var AuditoryFeedbackClock;
var Feedback;
var AudioFBText;
var countingCWClock;
var AuditoryTrialssClock;
var inputText3;
var contText3;
var RECALLtext;
var audio_PlayWAISClock;
var WAIS_sound;
var reminderTextSound;
var textFIXsound;
var audioTrial_WAISClock;
var inputText9;
var continuingText;
var recallingTime;
var vptScreenClock;
var vptInstruct;
var vptResp;
var patternGridClock;
var staticText;
var Blank1000Clock;
var blankText;
var respGridPracClock;
var respMousePrac;
var imagePrac;
var vptFeedbackClock;
var vptTEXT;
var counterRoutineClock;
var readyText;
var responseGridClock;
var respMouse;
var image;
var ENDINGClock;
var ENDtext;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  event=psychoJS.eventManager;
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  welcomeTyping = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeTyping',
    text: '**INSTRUCTIONS**\n\nWelcome to the typing task!\n\nIn this task, you will see a number presented on the screen. Please type in the number as quickly as you can. \n\nAfter typing the number, you will press RETURN to continue to the next number.\n\nIf you make any typing errors, you can use BACKSPACE to correct them.\n\nPlease note that you can only use the numbers on top of the keyboard.\n\nPress SPACE to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  welcomeResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "warningMac"
  warningMacClock = new util.Clock();
  text_41 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_41',
    text: "**ATTENTION MAC USERS**\n\nIf you are running this experiment on Safari, you will have to enable Auto-Play on this website.\n\n1) Press ESC once to access toolbar\n\n2) Click on Safari\n\n3) Go to Preferences\n\n4) Go to Websites\n\n5) Go to Auto-Play\n\n6) For pavlovia.org select 'Allow All Auto-Play' option\n\n\nPress SPACE to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  MACresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PracticeScreen_1"
  PracticeScreen_1Clock = new util.Clock();
  PracticeInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeInstruction',
    text: 'We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  PracticeScResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  blankEmpty = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankEmpty',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TypingPrac"
  TypingPracClock = new util.Clock();
  typeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'typeText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  inputText = new visual.TextStim({
    win: psychoJS.window,
    name: 'inputText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.498), (- 1.0), 0.004]),  opacity: 1,
    depth: -2.0 
  });
  
  contText = new visual.TextStim({
    win: psychoJS.window,
    name: 'contText',
    text: 'Press RETURN or ENTER to proceed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.137), (- 0.137), (- 0.137)]),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "TypingFeedback"
  TypingFeedbackClock = new util.Clock();
  msg = "";
  
  rtFeedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'rtFeedback',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "BeginTrialScreen"
  BeginTrialScreenClock = new util.Clock();
  beginTrialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginTrialText',
    text: 'You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  beginResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  blankEmpty = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankEmpty',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TypingPrac"
  TypingPracClock = new util.Clock();
  typeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'typeText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  inputText = new visual.TextStim({
    win: psychoJS.window,
    name: 'inputText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.498), (- 1.0), 0.004]),  opacity: 1,
    depth: -2.0 
  });
  
  contText = new visual.TextStim({
    win: psychoJS.window,
    name: 'contText',
    text: 'Press RETURN or ENTER to proceed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.137), (- 0.137), (- 0.137)]),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "BreakTime"
  BreakTimeClock = new util.Clock();
  breakText = new visual.TextStim({
    win: psychoJS.window,
    name: 'breakText',
    text: 'You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: 0.0 
  });
  
  breakResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "MultiplyScreen"
  MultiplyScreenClock = new util.Clock();
  practMultText = new visual.TextStim({
    win: psychoJS.window,
    name: 'practMultText',
    text: '**INSTRUCTIONS**\n\nWelcome to the multiplication task!\n\nIn this task, you will see a multiplication problem presented on the screen. Please type in your answer as quickly as you can. \n\nAfter typing the answer, you will press RETURN to continue to the next problem.\n\nIf you make any typing errors, you can use BACKSPACE to correct them.\n\nPlease note that you can only use the numbers on top of the keypad.\n\nPress SPACE to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  multiplyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PracticeScreen_1"
  PracticeScreen_1Clock = new util.Clock();
  PracticeInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeInstruction',
    text: 'We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  PracticeScResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  blankEmpty = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankEmpty',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "MultiplyPrac"
  MultiplyPracClock = new util.Clock();
  inputText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'inputText2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.498), (- 1.0), 0.004]),  opacity: 1,
    depth: -1.0 
  });
  
  productText = new visual.TextStim({
    win: psychoJS.window,
    name: 'productText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  contText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'contText2',
    text: 'Press RETURN or ENTER to proceed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.137), (- 0.137), (- 0.137)]),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "MultiplyFeedback"
  MultiplyFeedbackClock = new util.Clock();
  message = "";
  
  mulFBText = new visual.TextStim({
    win: psychoJS.window,
    name: 'mulFBText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "BeginTrialScreen"
  BeginTrialScreenClock = new util.Clock();
  beginTrialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginTrialText',
    text: 'You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  beginResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "READY"
  READYClock = new util.Clock();
  text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_1',
    text: 'When you are ready to start, press SPACE to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  blankEmpty = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankEmpty',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "MultiplyPrac"
  MultiplyPracClock = new util.Clock();
  inputText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'inputText2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.498), (- 1.0), 0.004]),  opacity: 1,
    depth: -1.0 
  });
  
  productText = new visual.TextStim({
    win: psychoJS.window,
    name: 'productText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  contText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'contText2',
    text: 'Press RETURN or ENTER to proceed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.137), (- 0.137), (- 0.137)]),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "BreakTime"
  BreakTimeClock = new util.Clock();
  breakText = new visual.TextStim({
    win: psychoJS.window,
    name: 'breakText',
    text: 'You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: 0.0 
  });
  
  breakResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AdjustSoundInst"
  AdjustSoundInstClock = new util.Clock();
  volumeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'volumeText',
    text: '**INSTRUCTIONS**\n\nReminder, please put on your headphone/earphone now if you have not done so.\n\nBefore we start, we will need to adjust the volume of your sound input. \n\nYou will hear an audio playing when you press SPACE. Please adjust the audio to your desired volume. \n\nOnce you are done, press SPACE to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  volInstruResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AdjustSoundVol"
  AdjustSoundVolClock = new util.Clock();
  sampleSoundVol = new sound.Sound({
    win: psychoJS.window,
    value: 'Audio/sample.mp3',
    secs: (- 1),
    });
  sampleSoundVol.setVolume(0.5);
  sampleResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  sampleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'sampleText',
    text: 'Now, you should hear an audio playing. Please adjust your microphone/earphone volume accordingly. \n\nOnce you are done, please press SPACE to continue. [You do not have to wait till the audio finishes.]',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "AuditoryScreen"
  AuditoryScreenClock = new util.Clock();
  pracAuditoryText = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracAuditoryText',
    text: "**INSTRUCTIONS**\n\nWelcome to the listening task!\n\nIn this task, you will hear a series of number presented to you through your earphone. Please remember the numbers in the exact order that they were presented.\n\nFollowing the presentation of audio, you will be asked to type in your response. Please key in the numbers as you hear it. For example, if you hear '3 ... 2 ... 1', key in '321.'\n\nAfter typing the answer, you will press RETURN/ENTER to continue to the next problem. If you make any typing errors, you can use BACKSPACE to correct them.\n\nIf you could not recall the series of numbers presented, take a guess, or press RETURN/ENTER to continue to the next set. When you answer correctly, the span (i.e., the number of digits to recall) increases.\n\nPress SPACE to continue. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  AuditoryResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PracticeScreen_1"
  PracticeScreen_1Clock = new util.Clock();
  PracticeInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeInstruction',
    text: 'We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  PracticeScResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Audio_Play"
  Audio_PlayClock = new util.Clock();
  soundPresentation = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  soundPresentation.setVolume(1);
  text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text1',
    text: 'Audio starts playing.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  crossFix1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'crossFix1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "AuditoryPracticeSet"
  AuditoryPracticeSetClock = new util.Clock();
  inputText4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'inputText4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.498), (- 1.0), 0.004]),  opacity: 1,
    depth: -1.0 
  });
  
  contText4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'contText4',
    text: 'Press RETURN or ENTER to proceed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.137), (- 0.137), (- 0.137)]),  opacity: 1,
    depth: -2.0 
  });
  
  RECALLtext2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RECALLtext2',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "AuditoryFeedback"
  AuditoryFeedbackClock = new util.Clock();
  Feedback = "";
  
  AudioFBText = new visual.TextStim({
    win: psychoJS.window,
    name: 'AudioFBText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "BeginTrialScreen"
  BeginTrialScreenClock = new util.Clock();
  beginTrialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginTrialText',
    text: 'You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  beginResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "countingCW"
  countingCWClock = new util.Clock();
  // Initialize components for Routine "Audio_Play"
  Audio_PlayClock = new util.Clock();
  soundPresentation = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  soundPresentation.setVolume(1);
  text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text1',
    text: 'Audio starts playing.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  crossFix1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'crossFix1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "AuditoryTrialss"
  AuditoryTrialssClock = new util.Clock();
  inputText3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'inputText3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.498), (- 1.0), 0.004]),  opacity: 1,
    depth: -1.0 
  });
  
  contText3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'contText3',
    text: 'Press RETURN or ENTER to proceed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.137), (- 0.137), (- 0.137)]),  opacity: 1,
    depth: -2.0 
  });
  
  RECALLtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'RECALLtext',
    text: 'RECALL',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "countingCW"
  countingCWClock = new util.Clock();
  // Initialize components for Routine "audio_PlayWAIS"
  audio_PlayWAISClock = new util.Clock();
  WAIS_sound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  WAIS_sound.setVolume(1);
  reminderTextSound = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminderTextSound',
    text: 'Audio starts playing.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  textFIXsound = new visual.TextStim({
    win: psychoJS.window,
    name: 'textFIXsound',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "audioTrial_WAIS"
  audioTrial_WAISClock = new util.Clock();
  inputText9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'inputText9',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.498), (- 1.0), 0.004]),  opacity: 1,
    depth: -1.0 
  });
  
  continuingText = new visual.TextStim({
    win: psychoJS.window,
    name: 'continuingText',
    text: 'Press RETURN or ENTER to proceed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 0.137), (- 0.137), (- 0.137)]),  opacity: 1,
    depth: -2.0 
  });
  
  recallingTime = new visual.TextStim({
    win: psychoJS.window,
    name: 'recallingTime',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "BreakTime"
  BreakTimeClock = new util.Clock();
  breakText = new visual.TextStim({
    win: psychoJS.window,
    name: 'breakText',
    text: 'You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: 0.0 
  });
  
  breakResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "vptScreen"
  vptScreenClock = new util.Clock();
  vptInstruct = new visual.TextStim({
    win: psychoJS.window,
    name: 'vptInstruct',
    text: '**INSTRUCTIONS**\n\nWelcome to the memory task!\n\nIn this task, you will see a checkerboard-like grid, with the squares in the grid each randomly colored (in either white or black colors). Please remember the patterns presented.\n\nFollowing the presentation of patterns, you are then shown a blank grid and must reproduce the pattern. You can click on the square to change its color. If you make any clicking errors, you can just click the square again to correct them.\n\nAfter you are done, you will click on the CONTINUE button to continue to the next problem. \n\nIf you could not recall the patterns presented, take a guess, or press CONTINUE to continue to the next set. The difficulty of the set increases with each correct answer.\n\nPress SPACE to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  vptResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PracticeScreen_1"
  PracticeScreen_1Clock = new util.Clock();
  PracticeInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeInstruction',
    text: 'We will start with practice trials. You have THREE practice trials before the real trial.\n\nPlease try your best. \n\nPress SPACE to begin a series of 3 practice trials.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  PracticeScResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "patternGrid"
  patternGridClock = new util.Clock();
  staticText = new visual.TextStim({
    win: psychoJS.window,
    name: 'staticText',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Blank1000"
  Blank1000Clock = new util.Clock();
  blankText = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankText',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "respGridPrac"
  respGridPracClock = new util.Clock();
  respMousePrac = new core.Mouse({
    win: psychoJS.window,
  });
  respMousePrac.mouseClock = new util.Clock();
  imagePrac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagePrac', units : undefined, 
    image : 'continueButton.png', mask : undefined,
    ori : 0, pos : [0, (- 0.35)], size : [0.35, 0.08],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "vptFeedback"
  vptFeedbackClock = new util.Clock();
  vptTEXT = new visual.TextStim({
    win: psychoJS.window,
    name: 'vptTEXT',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "BeginTrialScreen"
  BeginTrialScreenClock = new util.Clock();
  beginTrialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginTrialText',
    text: 'You have completed the practice trials.\n\nPress SPACE to begin the experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  beginResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "counterRoutine"
  counterRoutineClock = new util.Clock();
  readyText = new visual.TextStim({
    win: psychoJS.window,
    name: 'readyText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "patternGrid"
  patternGridClock = new util.Clock();
  staticText = new visual.TextStim({
    win: psychoJS.window,
    name: 'staticText',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Blank1000"
  Blank1000Clock = new util.Clock();
  blankText = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankText',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "responseGrid"
  responseGridClock = new util.Clock();
  respMouse = new core.Mouse({
    win: psychoJS.window,
  });
  respMouse.mouseClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'continueButton.png', mask : undefined,
    ori : 0, pos : [0, (- 0.35)], size : [0.35, 0.08],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "BreakTime"
  BreakTimeClock = new util.Clock();
  breakText = new visual.TextStim({
    win: psychoJS.window,
    name: 'breakText',
    text: 'You have completed a block of trials. Thank you for persevering with the task. \n\nYou deserve a break!\n\nWhen you are ready to continue with the experiment, press SPACE.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: 0.0 
  });
  
  breakResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ENDING"
  ENDINGClock = new util.Clock();
  ENDtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'ENDtext',
    text: 'This is the end of the experiment. Thank you for your time.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _welcomeResp_allKeys;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'WelcomeScreen'-------
    t = 0;
    WelcomeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    welcomeResp.keys = undefined;
    welcomeResp.rt = undefined;
    _welcomeResp_allKeys = [];
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(welcomeTyping);
    WelcomeScreenComponents.push(welcomeResp);
    
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function WelcomeScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'WelcomeScreen'-------
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcomeTyping* updates
    if (t >= 0.0 && welcomeTyping.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeTyping.tStart = t;  // (not accounting for frame time here)
      welcomeTyping.frameNStart = frameN;  // exact frame index
      
      welcomeTyping.setAutoDraw(true);
    }

    
    // *welcomeResp* updates
    if (t >= 0.0 && welcomeResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeResp.tStart = t;  // (not accounting for frame time here)
      welcomeResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcomeResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcomeResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcomeResp.clearEvents(); });
    }

    if (welcomeResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcomeResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _welcomeResp_allKeys = _welcomeResp_allKeys.concat(theseKeys);
      if (_welcomeResp_allKeys.length > 0) {
        welcomeResp.keys = _welcomeResp_allKeys[_welcomeResp_allKeys.length - 1].name;  // just the last key pressed
        welcomeResp.rt = _welcomeResp_allKeys[_welcomeResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'WelcomeScreen'-------
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _MACresp_allKeys;
var warningMacComponents;
function warningMacRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'warningMac'-------
    t = 0;
    warningMacClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    MACresp.keys = undefined;
    MACresp.rt = undefined;
    _MACresp_allKeys = [];
    // keep track of which components have finished
    warningMacComponents = [];
    warningMacComponents.push(text_41);
    warningMacComponents.push(MACresp);
    
    warningMacComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function warningMacRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'warningMac'-------
    // get current time
    t = warningMacClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_41* updates
    if (t >= 0.0 && text_41.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_41.tStart = t;  // (not accounting for frame time here)
      text_41.frameNStart = frameN;  // exact frame index
      
      text_41.setAutoDraw(true);
    }

    
    // *MACresp* updates
    if (t >= 0.0 && MACresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MACresp.tStart = t;  // (not accounting for frame time here)
      MACresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { MACresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { MACresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { MACresp.clearEvents(); });
    }

    if (MACresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = MACresp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _MACresp_allKeys = _MACresp_allKeys.concat(theseKeys);
      if (_MACresp_allKeys.length > 0) {
        MACresp.keys = _MACresp_allKeys[_MACresp_allKeys.length - 1].name;  // just the last key pressed
        MACresp.rt = _MACresp_allKeys[_MACresp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    warningMacComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function warningMacRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'warningMac'-------
    warningMacComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "warningMac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _PracticeScResp_allKeys;
var PracticeScreen_1Components;
function PracticeScreen_1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeScreen_1'-------
    t = 0;
    PracticeScreen_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    PracticeScResp.keys = undefined;
    PracticeScResp.rt = undefined;
    _PracticeScResp_allKeys = [];
    // keep track of which components have finished
    PracticeScreen_1Components = [];
    PracticeScreen_1Components.push(PracticeInstruction);
    PracticeScreen_1Components.push(PracticeScResp);
    
    PracticeScreen_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PracticeScreen_1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeScreen_1'-------
    // get current time
    t = PracticeScreen_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *PracticeInstruction* updates
    if (t >= 0.0 && PracticeInstruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeInstruction.tStart = t;  // (not accounting for frame time here)
      PracticeInstruction.frameNStart = frameN;  // exact frame index
      
      PracticeInstruction.setAutoDraw(true);
    }

    
    // *PracticeScResp* updates
    if (t >= 0.0 && PracticeScResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeScResp.tStart = t;  // (not accounting for frame time here)
      PracticeScResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PracticeScResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PracticeScResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PracticeScResp.clearEvents(); });
    }

    if (PracticeScResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = PracticeScResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _PracticeScResp_allKeys = _PracticeScResp_allKeys.concat(theseKeys);
      if (_PracticeScResp_allKeys.length > 0) {
        PracticeScResp.keys = _PracticeScResp_allKeys[_PracticeScResp_allKeys.length - 1].name;  // just the last key pressed
        PracticeScResp.rt = _PracticeScResp_allKeys[_PracticeScResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PracticeScreen_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeScreen_1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeScreen_1'-------
    PracticeScreen_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "PracticeScreen_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var typingLoopPract;
var currentLoop;
function typingLoopPractLoopBegin(typingLoopPractLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  typingLoopPract = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'typingPractice.xlsx',
    seed: undefined, name: 'typingLoopPract'
  });
  psychoJS.experiment.addLoop(typingLoopPract); // add the loop to the experiment
  currentLoop = typingLoopPract;  // we're now the current loop

  // Schedule all the trials in the trialList:
  typingLoopPract.forEach(function() {
    const snapshot = typingLoopPract.getSnapshot();

    typingLoopPractLoopScheduler.add(importConditions(snapshot));
    typingLoopPractLoopScheduler.add(Blank500RoutineBegin(snapshot));
    typingLoopPractLoopScheduler.add(Blank500RoutineEachFrame(snapshot));
    typingLoopPractLoopScheduler.add(Blank500RoutineEnd(snapshot));
    typingLoopPractLoopScheduler.add(TypingPracRoutineBegin(snapshot));
    typingLoopPractLoopScheduler.add(TypingPracRoutineEachFrame(snapshot));
    typingLoopPractLoopScheduler.add(TypingPracRoutineEnd(snapshot));
    typingLoopPractLoopScheduler.add(TypingFeedbackRoutineBegin(snapshot));
    typingLoopPractLoopScheduler.add(TypingFeedbackRoutineEachFrame(snapshot));
    typingLoopPractLoopScheduler.add(TypingFeedbackRoutineEnd(snapshot));
    typingLoopPractLoopScheduler.add(endLoopIteration(typingLoopPractLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function typingLoopPractLoopEnd() {
  psychoJS.experiment.removeLoop(typingLoopPract);

  return Scheduler.Event.NEXT;
}


var typingRTrial;
function typingRTrialLoopBegin(typingRTrialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  typingRTrial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'typingTest_stimuli.xlsx',
    seed: undefined, name: 'typingRTrial'
  });
  psychoJS.experiment.addLoop(typingRTrial); // add the loop to the experiment
  currentLoop = typingRTrial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  typingRTrial.forEach(function() {
    const snapshot = typingRTrial.getSnapshot();

    typingRTrialLoopScheduler.add(importConditions(snapshot));
    typingRTrialLoopScheduler.add(Blank500RoutineBegin(snapshot));
    typingRTrialLoopScheduler.add(Blank500RoutineEachFrame(snapshot));
    typingRTrialLoopScheduler.add(Blank500RoutineEnd(snapshot));
    typingRTrialLoopScheduler.add(TypingPracRoutineBegin(snapshot));
    typingRTrialLoopScheduler.add(TypingPracRoutineEachFrame(snapshot));
    typingRTrialLoopScheduler.add(TypingPracRoutineEnd(snapshot));
    typingRTrialLoopScheduler.add(endLoopIteration(typingRTrialLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function typingRTrialLoopEnd() {
  psychoJS.experiment.removeLoop(typingRTrial);

  return Scheduler.Event.NEXT;
}


var TaskOrderCond;
function TaskOrderCondLoopBegin(TaskOrderCondLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  TaskOrderCond = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: (("conditions" + expInfo["group"]) + ".xlsx"),
    seed: undefined, name: 'TaskOrderCond'
  });
  psychoJS.experiment.addLoop(TaskOrderCond); // add the loop to the experiment
  currentLoop = TaskOrderCond;  // we're now the current loop

  // Schedule all the trials in the trialList:
  TaskOrderCond.forEach(function() {
    const snapshot = TaskOrderCond.getSnapshot();

    TaskOrderCondLoopScheduler.add(importConditions(snapshot));
    const TaskALoopScheduler = new Scheduler(psychoJS);
    TaskOrderCondLoopScheduler.add(TaskALoopBegin, TaskALoopScheduler);
    TaskOrderCondLoopScheduler.add(TaskALoopScheduler);
    TaskOrderCondLoopScheduler.add(TaskALoopEnd);
    const TaskBLoopScheduler = new Scheduler(psychoJS);
    TaskOrderCondLoopScheduler.add(TaskBLoopBegin, TaskBLoopScheduler);
    TaskOrderCondLoopScheduler.add(TaskBLoopScheduler);
    TaskOrderCondLoopScheduler.add(TaskBLoopEnd);
    const TaskCLoopScheduler = new Scheduler(psychoJS);
    TaskOrderCondLoopScheduler.add(TaskCLoopBegin, TaskCLoopScheduler);
    TaskOrderCondLoopScheduler.add(TaskCLoopScheduler);
    TaskOrderCondLoopScheduler.add(TaskCLoopEnd);
    TaskOrderCondLoopScheduler.add(endLoopIteration(TaskOrderCondLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var TaskA;
function TaskALoopBegin(TaskALoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  TaskA = new TrialHandler({
    psychoJS: psychoJS,
    nReps: nRepsTask1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'TaskA'
  });
  psychoJS.experiment.addLoop(TaskA); // add the loop to the experiment
  currentLoop = TaskA;  // we're now the current loop

  // Schedule all the trials in the trialList:
  TaskA.forEach(function() {
    const snapshot = TaskA.getSnapshot();

    TaskALoopScheduler.add(importConditions(snapshot));
    TaskALoopScheduler.add(MultiplyScreenRoutineBegin(snapshot));
    TaskALoopScheduler.add(MultiplyScreenRoutineEachFrame(snapshot));
    TaskALoopScheduler.add(MultiplyScreenRoutineEnd(snapshot));
    TaskALoopScheduler.add(PracticeScreen_1RoutineBegin(snapshot));
    TaskALoopScheduler.add(PracticeScreen_1RoutineEachFrame(snapshot));
    TaskALoopScheduler.add(PracticeScreen_1RoutineEnd(snapshot));
    const multiLoopPracLoopScheduler = new Scheduler(psychoJS);
    TaskALoopScheduler.add(multiLoopPracLoopBegin, multiLoopPracLoopScheduler);
    TaskALoopScheduler.add(multiLoopPracLoopScheduler);
    TaskALoopScheduler.add(multiLoopPracLoopEnd);
    TaskALoopScheduler.add(BeginTrialScreenRoutineBegin(snapshot));
    TaskALoopScheduler.add(BeginTrialScreenRoutineEachFrame(snapshot));
    TaskALoopScheduler.add(BeginTrialScreenRoutineEnd(snapshot));
    const trials_2LoopScheduler = new Scheduler(psychoJS);
    TaskALoopScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
    TaskALoopScheduler.add(trials_2LoopScheduler);
    TaskALoopScheduler.add(trials_2LoopEnd);
    TaskALoopScheduler.add(BreakTimeRoutineBegin(snapshot));
    TaskALoopScheduler.add(BreakTimeRoutineEachFrame(snapshot));
    TaskALoopScheduler.add(BreakTimeRoutineEnd(snapshot));
    TaskALoopScheduler.add(endLoopIteration(TaskALoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var multiLoopPrac;
function multiLoopPracLoopBegin(multiLoopPracLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  multiLoopPrac = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'multiplicationPract.xlsx',
    seed: undefined, name: 'multiLoopPrac'
  });
  psychoJS.experiment.addLoop(multiLoopPrac); // add the loop to the experiment
  currentLoop = multiLoopPrac;  // we're now the current loop

  // Schedule all the trials in the trialList:
  multiLoopPrac.forEach(function() {
    const snapshot = multiLoopPrac.getSnapshot();

    multiLoopPracLoopScheduler.add(importConditions(snapshot));
    multiLoopPracLoopScheduler.add(Blank500RoutineBegin(snapshot));
    multiLoopPracLoopScheduler.add(Blank500RoutineEachFrame(snapshot));
    multiLoopPracLoopScheduler.add(Blank500RoutineEnd(snapshot));
    multiLoopPracLoopScheduler.add(MultiplyPracRoutineBegin(snapshot));
    multiLoopPracLoopScheduler.add(MultiplyPracRoutineEachFrame(snapshot));
    multiLoopPracLoopScheduler.add(MultiplyPracRoutineEnd(snapshot));
    multiLoopPracLoopScheduler.add(MultiplyFeedbackRoutineBegin(snapshot));
    multiLoopPracLoopScheduler.add(MultiplyFeedbackRoutineEachFrame(snapshot));
    multiLoopPracLoopScheduler.add(MultiplyFeedbackRoutineEnd(snapshot));
    multiLoopPracLoopScheduler.add(endLoopIteration(multiLoopPracLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function multiLoopPracLoopEnd() {
  psychoJS.experiment.removeLoop(multiLoopPrac);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'multiplyConds.xlsx',
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_2.forEach(function() {
    const snapshot = trials_2.getSnapshot();

    trials_2LoopScheduler.add(importConditions(snapshot));
    trials_2LoopScheduler.add(READYRoutineBegin(snapshot));
    trials_2LoopScheduler.add(READYRoutineEachFrame(snapshot));
    trials_2LoopScheduler.add(READYRoutineEnd(snapshot));
    const multiRTrialLoopScheduler = new Scheduler(psychoJS);
    trials_2LoopScheduler.add(multiRTrialLoopBegin, multiRTrialLoopScheduler);
    trials_2LoopScheduler.add(multiRTrialLoopScheduler);
    trials_2LoopScheduler.add(multiRTrialLoopEnd);
    trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var multiRTrial;
function multiRTrialLoopBegin(multiRTrialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  multiRTrial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: fileee,
    seed: undefined, name: 'multiRTrial'
  });
  psychoJS.experiment.addLoop(multiRTrial); // add the loop to the experiment
  currentLoop = multiRTrial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  multiRTrial.forEach(function() {
    const snapshot = multiRTrial.getSnapshot();

    multiRTrialLoopScheduler.add(importConditions(snapshot));
    multiRTrialLoopScheduler.add(Blank500RoutineBegin(snapshot));
    multiRTrialLoopScheduler.add(Blank500RoutineEachFrame(snapshot));
    multiRTrialLoopScheduler.add(Blank500RoutineEnd(snapshot));
    multiRTrialLoopScheduler.add(MultiplyPracRoutineBegin(snapshot));
    multiRTrialLoopScheduler.add(MultiplyPracRoutineEachFrame(snapshot));
    multiRTrialLoopScheduler.add(MultiplyPracRoutineEnd(snapshot));
    multiRTrialLoopScheduler.add(endLoopIteration(multiRTrialLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function multiRTrialLoopEnd() {
  psychoJS.experiment.removeLoop(multiRTrial);

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


function TaskALoopEnd() {
  psychoJS.experiment.removeLoop(TaskA);

  return Scheduler.Event.NEXT;
}


var TaskB;
function TaskBLoopBegin(TaskBLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  TaskB = new TrialHandler({
    psychoJS: psychoJS,
    nReps: nRepsTask2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'TaskB'
  });
  psychoJS.experiment.addLoop(TaskB); // add the loop to the experiment
  currentLoop = TaskB;  // we're now the current loop

  // Schedule all the trials in the trialList:
  TaskB.forEach(function() {
    const snapshot = TaskB.getSnapshot();

    TaskBLoopScheduler.add(importConditions(snapshot));
    TaskBLoopScheduler.add(AdjustSoundInstRoutineBegin(snapshot));
    TaskBLoopScheduler.add(AdjustSoundInstRoutineEachFrame(snapshot));
    TaskBLoopScheduler.add(AdjustSoundInstRoutineEnd(snapshot));
    TaskBLoopScheduler.add(AdjustSoundVolRoutineBegin(snapshot));
    TaskBLoopScheduler.add(AdjustSoundVolRoutineEachFrame(snapshot));
    TaskBLoopScheduler.add(AdjustSoundVolRoutineEnd(snapshot));
    TaskBLoopScheduler.add(AuditoryScreenRoutineBegin(snapshot));
    TaskBLoopScheduler.add(AuditoryScreenRoutineEachFrame(snapshot));
    TaskBLoopScheduler.add(AuditoryScreenRoutineEnd(snapshot));
    TaskBLoopScheduler.add(PracticeScreen_1RoutineBegin(snapshot));
    TaskBLoopScheduler.add(PracticeScreen_1RoutineEachFrame(snapshot));
    TaskBLoopScheduler.add(PracticeScreen_1RoutineEnd(snapshot));
    const audioLoopPracLoopScheduler = new Scheduler(psychoJS);
    TaskBLoopScheduler.add(audioLoopPracLoopBegin, audioLoopPracLoopScheduler);
    TaskBLoopScheduler.add(audioLoopPracLoopScheduler);
    TaskBLoopScheduler.add(audioLoopPracLoopEnd);
    TaskBLoopScheduler.add(BeginTrialScreenRoutineBegin(snapshot));
    TaskBLoopScheduler.add(BeginTrialScreenRoutineEachFrame(snapshot));
    TaskBLoopScheduler.add(BeginTrialScreenRoutineEnd(snapshot));
    const audioCondLoopLoopScheduler = new Scheduler(psychoJS);
    TaskBLoopScheduler.add(audioCondLoopLoopBegin, audioCondLoopLoopScheduler);
    TaskBLoopScheduler.add(audioCondLoopLoopScheduler);
    TaskBLoopScheduler.add(audioCondLoopLoopEnd);
    const audioCondLoopwaisLoopScheduler = new Scheduler(psychoJS);
    TaskBLoopScheduler.add(audioCondLoopwaisLoopBegin, audioCondLoopwaisLoopScheduler);
    TaskBLoopScheduler.add(audioCondLoopwaisLoopScheduler);
    TaskBLoopScheduler.add(audioCondLoopwaisLoopEnd);
    TaskBLoopScheduler.add(BreakTimeRoutineBegin(snapshot));
    TaskBLoopScheduler.add(BreakTimeRoutineEachFrame(snapshot));
    TaskBLoopScheduler.add(BreakTimeRoutineEnd(snapshot));
    TaskBLoopScheduler.add(endLoopIteration(TaskBLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var audioLoopPrac;
function audioLoopPracLoopBegin(audioLoopPracLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  audioLoopPrac = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'auditoryPract.xlsx',
    seed: undefined, name: 'audioLoopPrac'
  });
  psychoJS.experiment.addLoop(audioLoopPrac); // add the loop to the experiment
  currentLoop = audioLoopPrac;  // we're now the current loop

  // Schedule all the trials in the trialList:
  audioLoopPrac.forEach(function() {
    const snapshot = audioLoopPrac.getSnapshot();

    audioLoopPracLoopScheduler.add(importConditions(snapshot));
    audioLoopPracLoopScheduler.add(Audio_PlayRoutineBegin(snapshot));
    audioLoopPracLoopScheduler.add(Audio_PlayRoutineEachFrame(snapshot));
    audioLoopPracLoopScheduler.add(Audio_PlayRoutineEnd(snapshot));
    audioLoopPracLoopScheduler.add(AuditoryPracticeSetRoutineBegin(snapshot));
    audioLoopPracLoopScheduler.add(AuditoryPracticeSetRoutineEachFrame(snapshot));
    audioLoopPracLoopScheduler.add(AuditoryPracticeSetRoutineEnd(snapshot));
    audioLoopPracLoopScheduler.add(AuditoryFeedbackRoutineBegin(snapshot));
    audioLoopPracLoopScheduler.add(AuditoryFeedbackRoutineEachFrame(snapshot));
    audioLoopPracLoopScheduler.add(AuditoryFeedbackRoutineEnd(snapshot));
    audioLoopPracLoopScheduler.add(endLoopIteration(audioLoopPracLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function audioLoopPracLoopEnd() {
  psychoJS.experiment.removeLoop(audioLoopPrac);

  return Scheduler.Event.NEXT;
}


var audioCondLoop;
function audioCondLoopLoopBegin(audioCondLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  audioCondLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Egner.xlsx',
    seed: undefined, name: 'audioCondLoop'
  });
  psychoJS.experiment.addLoop(audioCondLoop); // add the loop to the experiment
  currentLoop = audioCondLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  audioCondLoop.forEach(function() {
    const snapshot = audioCondLoop.getSnapshot();

    audioCondLoopLoopScheduler.add(importConditions(snapshot));
    audioCondLoopLoopScheduler.add(countingCWRoutineBegin(snapshot));
    audioCondLoopLoopScheduler.add(countingCWRoutineEachFrame(snapshot));
    audioCondLoopLoopScheduler.add(countingCWRoutineEnd(snapshot));
    const audioRTrialLoopScheduler = new Scheduler(psychoJS);
    audioCondLoopLoopScheduler.add(audioRTrialLoopBegin, audioRTrialLoopScheduler);
    audioCondLoopLoopScheduler.add(audioRTrialLoopScheduler);
    audioCondLoopLoopScheduler.add(audioRTrialLoopEnd);
    audioCondLoopLoopScheduler.add(endLoopIteration(audioCondLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var audioRTrial;
function audioRTrialLoopBegin(audioRTrialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  audioRTrial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: Condition,
    seed: undefined, name: 'audioRTrial'
  });
  psychoJS.experiment.addLoop(audioRTrial); // add the loop to the experiment
  currentLoop = audioRTrial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  audioRTrial.forEach(function() {
    const snapshot = audioRTrial.getSnapshot();

    audioRTrialLoopScheduler.add(importConditions(snapshot));
    audioRTrialLoopScheduler.add(Audio_PlayRoutineBegin(snapshot));
    audioRTrialLoopScheduler.add(Audio_PlayRoutineEachFrame(snapshot));
    audioRTrialLoopScheduler.add(Audio_PlayRoutineEnd(snapshot));
    audioRTrialLoopScheduler.add(AuditoryTrialssRoutineBegin(snapshot));
    audioRTrialLoopScheduler.add(AuditoryTrialssRoutineEachFrame(snapshot));
    audioRTrialLoopScheduler.add(AuditoryTrialssRoutineEnd(snapshot));
    audioRTrialLoopScheduler.add(endLoopIteration(audioRTrialLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function audioRTrialLoopEnd() {
  psychoJS.experiment.removeLoop(audioRTrial);

  return Scheduler.Event.NEXT;
}


function audioCondLoopLoopEnd() {
  psychoJS.experiment.removeLoop(audioCondLoop);

  return Scheduler.Event.NEXT;
}


var audioCondLoopwais;
function audioCondLoopwaisLoopBegin(audioCondLoopwaisLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  audioCondLoopwais = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'WAIS.xlsx',
    seed: undefined, name: 'audioCondLoopwais'
  });
  psychoJS.experiment.addLoop(audioCondLoopwais); // add the loop to the experiment
  currentLoop = audioCondLoopwais;  // we're now the current loop

  // Schedule all the trials in the trialList:
  audioCondLoopwais.forEach(function() {
    const snapshot = audioCondLoopwais.getSnapshot();

    audioCondLoopwaisLoopScheduler.add(importConditions(snapshot));
    audioCondLoopwaisLoopScheduler.add(countingCWRoutineBegin(snapshot));
    audioCondLoopwaisLoopScheduler.add(countingCWRoutineEachFrame(snapshot));
    audioCondLoopwaisLoopScheduler.add(countingCWRoutineEnd(snapshot));
    const audioRTrialwaisLoopScheduler = new Scheduler(psychoJS);
    audioCondLoopwaisLoopScheduler.add(audioRTrialwaisLoopBegin, audioRTrialwaisLoopScheduler);
    audioCondLoopwaisLoopScheduler.add(audioRTrialwaisLoopScheduler);
    audioCondLoopwaisLoopScheduler.add(audioRTrialwaisLoopEnd);
    audioCondLoopwaisLoopScheduler.add(endLoopIteration(audioCondLoopwaisLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var audioRTrialwais;
function audioRTrialwaisLoopBegin(audioRTrialwaisLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  audioRTrialwais = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: ConditionWAIS,
    seed: undefined, name: 'audioRTrialwais'
  });
  psychoJS.experiment.addLoop(audioRTrialwais); // add the loop to the experiment
  currentLoop = audioRTrialwais;  // we're now the current loop

  // Schedule all the trials in the trialList:
  audioRTrialwais.forEach(function() {
    const snapshot = audioRTrialwais.getSnapshot();

    audioRTrialwaisLoopScheduler.add(importConditions(snapshot));
    audioRTrialwaisLoopScheduler.add(audio_PlayWAISRoutineBegin(snapshot));
    audioRTrialwaisLoopScheduler.add(audio_PlayWAISRoutineEachFrame(snapshot));
    audioRTrialwaisLoopScheduler.add(audio_PlayWAISRoutineEnd(snapshot));
    audioRTrialwaisLoopScheduler.add(audioTrial_WAISRoutineBegin(snapshot));
    audioRTrialwaisLoopScheduler.add(audioTrial_WAISRoutineEachFrame(snapshot));
    audioRTrialwaisLoopScheduler.add(audioTrial_WAISRoutineEnd(snapshot));
    audioRTrialwaisLoopScheduler.add(endLoopIteration(audioRTrialwaisLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function audioRTrialwaisLoopEnd() {
  psychoJS.experiment.removeLoop(audioRTrialwais);

  return Scheduler.Event.NEXT;
}


function audioCondLoopwaisLoopEnd() {
  psychoJS.experiment.removeLoop(audioCondLoopwais);

  return Scheduler.Event.NEXT;
}


function TaskBLoopEnd() {
  psychoJS.experiment.removeLoop(TaskB);

  return Scheduler.Event.NEXT;
}


var TaskC;
function TaskCLoopBegin(TaskCLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  TaskC = new TrialHandler({
    psychoJS: psychoJS,
    nReps: nRepsTask3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'TaskC'
  });
  psychoJS.experiment.addLoop(TaskC); // add the loop to the experiment
  currentLoop = TaskC;  // we're now the current loop

  // Schedule all the trials in the trialList:
  TaskC.forEach(function() {
    const snapshot = TaskC.getSnapshot();

    TaskCLoopScheduler.add(importConditions(snapshot));
    TaskCLoopScheduler.add(vptScreenRoutineBegin(snapshot));
    TaskCLoopScheduler.add(vptScreenRoutineEachFrame(snapshot));
    TaskCLoopScheduler.add(vptScreenRoutineEnd(snapshot));
    TaskCLoopScheduler.add(PracticeScreen_1RoutineBegin(snapshot));
    TaskCLoopScheduler.add(PracticeScreen_1RoutineEachFrame(snapshot));
    TaskCLoopScheduler.add(PracticeScreen_1RoutineEnd(snapshot));
    const vptLoopPracLoopScheduler = new Scheduler(psychoJS);
    TaskCLoopScheduler.add(vptLoopPracLoopBegin, vptLoopPracLoopScheduler);
    TaskCLoopScheduler.add(vptLoopPracLoopScheduler);
    TaskCLoopScheduler.add(vptLoopPracLoopEnd);
    TaskCLoopScheduler.add(BeginTrialScreenRoutineBegin(snapshot));
    TaskCLoopScheduler.add(BeginTrialScreenRoutineEachFrame(snapshot));
    TaskCLoopScheduler.add(BeginTrialScreenRoutineEnd(snapshot));
    const conditionLoopLoopScheduler = new Scheduler(psychoJS);
    TaskCLoopScheduler.add(conditionLoopLoopBegin, conditionLoopLoopScheduler);
    TaskCLoopScheduler.add(conditionLoopLoopScheduler);
    TaskCLoopScheduler.add(conditionLoopLoopEnd);
    TaskCLoopScheduler.add(BreakTimeRoutineBegin(snapshot));
    TaskCLoopScheduler.add(BreakTimeRoutineEachFrame(snapshot));
    TaskCLoopScheduler.add(BreakTimeRoutineEnd(snapshot));
    TaskCLoopScheduler.add(endLoopIteration(TaskCLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var vptLoopPrac;
function vptLoopPracLoopBegin(vptLoopPracLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  vptLoopPrac = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'practiceVPT.xlsx',
    seed: undefined, name: 'vptLoopPrac'
  });
  psychoJS.experiment.addLoop(vptLoopPrac); // add the loop to the experiment
  currentLoop = vptLoopPrac;  // we're now the current loop

  // Schedule all the trials in the trialList:
  vptLoopPrac.forEach(function() {
    const snapshot = vptLoopPrac.getSnapshot();

    vptLoopPracLoopScheduler.add(importConditions(snapshot));
    vptLoopPracLoopScheduler.add(patternGridRoutineBegin(snapshot));
    vptLoopPracLoopScheduler.add(patternGridRoutineEachFrame(snapshot));
    vptLoopPracLoopScheduler.add(patternGridRoutineEnd(snapshot));
    vptLoopPracLoopScheduler.add(Blank1000RoutineBegin(snapshot));
    vptLoopPracLoopScheduler.add(Blank1000RoutineEachFrame(snapshot));
    vptLoopPracLoopScheduler.add(Blank1000RoutineEnd(snapshot));
    vptLoopPracLoopScheduler.add(respGridPracRoutineBegin(snapshot));
    vptLoopPracLoopScheduler.add(respGridPracRoutineEachFrame(snapshot));
    vptLoopPracLoopScheduler.add(respGridPracRoutineEnd(snapshot));
    vptLoopPracLoopScheduler.add(vptFeedbackRoutineBegin(snapshot));
    vptLoopPracLoopScheduler.add(vptFeedbackRoutineEachFrame(snapshot));
    vptLoopPracLoopScheduler.add(vptFeedbackRoutineEnd(snapshot));
    vptLoopPracLoopScheduler.add(endLoopIteration(vptLoopPracLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function vptLoopPracLoopEnd() {
  psychoJS.experiment.removeLoop(vptLoopPrac);

  return Scheduler.Event.NEXT;
}


var conditionLoop;
function conditionLoopLoopBegin(conditionLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  conditionLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condsLoop.xlsx',
    seed: undefined, name: 'conditionLoop'
  });
  psychoJS.experiment.addLoop(conditionLoop); // add the loop to the experiment
  currentLoop = conditionLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  conditionLoop.forEach(function() {
    const snapshot = conditionLoop.getSnapshot();

    conditionLoopLoopScheduler.add(importConditions(snapshot));
    conditionLoopLoopScheduler.add(counterRoutineRoutineBegin(snapshot));
    conditionLoopLoopScheduler.add(counterRoutineRoutineEachFrame(snapshot));
    conditionLoopLoopScheduler.add(counterRoutineRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    conditionLoopLoopScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    conditionLoopLoopScheduler.add(trialsLoopScheduler);
    conditionLoopLoopScheduler.add(trialsLoopEnd);
    conditionLoopLoopScheduler.add(endLoopIteration(conditionLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: sheet,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(patternGridRoutineBegin(snapshot));
    trialsLoopScheduler.add(patternGridRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(patternGridRoutineEnd(snapshot));
    trialsLoopScheduler.add(Blank1000RoutineBegin(snapshot));
    trialsLoopScheduler.add(Blank1000RoutineEachFrame(snapshot));
    trialsLoopScheduler.add(Blank1000RoutineEnd(snapshot));
    trialsLoopScheduler.add(responseGridRoutineBegin(snapshot));
    trialsLoopScheduler.add(responseGridRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(responseGridRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function conditionLoopLoopEnd() {
  psychoJS.experiment.removeLoop(conditionLoop);

  return Scheduler.Event.NEXT;
}


function TaskCLoopEnd() {
  psychoJS.experiment.removeLoop(TaskC);

  return Scheduler.Event.NEXT;
}


function TaskOrderCondLoopEnd() {
  psychoJS.experiment.removeLoop(TaskOrderCond);

  return Scheduler.Event.NEXT;
}


var Blank500Components;
function Blank500RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Blank500'-------
    t = 0;
    Blank500Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.250000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Blank500Components = [];
    Blank500Components.push(blankEmpty);
    
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Blank500RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Blank500'-------
    // get current time
    t = Blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blankEmpty* updates
    if (t >= 0.0 && blankEmpty.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blankEmpty.tStart = t;  // (not accounting for frame time here)
      blankEmpty.frameNStart = frameN;  // exact frame index
      
      blankEmpty.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((blankEmpty.status === PsychoJS.Status.STARTED || blankEmpty.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      blankEmpty.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank500RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Blank500'-------
    Blank500Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var modify;
var TypingPracComponents;
function TypingPracRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TypingPrac'-------
    t = 0;
    TypingPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    modify = false;
    inputText.text = "";
    event.clearEvents("keyboard");
    t = 0;
    
    typeText.setText(productNo);
    // keep track of which components have finished
    TypingPracComponents = [];
    TypingPracComponents.push(typeText);
    TypingPracComponents.push(inputText);
    TypingPracComponents.push(contText);
    
    TypingPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var keys;
function TypingPracRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TypingPrac'-------
    // get current time
    t = TypingPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys({"keyList": ["backspace", "return", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]});
    if (keys.length) {
        if (_pj.in_es6("backspace", keys)) {
            inputText.text = inputText.text.slice(0, (- 1));
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
                thisExp.addData("typedNumber", inputText.text);
                thisExp.addData("typingRT", t);
            } else {
                if (modify) {
                    inputText.text = (inputText.text + keys[0].upper());
                    modify = false;
                } else {
                    inputText.text = (inputText.text + keys[0]);
                }
            }
        }
    }
    
    
    // *typeText* updates
    if (t >= 0.0 && typeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      typeText.tStart = t;  // (not accounting for frame time here)
      typeText.frameNStart = frameN;  // exact frame index
      
      typeText.setAutoDraw(true);
    }

    
    // *inputText* updates
    if (t >= 0.0 && inputText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inputText.tStart = t;  // (not accounting for frame time here)
      inputText.frameNStart = frameN;  // exact frame index
      
      inputText.setAutoDraw(true);
    }

    
    // *contText* updates
    if (t >= 0.0 && contText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contText.tStart = t;  // (not accounting for frame time here)
      contText.frameNStart = frameN;  // exact frame index
      
      contText.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TypingPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TypingPracRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TypingPrac'-------
    TypingPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((Number.parseInt(inputText.text) === productNo)) {
        thisExp.addData("answerCorr", 1);
    } else {
        thisExp.addData("answerCorr", 0);
    }
    
    // the Routine "TypingPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var TypingFeedbackComponents;
function TypingFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TypingFeedback'-------
    t = 0;
    TypingFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if ((Number.parseInt(inputText.text) === productNo)) {
        msg = "Correct!";
    } else {
        msg = "Wrong!";
    }
    
    rtFeedback.setText(msg);
    // keep track of which components have finished
    TypingFeedbackComponents = [];
    TypingFeedbackComponents.push(rtFeedback);
    
    TypingFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TypingFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TypingFeedback'-------
    // get current time
    t = TypingFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rtFeedback* updates
    if (t >= 0.0 && rtFeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rtFeedback.tStart = t;  // (not accounting for frame time here)
      rtFeedback.frameNStart = frameN;  // exact frame index
      
      rtFeedback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((rtFeedback.status === PsychoJS.Status.STARTED || rtFeedback.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rtFeedback.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TypingFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TypingFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TypingFeedback'-------
    TypingFeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _beginResp_allKeys;
var BeginTrialScreenComponents;
function BeginTrialScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'BeginTrialScreen'-------
    t = 0;
    BeginTrialScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    beginResp.keys = undefined;
    beginResp.rt = undefined;
    _beginResp_allKeys = [];
    // keep track of which components have finished
    BeginTrialScreenComponents = [];
    BeginTrialScreenComponents.push(beginTrialText);
    BeginTrialScreenComponents.push(beginResp);
    
    BeginTrialScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function BeginTrialScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'BeginTrialScreen'-------
    // get current time
    t = BeginTrialScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *beginTrialText* updates
    if (t >= 0.0 && beginTrialText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beginTrialText.tStart = t;  // (not accounting for frame time here)
      beginTrialText.frameNStart = frameN;  // exact frame index
      
      beginTrialText.setAutoDraw(true);
    }

    
    // *beginResp* updates
    if (t >= 0.0 && beginResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beginResp.tStart = t;  // (not accounting for frame time here)
      beginResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { beginResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { beginResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { beginResp.clearEvents(); });
    }

    if (beginResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = beginResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _beginResp_allKeys = _beginResp_allKeys.concat(theseKeys);
      if (_beginResp_allKeys.length > 0) {
        beginResp.keys = _beginResp_allKeys[_beginResp_allKeys.length - 1].name;  // just the last key pressed
        beginResp.rt = _beginResp_allKeys[_beginResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    BeginTrialScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BeginTrialScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'BeginTrialScreen'-------
    BeginTrialScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "BeginTrialScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _breakResp_allKeys;
var BreakTimeComponents;
function BreakTimeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'BreakTime'-------
    t = 0;
    BreakTimeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    breakResp.keys = undefined;
    breakResp.rt = undefined;
    _breakResp_allKeys = [];
    // keep track of which components have finished
    BreakTimeComponents = [];
    BreakTimeComponents.push(breakText);
    BreakTimeComponents.push(breakResp);
    
    BreakTimeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function BreakTimeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'BreakTime'-------
    // get current time
    t = BreakTimeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *breakText* updates
    if (t >= 0.0 && breakText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breakText.tStart = t;  // (not accounting for frame time here)
      breakText.frameNStart = frameN;  // exact frame index
      
      breakText.setAutoDraw(true);
    }

    
    // *breakResp* updates
    if (t >= 0.0 && breakResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breakResp.tStart = t;  // (not accounting for frame time here)
      breakResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { breakResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { breakResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { breakResp.clearEvents(); });
    }

    if (breakResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = breakResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _breakResp_allKeys = _breakResp_allKeys.concat(theseKeys);
      if (_breakResp_allKeys.length > 0) {
        breakResp.keys = _breakResp_allKeys[_breakResp_allKeys.length - 1].name;  // just the last key pressed
        breakResp.rt = _breakResp_allKeys[_breakResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    BreakTimeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BreakTimeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'BreakTime'-------
    BreakTimeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "BreakTime" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _multiplyResp_allKeys;
var MultiplyScreenComponents;
function MultiplyScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MultiplyScreen'-------
    t = 0;
    MultiplyScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    multiplyResp.keys = undefined;
    multiplyResp.rt = undefined;
    _multiplyResp_allKeys = [];
    // keep track of which components have finished
    MultiplyScreenComponents = [];
    MultiplyScreenComponents.push(practMultText);
    MultiplyScreenComponents.push(multiplyResp);
    
    MultiplyScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MultiplyScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MultiplyScreen'-------
    // get current time
    t = MultiplyScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practMultText* updates
    if (t >= 0.0 && practMultText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practMultText.tStart = t;  // (not accounting for frame time here)
      practMultText.frameNStart = frameN;  // exact frame index
      
      practMultText.setAutoDraw(true);
    }

    
    // *multiplyResp* updates
    if (t >= 0.0 && multiplyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      multiplyResp.tStart = t;  // (not accounting for frame time here)
      multiplyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { multiplyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { multiplyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { multiplyResp.clearEvents(); });
    }

    if (multiplyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = multiplyResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _multiplyResp_allKeys = _multiplyResp_allKeys.concat(theseKeys);
      if (_multiplyResp_allKeys.length > 0) {
        multiplyResp.keys = _multiplyResp_allKeys[_multiplyResp_allKeys.length - 1].name;  // just the last key pressed
        multiplyResp.rt = _multiplyResp_allKeys[_multiplyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    MultiplyScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MultiplyScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MultiplyScreen'-------
    MultiplyScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "MultiplyScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var MultiplyPracComponents;
function MultiplyPracRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MultiplyPrac'-------
    t = 0;
    MultiplyPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    modify = false;
    inputText2.text = "";
    event.clearEvents("keyboard");
    t = 0;
    
    productText.setText(problem);
    // keep track of which components have finished
    MultiplyPracComponents = [];
    MultiplyPracComponents.push(inputText2);
    MultiplyPracComponents.push(productText);
    MultiplyPracComponents.push(contText2);
    
    MultiplyPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MultiplyPracRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MultiplyPrac'-------
    // get current time
    t = MultiplyPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys({"keyList": ["backspace", "return", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]});
    if (keys.length) {
        if (_pj.in_es6("backspace", keys)) {
            inputText2.text = inputText2.text.slice(0, (- 1));
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
                thisExp.addData("typedAnswer", inputText2.text);
                thisExp.addData("multiplyRT", t);
            } else {
                if (modify) {
                    inputText2.text = (inputText2.text + keys[0].upper());
                    modify = false;
                } else {
                    inputText2.text = (inputText2.text + keys[0]);
                }
            }
        }
    }
    
    
    // *inputText2* updates
    if (t >= 0.0 && inputText2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inputText2.tStart = t;  // (not accounting for frame time here)
      inputText2.frameNStart = frameN;  // exact frame index
      
      inputText2.setAutoDraw(true);
    }

    
    // *productText* updates
    if (t >= 0.0 && productText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      productText.tStart = t;  // (not accounting for frame time here)
      productText.frameNStart = frameN;  // exact frame index
      
      productText.setAutoDraw(true);
    }

    
    // *contText2* updates
    if (t >= 0.0 && contText2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contText2.tStart = t;  // (not accounting for frame time here)
      contText2.frameNStart = frameN;  // exact frame index
      
      contText2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    MultiplyPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MultiplyPracRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MultiplyPrac'-------
    MultiplyPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((Number.parseInt(inputText2.text) === Answer)) {
        thisExp.addData("multiplyCorr", 1);
    } else {
        thisExp.addData("multiplyCorr", 0);
    }
    
    // the Routine "MultiplyPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var MultiplyFeedbackComponents;
function MultiplyFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MultiplyFeedback'-------
    t = 0;
    MultiplyFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if ((Number.parseInt(inputText2.text) === Answer)) {
        message = "Correct!";
    } else {
        message = "Wrong!";
    }
    
    mulFBText.setText(message);
    // keep track of which components have finished
    MultiplyFeedbackComponents = [];
    MultiplyFeedbackComponents.push(mulFBText);
    
    MultiplyFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MultiplyFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MultiplyFeedback'-------
    // get current time
    t = MultiplyFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mulFBText* updates
    if (t >= 0.0 && mulFBText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mulFBText.tStart = t;  // (not accounting for frame time here)
      mulFBText.frameNStart = frameN;  // exact frame index
      
      mulFBText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((mulFBText.status === PsychoJS.Status.STARTED || mulFBText.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      mulFBText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    MultiplyFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MultiplyFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MultiplyFeedback'-------
    MultiplyFeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp1_allKeys;
var READYComponents;
function READYRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'READY'-------
    t = 0;
    READYClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp1.keys = undefined;
    key_resp1.rt = undefined;
    _key_resp1_allKeys = [];
    // keep track of which components have finished
    READYComponents = [];
    READYComponents.push(text_1);
    READYComponents.push(key_resp1);
    
    READYComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function READYRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'READY'-------
    // get current time
    t = READYClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_1* updates
    if (t >= 0.0 && text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_1.tStart = t;  // (not accounting for frame time here)
      text_1.frameNStart = frameN;  // exact frame index
      
      text_1.setAutoDraw(true);
    }

    
    // *key_resp1* updates
    if (t >= 0.0 && key_resp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp1.tStart = t;  // (not accounting for frame time here)
      key_resp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp1.clearEvents(); });
    }

    if (key_resp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp1.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _key_resp1_allKeys = _key_resp1_allKeys.concat(theseKeys);
      if (_key_resp1_allKeys.length > 0) {
        key_resp1.keys = _key_resp1_allKeys[_key_resp1_allKeys.length - 1].name;  // just the last key pressed
        key_resp1.rt = _key_resp1_allKeys[_key_resp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    READYComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function READYRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'READY'-------
    READYComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "READY" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _volInstruResp_allKeys;
var AdjustSoundInstComponents;
function AdjustSoundInstRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AdjustSoundInst'-------
    t = 0;
    AdjustSoundInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    volInstruResp.keys = undefined;
    volInstruResp.rt = undefined;
    _volInstruResp_allKeys = [];
    // keep track of which components have finished
    AdjustSoundInstComponents = [];
    AdjustSoundInstComponents.push(volumeText);
    AdjustSoundInstComponents.push(volInstruResp);
    
    AdjustSoundInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AdjustSoundInstRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AdjustSoundInst'-------
    // get current time
    t = AdjustSoundInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *volumeText* updates
    if (t >= 0.0 && volumeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      volumeText.tStart = t;  // (not accounting for frame time here)
      volumeText.frameNStart = frameN;  // exact frame index
      
      volumeText.setAutoDraw(true);
    }

    
    // *volInstruResp* updates
    if (t >= 0.0 && volInstruResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      volInstruResp.tStart = t;  // (not accounting for frame time here)
      volInstruResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { volInstruResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { volInstruResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { volInstruResp.clearEvents(); });
    }

    if (volInstruResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = volInstruResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _volInstruResp_allKeys = _volInstruResp_allKeys.concat(theseKeys);
      if (_volInstruResp_allKeys.length > 0) {
        volInstruResp.keys = _volInstruResp_allKeys[_volInstruResp_allKeys.length - 1].name;  // just the last key pressed
        volInstruResp.rt = _volInstruResp_allKeys[_volInstruResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AdjustSoundInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AdjustSoundInstRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AdjustSoundInst'-------
    AdjustSoundInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "AdjustSoundInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _sampleResp_allKeys;
var AdjustSoundVolComponents;
function AdjustSoundVolRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AdjustSoundVol'-------
    t = 0;
    AdjustSoundVolClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sampleSoundVol.setVolume(0.5);
    sampleResp.keys = undefined;
    sampleResp.rt = undefined;
    _sampleResp_allKeys = [];
    // keep track of which components have finished
    AdjustSoundVolComponents = [];
    AdjustSoundVolComponents.push(sampleSoundVol);
    AdjustSoundVolComponents.push(sampleResp);
    AdjustSoundVolComponents.push(sampleText);
    
    AdjustSoundVolComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AdjustSoundVolRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AdjustSoundVol'-------
    // get current time
    t = AdjustSoundVolClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sampleSoundVol
    if (t >= 0.0 && sampleSoundVol.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sampleSoundVol.tStart = t;  // (not accounting for frame time here)
      sampleSoundVol.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sampleSoundVol.play(); });  // screen flip
      sampleSoundVol.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sampleSoundVol.getDuration() + sampleSoundVol.tStart)     && sampleSoundVol.status === PsychoJS.Status.STARTED) {
      sampleSoundVol.stop();  // stop the sound (if longer than duration)
      sampleSoundVol.status = PsychoJS.Status.FINISHED;
    }
    
    // *sampleResp* updates
    if (t >= 0.0 && sampleResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sampleResp.tStart = t;  // (not accounting for frame time here)
      sampleResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { sampleResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { sampleResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { sampleResp.clearEvents(); });
    }

    if (sampleResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = sampleResp.getKeys({keyList: ['0', 'space'], waitRelease: false});
      _sampleResp_allKeys = _sampleResp_allKeys.concat(theseKeys);
      if (_sampleResp_allKeys.length > 0) {
        sampleResp.keys = _sampleResp_allKeys[_sampleResp_allKeys.length - 1].name;  // just the last key pressed
        sampleResp.rt = _sampleResp_allKeys[_sampleResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *sampleText* updates
    if (t >= 0.0 && sampleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sampleText.tStart = t;  // (not accounting for frame time here)
      sampleText.frameNStart = frameN;  // exact frame index
      
      sampleText.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AdjustSoundVolComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AdjustSoundVolRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AdjustSoundVol'-------
    AdjustSoundVolComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    sampleSoundVol.stop();  // ensure sound has stopped at end of routine
    // the Routine "AdjustSoundVol" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _AuditoryResp_allKeys;
var AuditoryScreenComponents;
function AuditoryScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AuditoryScreen'-------
    t = 0;
    AuditoryScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    AuditoryResp.keys = undefined;
    AuditoryResp.rt = undefined;
    _AuditoryResp_allKeys = [];
    // keep track of which components have finished
    AuditoryScreenComponents = [];
    AuditoryScreenComponents.push(pracAuditoryText);
    AuditoryScreenComponents.push(AuditoryResp);
    
    AuditoryScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AuditoryScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AuditoryScreen'-------
    // get current time
    t = AuditoryScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pracAuditoryText* updates
    if (t >= 0.0 && pracAuditoryText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracAuditoryText.tStart = t;  // (not accounting for frame time here)
      pracAuditoryText.frameNStart = frameN;  // exact frame index
      
      pracAuditoryText.setAutoDraw(true);
    }

    
    // *AuditoryResp* updates
    if (t >= 0.0 && AuditoryResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AuditoryResp.tStart = t;  // (not accounting for frame time here)
      AuditoryResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { AuditoryResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { AuditoryResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { AuditoryResp.clearEvents(); });
    }

    if (AuditoryResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = AuditoryResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _AuditoryResp_allKeys = _AuditoryResp_allKeys.concat(theseKeys);
      if (_AuditoryResp_allKeys.length > 0) {
        AuditoryResp.keys = _AuditoryResp_allKeys[_AuditoryResp_allKeys.length - 1].name;  // just the last key pressed
        AuditoryResp.rt = _AuditoryResp_allKeys[_AuditoryResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AuditoryScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AuditoryScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AuditoryScreen'-------
    AuditoryScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "AuditoryScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Audio_PlayComponents;
function Audio_PlayRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Audio_Play'-------
    t = 0;
    Audio_PlayClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    soundPresentation = new sound.Sound({
    win: psychoJS.window,
    value: soundsJS,
    secs: -1,
    });
    soundPresentation.setVolume(1);
    // keep track of which components have finished
    Audio_PlayComponents = [];
    Audio_PlayComponents.push(soundPresentation);
    Audio_PlayComponents.push(text1);
    Audio_PlayComponents.push(crossFix1);
    
    Audio_PlayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Audio_PlayRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Audio_Play'-------
    // get current time
    t = Audio_PlayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop soundPresentation
    if (t >= 1 && soundPresentation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      soundPresentation.tStart = t;  // (not accounting for frame time here)
      soundPresentation.frameNStart = frameN;  // exact frame index
      
      soundPresentation.play();  // start the sound (it finishes automatically)
      soundPresentation.status = PsychoJS.Status.STARTED;
    }
    if (t >= (soundPresentation.getDuration() + soundPresentation.tStart)     && soundPresentation.status === PsychoJS.Status.STARTED) {
      soundPresentation.stop();  // stop the sound (if longer than duration)
      soundPresentation.status = PsychoJS.Status.FINISHED;
    }
    
    // *text1* updates
    if (t >= 1 && text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text1.tStart = t;  // (not accounting for frame time here)
      text1.frameNStart = frameN;  // exact frame index
      
      text1.setAutoDraw(true);
    }

    frameRemains = 1 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((text1.status === PsychoJS.Status.STARTED || text1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      text1.setAutoDraw(false);
    }
    
    // *crossFix1* updates
    if (t >= 0.0 && crossFix1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crossFix1.tStart = t;  // (not accounting for frame time here)
      crossFix1.frameNStart = frameN;  // exact frame index
      
      crossFix1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((crossFix1.status === PsychoJS.Status.STARTED || crossFix1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      crossFix1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Audio_PlayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Audio_PlayRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Audio_Play'-------
    Audio_PlayComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    soundPresentation.stop();  // ensure sound has stopped at end of routine
    // the Routine "Audio_Play" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var AuditoryPracticeSetComponents;
function AuditoryPracticeSetRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AuditoryPracticeSet'-------
    t = 0;
    AuditoryPracticeSetClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    modify = false;
    inputText4.text = "";
    event.clearEvents("keyboard");
    t = 0;
    
    // keep track of which components have finished
    AuditoryPracticeSetComponents = [];
    AuditoryPracticeSetComponents.push(inputText4);
    AuditoryPracticeSetComponents.push(contText4);
    AuditoryPracticeSetComponents.push(RECALLtext2);
    
    AuditoryPracticeSetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AuditoryPracticeSetRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AuditoryPracticeSet'-------
    // get current time
    t = AuditoryPracticeSetClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys({"keyList": ["backspace", "return", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]});
    if (keys.length) {
        if (_pj.in_es6("backspace", keys)) {
            inputText4.text = inputText4.text.slice(0, (- 1));
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
                thisExp.addData("typedAudioPrac", inputText4.text);
                thisExp.addData("audioPracRT", t);
            } else {
                if (modify) {
                    inputText4.text = (inputText4.text + keys[0].upper());
                    modify = false;
                } else {
                    inputText4.text = (inputText4.text + keys[0]);
                }
            }
        }
    }
    
    
    // *inputText4* updates
    if (t >= 0.0 && inputText4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inputText4.tStart = t;  // (not accounting for frame time here)
      inputText4.frameNStart = frameN;  // exact frame index
      
      inputText4.setAutoDraw(true);
    }

    
    // *contText4* updates
    if (t >= 0.0 && contText4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contText4.tStart = t;  // (not accounting for frame time here)
      contText4.frameNStart = frameN;  // exact frame index
      
      contText4.setAutoDraw(true);
    }

    
    // *RECALLtext2* updates
    if (t >= 0.0 && RECALLtext2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RECALLtext2.tStart = t;  // (not accounting for frame time here)
      RECALLtext2.frameNStart = frameN;  // exact frame index
      
      RECALLtext2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AuditoryPracticeSetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AuditoryPracticeSetRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AuditoryPracticeSet'-------
    AuditoryPracticeSetComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((Number.parseInt(inputText4.text) === digits_audio)) {
        thisExp.addData("audioPrCorr", 1);
    } else {
        thisExp.addData("audioPrCorr", 0);
    }
    
    // the Routine "AuditoryPracticeSet" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var AuditoryFeedbackComponents;
function AuditoryFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AuditoryFeedback'-------
    t = 0;
    AuditoryFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if ((Number.parseInt(inputText4.text) === digits_audio)) {
        Feedback = "Correct!";
    } else {
        Feedback = "Wrong!";
    }
    
    AudioFBText.setText(Feedback);
    // keep track of which components have finished
    AuditoryFeedbackComponents = [];
    AuditoryFeedbackComponents.push(AudioFBText);
    
    AuditoryFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AuditoryFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AuditoryFeedback'-------
    // get current time
    t = AuditoryFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AudioFBText* updates
    if (t >= 0.0 && AudioFBText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AudioFBText.tStart = t;  // (not accounting for frame time here)
      AudioFBText.frameNStart = frameN;  // exact frame index
      
      AudioFBText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((AudioFBText.status === PsychoJS.Status.STARTED || AudioFBText.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      AudioFBText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AuditoryFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AuditoryFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AuditoryFeedback'-------
    AuditoryFeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var correct;
var wrongTotal;
var countingCWComponents;
function countingCWRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'countingCW'-------
    t = 0;
    countingCWClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    correct = 0;
    wrongTotal = 0;
    
    // keep track of which components have finished
    countingCWComponents = [];
    
    countingCWComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function countingCWRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'countingCW'-------
    // get current time
    t = countingCWClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    countingCWComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function countingCWRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'countingCW'-------
    countingCWComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "countingCW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var AuditoryTrialssComponents;
function AuditoryTrialssRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AuditoryTrialss'-------
    t = 0;
    AuditoryTrialssClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    modify = false;
    inputText3.text = "";
    event.clearEvents("keyboard");
    t = 0;
    
    // keep track of which components have finished
    AuditoryTrialssComponents = [];
    AuditoryTrialssComponents.push(inputText3);
    AuditoryTrialssComponents.push(contText3);
    AuditoryTrialssComponents.push(RECALLtext);
    
    AuditoryTrialssComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AuditoryTrialssRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AuditoryTrialss'-------
    // get current time
    t = AuditoryTrialssClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys({"keyList": ["backspace", "return", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]});
    if (keys.length) {
        if (_pj.in_es6("backspace", keys)) {
            inputText3.text = inputText3.text.slice(0, (- 1));
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
                thisExp.addData("EgnerDSresponse", inputText3.text);
                thisExp.addData("EgnerDSrt", t);
            } else {
                if (modify) {
                    inputText3.text = (inputText3.text + keys[0].upper());
                    modify = false;
                } else {
                    inputText3.text = (inputText3.text + keys[0]);
                }
            }
        }
    }
    
    
    // *inputText3* updates
    if (t >= 0.0 && inputText3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inputText3.tStart = t;  // (not accounting for frame time here)
      inputText3.frameNStart = frameN;  // exact frame index
      
      inputText3.setAutoDraw(true);
    }

    
    // *contText3* updates
    if (t >= 0.0 && contText3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contText3.tStart = t;  // (not accounting for frame time here)
      contText3.frameNStart = frameN;  // exact frame index
      
      contText3.setAutoDraw(true);
    }

    
    // *RECALLtext* updates
    if (t >= 0.0 && RECALLtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RECALLtext.tStart = t;  // (not accounting for frame time here)
      RECALLtext.frameNStart = frameN;  // exact frame index
      
      RECALLtext.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AuditoryTrialssComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AuditoryTrialssRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AuditoryTrialss'-------
    AuditoryTrialssComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((Number.parseInt(inputText3.text) === digits_audio)) {
        correct += 1;
        thisExp.addData("EgnerDSscore", 1);
    } else {
        wrongTotal += 1;
        thisExp.addData("EgnerDSscore", 0);
    }
    if (((inputText3.text.length >= 2) && (correct === 1))) {
        audioRTrial.finished = true;
    } else {
        if ((wrongTotal >= 2)) {
            audioCondLoop.finished = true;
            inputText3 = [];
        }
    }
    
    // the Routine "AuditoryTrialss" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var audio_PlayWAISComponents;
function audio_PlayWAISRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'audio_PlayWAIS'-------
    t = 0;
    audio_PlayWAISClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WAIS_sound = new sound.Sound({
    win: psychoJS.window,
    value: soundsWAIS,
    secs: -1,
    });
    WAIS_sound.setVolume(1);
    // keep track of which components have finished
    audio_PlayWAISComponents = [];
    audio_PlayWAISComponents.push(WAIS_sound);
    audio_PlayWAISComponents.push(reminderTextSound);
    audio_PlayWAISComponents.push(textFIXsound);
    
    audio_PlayWAISComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_PlayWAISRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'audio_PlayWAIS'-------
    // get current time
    t = audio_PlayWAISClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop WAIS_sound
    if (t >= 1 && WAIS_sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WAIS_sound.tStart = t;  // (not accounting for frame time here)
      WAIS_sound.frameNStart = frameN;  // exact frame index
      
      WAIS_sound.play();  // start the sound (it finishes automatically)
      WAIS_sound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (WAIS_sound.getDuration() + WAIS_sound.tStart)     && WAIS_sound.status === PsychoJS.Status.STARTED) {
      WAIS_sound.stop();  // stop the sound (if longer than duration)
      WAIS_sound.status = PsychoJS.Status.FINISHED;
    }
    
    // *reminderTextSound* updates
    if (t >= 1 && reminderTextSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminderTextSound.tStart = t;  // (not accounting for frame time here)
      reminderTextSound.frameNStart = frameN;  // exact frame index
      
      reminderTextSound.setAutoDraw(true);
    }

    frameRemains = 1 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((reminderTextSound.status === PsychoJS.Status.STARTED || reminderTextSound.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      reminderTextSound.setAutoDraw(false);
    }
    
    // *textFIXsound* updates
    if (t >= 0.0 && textFIXsound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textFIXsound.tStart = t;  // (not accounting for frame time here)
      textFIXsound.frameNStart = frameN;  // exact frame index
      
      textFIXsound.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((textFIXsound.status === PsychoJS.Status.STARTED || textFIXsound.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      textFIXsound.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    audio_PlayWAISComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_PlayWAISRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'audio_PlayWAIS'-------
    audio_PlayWAISComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    WAIS_sound.stop();  // ensure sound has stopped at end of routine
    // the Routine "audio_PlayWAIS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var audioTrial_WAISComponents;
function audioTrial_WAISRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'audioTrial_WAIS'-------
    t = 0;
    audioTrial_WAISClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    modify = false;
    inputText9.text = "";
    event.clearEvents("keyboard");
    t = 0;
    
    // keep track of which components have finished
    audioTrial_WAISComponents = [];
    audioTrial_WAISComponents.push(inputText9);
    audioTrial_WAISComponents.push(continuingText);
    audioTrial_WAISComponents.push(recallingTime);
    
    audioTrial_WAISComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audioTrial_WAISRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'audioTrial_WAIS'-------
    // get current time
    t = audioTrial_WAISClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys({"keyList": ["backspace", "return", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]});
    if (keys.length) {
        if (_pj.in_es6("backspace", keys)) {
            inputText9.text = inputText9.text.slice(0, (- 1));
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
                thisExp.addData("WAISDSresponse", inputText9.text);
                thisExp.addData("WAISDSrt", t);
            } else {
                if (modify) {
                    inputText9.text = (inputText9.text + keys[0].upper());
                    modify = false;
                } else {
                    inputText9.text = (inputText9.text + keys[0]);
                }
            }
        }
    }
    
    
    // *inputText9* updates
    if (t >= 0.0 && inputText9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inputText9.tStart = t;  // (not accounting for frame time here)
      inputText9.frameNStart = frameN;  // exact frame index
      
      inputText9.setAutoDraw(true);
    }

    
    // *continuingText* updates
    if (t >= 0.0 && continuingText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continuingText.tStart = t;  // (not accounting for frame time here)
      continuingText.frameNStart = frameN;  // exact frame index
      
      continuingText.setAutoDraw(true);
    }

    
    // *recallingTime* updates
    if (t >= 0.0 && recallingTime.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recallingTime.tStart = t;  // (not accounting for frame time here)
      recallingTime.frameNStart = frameN;  // exact frame index
      
      recallingTime.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    audioTrial_WAISComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audioTrial_WAISRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'audioTrial_WAIS'-------
    audioTrial_WAISComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((Number.parseInt(inputText9.text) === digits_audioWAIS)) {
        correct += 1;
        thisExp.addData("WAISDSscore", 1);
    } else {
        wrongTotal += 1;
        thisExp.addData("WAISDSscore", 0);
    }
    if (((inputText9.text.length >= 2) && (correct === 1))) {
        audioRTrialwais.finished = true;
    } else {
        if ((wrongTotal >= 2)) {
            audioCondLoopwais.finished = true;
            inputText9 = [];
        }
    }
    
    // the Routine "audioTrial_WAIS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _vptResp_allKeys;
var vptScreenComponents;
function vptScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vptScreen'-------
    t = 0;
    vptScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    vptResp.keys = undefined;
    vptResp.rt = undefined;
    _vptResp_allKeys = [];
    // keep track of which components have finished
    vptScreenComponents = [];
    vptScreenComponents.push(vptInstruct);
    vptScreenComponents.push(vptResp);
    
    vptScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function vptScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vptScreen'-------
    // get current time
    t = vptScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *vptInstruct* updates
    if (t >= 0.0 && vptInstruct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vptInstruct.tStart = t;  // (not accounting for frame time here)
      vptInstruct.frameNStart = frameN;  // exact frame index
      
      vptInstruct.setAutoDraw(true);
    }

    
    // *vptResp* updates
    if (t >= 0.0 && vptResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vptResp.tStart = t;  // (not accounting for frame time here)
      vptResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { vptResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { vptResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { vptResp.clearEvents(); });
    }

    if (vptResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = vptResp.getKeys({keyList: ['o', 'space'], waitRelease: false});
      _vptResp_allKeys = _vptResp_allKeys.concat(theseKeys);
      if (_vptResp_allKeys.length > 0) {
        vptResp.keys = _vptResp_allKeys[_vptResp_allKeys.length - 1].name;  // just the last key pressed
        vptResp.rt = _vptResp_allKeys[_vptResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vptScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vptScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vptScreen'-------
    vptScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "vptScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var patternGrid;
var patternGridComponents;
function patternGridRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'patternGrid'-------
    t = 0;
    patternGridClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    patternGrid = createGrid(rows, cols, tiles);
    drawGrid(patternGrid, true);
    
    // keep track of which components have finished
    patternGridComponents = [];
    patternGridComponents.push(staticText);
    
    patternGridComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function patternGridRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'patternGrid'-------
    // get current time
    t = patternGridClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *staticText* updates
    if (t >= 0.0 && staticText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticText.tStart = t;  // (not accounting for frame time here)
      staticText.frameNStart = frameN;  // exact frame index
      
      staticText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((staticText.status === PsychoJS.Status.STARTED || staticText.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      staticText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    patternGridComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function patternGridRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'patternGrid'-------
    patternGridComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    drawGrid(patternGrid, false);
    
    return Scheduler.Event.NEXT;
  };
}


var Blank1000Components;
function Blank1000RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Blank1000'-------
    t = 0;
    Blank1000Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Blank1000Components = [];
    Blank1000Components.push(blankText);
    
    Blank1000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Blank1000RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Blank1000'-------
    // get current time
    t = Blank1000Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blankText* updates
    if (t >= 0.0 && blankText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blankText.tStart = t;  // (not accounting for frame time here)
      blankText.frameNStart = frameN;  // exact frame index
      
      blankText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((blankText.status === PsychoJS.Status.STARTED || blankText.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      blankText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Blank1000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank1000RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Blank1000'-------
    Blank1000Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var respGrid;
var mouseDown;
var gotValidClick;
var respGridPracComponents;
function respGridPracRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'respGridPrac'-------
    t = 0;
    respGridPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respGrid = createGrid(rows, cols, tiles, true);
    correct = false;
    drawGrid(respGrid, true);
    mouseDown = false;
    
    // setup some python lists for storing info about the respMousePrac
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    respGridPracComponents = [];
    respGridPracComponents.push(respMousePrac);
    respGridPracComponents.push(imagePrac);
    
    respGridPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var currentTile;
var patternTile;
function respGridPracRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'respGridPrac'-------
    // get current time
    t = respGridPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    currentTile = 0;
    patternTile = 0;
    for (var tileN = 0, _pj_a = respGrid.length; (tileN < _pj_a); tileN += 1) {
        currentTile = respGrid[tileN];
        patternTile = patternGrid[tileN];
        if (((respMousePrac.isPressedIn(currentTile) && (currentTile.fillColor === white)) && (! mouseDown))) {
            respGrid[tileN].fillColor = black;
            mouseDown = true;
        } else {
            if (((respMousePrac.isPressedIn(currentTile) && (currentTile.fillColor === black)) && (! mouseDown))) {
                respGrid[tileN].fillColor = white;
                mouseDown = true;
            }
        }
        if ((! (respMousePrac.getPressed()[0] === 1))) {
            mouseDown = false;
        }
    }
    if (respMousePrac.isPressedIn(imagePrac)) {
        correct = compareGrid(respGrid, patternGrid);
        thisExp.addData("correct", correct);
        if ((! correct)) {
            thisExp.addData("correct", correct);
            continueRoutine = false;
        }
        continueRoutine = false;
    }
    
    
    // *imagePrac* updates
    if (t >= 0.0 && imagePrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imagePrac.tStart = t;  // (not accounting for frame time here)
      imagePrac.frameNStart = frameN;  // exact frame index
      
      imagePrac.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    respGridPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var _mouseButtons;
function respGridPracRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'respGridPrac'-------
    respGridPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    drawGrid(respGrid, false);
    
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = respMousePrac.getPos();
    _mouseButtons = respMousePrac.getPressed();
    psychoJS.experiment.addData('respMousePrac.x', _mouseXYs[0]);
    psychoJS.experiment.addData('respMousePrac.y', _mouseXYs[1]);
    psychoJS.experiment.addData('respMousePrac.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('respMousePrac.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('respMousePrac.rightButton', _mouseButtons[2]);
    // the Routine "respGridPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fb;
var vptFeedbackComponents;
function vptFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vptFeedback'-------
    t = 0;
    vptFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    fb = "You were incorrect.";
    if ((correct === true)) {
        fb = "You were correct!";
    }
    
    vptTEXT.setText(fb);
    // keep track of which components have finished
    vptFeedbackComponents = [];
    vptFeedbackComponents.push(vptTEXT);
    
    vptFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function vptFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vptFeedback'-------
    // get current time
    t = vptFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *vptTEXT* updates
    if (t >= 0.0 && vptTEXT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vptTEXT.tStart = t;  // (not accounting for frame time here)
      vptTEXT.frameNStart = frameN;  // exact frame index
      
      vptTEXT.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((vptTEXT.status === PsychoJS.Status.STARTED || vptTEXT.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      vptTEXT.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vptFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vptFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vptFeedback'-------
    vptFeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var totalWrong;
var counterRoutineComponents;
function counterRoutineRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'counterRoutine'-------
    t = 0;
    counterRoutineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    totalWrong = 0;
    
    readyText.setText(readyMsg);
    // keep track of which components have finished
    counterRoutineComponents = [];
    counterRoutineComponents.push(readyText);
    
    counterRoutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function counterRoutineRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'counterRoutine'-------
    // get current time
    t = counterRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *readyText* updates
    if (t >= 0.0 && readyText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      readyText.tStart = t;  // (not accounting for frame time here)
      readyText.frameNStart = frameN;  // exact frame index
      
      readyText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((readyText.status === PsychoJS.Status.STARTED || readyText.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      readyText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    counterRoutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function counterRoutineRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'counterRoutine'-------
    counterRoutineComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var responseGridComponents;
function responseGridRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'responseGrid'-------
    t = 0;
    responseGridClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respGrid = createGrid(rows, cols, tiles, true);
    correct = false;
    drawGrid(respGrid, true);
    mouseDown = false;
    
    // setup some python lists for storing info about the respMouse
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    responseGridComponents = [];
    responseGridComponents.push(respMouse);
    responseGridComponents.push(image);
    
    responseGridComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function responseGridRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'responseGrid'-------
    // get current time
    t = responseGridClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    currentTile = 0;
    patternTile = 0;
    for (var tileN = 0, _pj_a = respGrid.length; (tileN < _pj_a); tileN += 1) {
        currentTile = respGrid[tileN];
        patternTile = patternGrid[tileN];
        if (((respMouse.isPressedIn(currentTile) && (currentTile.fillColor === white)) && (! mouseDown))) {
            respGrid[tileN].fillColor = black;
            mouseDown = true;
        } else {
            if (((respMouse.isPressedIn(currentTile) && (currentTile.fillColor === black)) && (! mouseDown))) {
                respGrid[tileN].fillColor = white;
                mouseDown = true;
            }
        }
        if ((! (respMouse.getPressed()[0] === 1))) {
            mouseDown = false;
        }
    }
    if (respMouse.isPressedIn(image)) {
        correct = compareGrid(respGrid, patternGrid);
        thisExp.addData("vptCorrect", correct);
        if ((! correct)) {
            totalWrong += 1;
        }
        if ((totalWrong >= 2)) {
            continueRoutine = false;
            trials.finished = true;
            conditionLoop.finished = true;
        }
        continueRoutine = false;
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    responseGridComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function responseGridRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'responseGrid'-------
    responseGridComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    drawGrid(respGrid, false);
    
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = respMouse.getPos();
    _mouseButtons = respMouse.getPressed();
    psychoJS.experiment.addData('respMouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('respMouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('respMouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('respMouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('respMouse.rightButton', _mouseButtons[2]);
    // the Routine "responseGrid" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var ENDINGComponents;
function ENDINGRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ENDING'-------
    t = 0;
    ENDINGClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ENDINGComponents = [];
    ENDINGComponents.push(ENDtext);
    
    ENDINGComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ENDINGRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ENDING'-------
    // get current time
    t = ENDINGClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ENDtext* updates
    if (t >= 0.0 && ENDtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ENDtext.tStart = t;  // (not accounting for frame time here)
      ENDtext.frameNStart = frameN;  // exact frame index
      
      ENDtext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ENDtext.status === PsychoJS.Status.STARTED || ENDtext.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ENDtext.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ENDINGComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ENDINGRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ENDING'-------
    ENDINGComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
