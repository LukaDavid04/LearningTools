import Paddle from "/src/paddle";
import InputHandler from "/src/input";

let canvas = document.getElementById("gameScreen");
let ctx = canvas.getContext("2d");

// ctx.clearRect(0,0,800,600);

// ctx.fillStyle = "#f00";
// ctx.fillRect(20, 20, 100, 100);

// ctx.fillStyle = '#00f';
// ctx.fillRect(370,260,50,50);

const GAME_WIDTH = 500;
const GAME_HEIGHT = 600;

ctx.clearRect(0, 0, 500, 600);

let paddle = new Paddle(GAME_WIDTH, GAME_HEIGHT);

new InputHandler(paddle);

paddle.draw(ctx);

let lastTime = 0;

function gameLoop(timestamp) {
  let dt = timestamp - lastTime;
  lastTime = timestamp;
  ctx.clearRect(0, 0, 500, 600);
  paddle.update(dt);
  paddle.draw(ctx);

  requestAnimationFrame(gameLoop);
}

gameLoop();
