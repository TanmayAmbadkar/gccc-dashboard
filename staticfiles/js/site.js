var AppClass = function() {
  var appstate = {
    target: 'confetti-holder',
    max: 120,
    size: 1,
    animate: true,
    props: ['circle', 'square', 'triangle', 'line'],
    colors: [[165,104,246],[230,61,135],[0,199,228],[253,214,126]],
    clock: 25,
    rotate: false,
    width: window.innerWidth,
    height: 10*window.innerHeight,
    start_from_edge: false,
    respawn: true
  };

  var confetti = null;

  //
  var updateForm = function() {

    //document.getElementById('json-output').innerHTML = JSON.stringify(appstate);
  };

  var updateState = function() {
    //document.getElementById('json-output').innerHTML = JSON.stringify(appstate);
  };
  //

  var render = function() {
    //updateState();
    if(confetti)
      confetti.clear();
    confetti = new ConfettiGenerator(appstate);
    confetti.render();
  };

  var start = function() {
    //updateForm();
    render();
  };

  var clear = function() {
    confetti.clear();
  }

  return {
    start: start,
    clear: clear,
    render: render
  };
}

///

var app = null;

window.onload = function(){
  app = new AppClass();
  app.start();
}
