/*  
    This JS is pretty quick and hacky – used for triggering the sounds, and for the button interaction at the start.
*/

var startBtn = document.querySelector('.startBtn'),
  moveText = document.querySelector('.moveText'),
  marioFlat = document.querySelector('.marioFlat'),
  mario = document.querySelector('.mario'),
  coin = document.querySelectorAll('.coin'),
  qbox = document.querySelectorAll('.qbox'),
  mushroom = document.querySelector('.mushroom'),
  goombaDies = document.querySelectorAll('.enemy-dies'),
  enemy1 = document.querySelector('.enemy1'),
  enemy4 = document.querySelector('.enemy4'),
  enemy5 = document.querySelector('.enemy5'),
  enemy7 = document.querySelector('.enemy7');

//  =======================
//  === EVENT LISTENERS ===
//  =======================

//click handler for START button
  startBtn.addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('textBox').className += ' fade';
    audioNewWorld.play();
    document.getElementById('levelSelect').className = 'startScreen';
  }, false);

//listening for our flat mario on level select to start moving
  marioFlat.addEventListener('animationstart', marioFlatSound);
  marioFlat.addEventListener('webkitAnimationStart', marioFlatSound);
    function marioFlatSound() {
      //play movement sound, delay by 200ms, then play again
      mapTravel.play();
      window.setTimeout(function () { mapTravel.currentTime = 0.01; }, 200);
    }

//listening for our flat mario on level select to start moving
  marioFlat.addEventListener('animationend', marioFlatEnd);
  marioFlat.addEventListener('webkitAnimationEnd', marioFlatEnd);
    function marioFlatEnd() {
      //play movement sound, delay by 200ms, then play again
      levelBegin.play();
      audioSelectTheme.pause();
      document.getElementById('levelSelect').className += ' fadeScreen';

      window.setTimeout(function () { audioWorldTheme.play(); }, 300);
      window.setTimeout(function () { document.getElementById('mainScene').className += ' startAnim'; }, 1000);
    }

//listening for end of the first goomba animation
  var i, enemyLength = goombaDies.length;
  for (i = 0; i < enemyLength; i++) {
    goombaDies[i].addEventListener('animationend', enemyDead);
    goombaDies[i].addEventListener('webkitAnimationEnd', enemyDead);
  }
    function enemyDead(e) {
      if (!audioStomp.paused) {
        audioStomp.currentTime = 0.01;
      } else {
        audioStomp.play();
      }
    }

  enemy4.addEventListener('animationend', playStomp);
  enemy4.addEventListener('webkitAnimationEnd', playStomp);
    function playStomp(e) {
      if (e.animationName !== 'turtle-hit-qbox') {

        if (!audioStomp.paused) {
          audioStomp.currentTime = 0.01;
        } else {
          audioStomp.play();
        }
      }
    }

  enemy4.addEventListener('animationstart', playKick);
  enemy4.addEventListener('webkitAnimationEnd', playKick);
    function playKick() {
      audioKick.play();
    }

  enemy7.addEventListener('animationstart', wingedGoomba);
  enemy7.addEventListener('webkitAnimationStart', wingedGoomba);
    function wingedGoomba(e) {
      if (e.animationName === 'enemy-seventh') {
        window.setTimeout(function () { audioStomp.currentTime = 0.01; audioStomp.play(); }, 1800);
      } else if (e.animationName === 'enemy-seventh-dead') {
        audioTailSpin.play();
      }
    }

//coin
  var i, coinLength = coin.length;
  for (i = 0; i < coinLength; i++) {
    coin[i].addEventListener('animationstart', playCoin);
    coin[i].addEventListener('webkitAnimationStart', playCoin);
  }
    function playCoin() {
      if (!audioCoin.paused) {
        audioCoin.currentTime = 0.01;
      } else {
        audioCoin.play();
      }
    }

  var i, qboxLength = qbox.length;
  for (i = 0; i < qboxLength; i++) {
    qbox[i].addEventListener('animationstart', playBump);
    qbox[i].addEventListener('webkitAnimationStart', playBump);
  }
    function playBump() {
      if (!audioBump.paused) {
        audioBump.currentTime = 0.01;
      } else {
        audioBump.play();
      }
    }

//mushroom
  mushroom.addEventListener('animationstart', function(e) { audioMushroom.play(); });
  mushroom.addEventListener('webkitAnimationStart', function(e) { audioMushroom.play(); });

//Mario listener events
  mario.addEventListener('animationstart', marioEventListener);
  mario.addEventListener('webkitAnimationStart', marioEventListener);
    function marioEventListener(e) {
      switch (e.animationName) {
        //jumps
        case 'mario-jump-first':
        case 'mario-jump-third':
        case 'mario-jump-qbox':
        case 'mario-jump-fourth':
        case 'mario-jump-fifth':
        case 'mario-jump-sixth':
          moveTextToggle('hide'); //turn sign off
          audioMarioJump.play();
          break;
        case 'mario-jump-second':
          moveTextToggle('hide'); //turn sign off
          audioMarioJump.play();
          window.setTimeout(function () { audioMarioJump.currentTime = 0.01; }, 370);
          break;
        case 'mario-grow':
          audioPowerUp.play();
          break;
        case 'mario-run-second':
        case 'mario-sprite-jump-fourth':
        case 'mario-kick-shell':
        case 'mario-jump-sixth':
        case 'mario-sprint':
          moveTextToggle('hide'); //turn sign off
          break;
        case 'mario-racoon-change':
          audioRacoon.play();
          break;
        case 'mario-flight-sprite':
          window.setTimeout(function () { audioFlight.play(); }, 400);
          break;
      }
    }
  mario.addEventListener('animationend', marioEventEndListener);
  mario.addEventListener('webkitAnimationEnd', marioEventEndListener);
    function marioEventEndListener(e) {
      switch (e.animationName) {
        //jumps
        case 'mario-jump-first':
        case 'mario-grow':
        case 'mario-jump-qbox':
        case 'mario-turtle-hit':
        case 'mario-racoon-change':
        case 'mario-jump-seventh':
          moveTextToggle('show');
          break;
      }
    }

//  =============================
//  === AUDIO BITS AND PIECES ===
//  =============================

var audio = new Audio(), //generic audio object for testing
  canPlayOgg = !!audio.canPlayType && audio.canPlayType('audio/ogg; codecs="vorbis"') !== "",
  canPlayMP3 = !!audio.canPlayType && audio.canPlayType('audio/mp3') !== "",

  //setup audio elements to embed in page,
  audioObjects = [],
  audioSelectTheme,
  audioWorldTheme,
  audioNewWorld,
  mapTravel,
  levelBegin,
  audioMarioJump,
  audioFlight,
  audioCoin,
  audioBump,
  audioStomp,
  audioKick,
  audioTailSpin,
  audioMushroom,
  audioPowerUp,
  audioRacoon;


  audioSelectTheme = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3-world-map", true);
  audioWorldTheme = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3-overworld-1", true);
  audioNewWorld = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_map_new_world");
  mapTravel = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_map_travel");
  levelBegin = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_enter_level");
  audioMarioJump = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_jump");
  audioFlight = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_pmeter");
  audioCoin = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_coin");
  audioBump = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_bump");
  audioStomp = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_stomp");
  audioKick = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_kick");
  audioTailSpin = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_tail");
  audioMushroom = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_mushroom_appears");
  audioPowerUp = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_power-up"),
  audioRacoon = createAudio("https://s3-us-west-2.amazonaws.com/s.cdpn.io/12207/smb3_raccoon_transform");

audioSelectTheme.play();

//generic function to create all new audio elements equal, with preload
function createAudio (audioFile, loopSet) {
  var tempAudio = new Audio(),
    audioExt;

  if (canPlayMP3) {
    audioExt = '.mp3';
  } else if (canPlayOgg) {
    audioExt = '.ogg';
  }

  tempAudio.setAttribute('src', audioFile + audioExt);
  tempAudio.preload = 'auto';
  tempAudio.loop = (loopSet === true ? true : false);

  return tempAudio;
}


function deleteNode(element) {
  element.style.display = 'none';
}

function moveTextToggle (state) {
  var moveTextState = moveText.style.display;

  if (moveTextState === 'block' || state === 'hide') {
    moveText.style.display = 'none';
  } else if (moveTextState !== 'block' || state === 'show') {
    moveText.style.display = 'block';
  }
}