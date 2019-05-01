// Inspired by the example here:
// https://processing.org/tutorials/gettingstarted/

int t = 0;
int maxT = 10000;
int side;

float centerRW, centerW, radiusW, shiftXW, shiftYW;


void setup() {
  fill(255);
  background(255);
  size(480, 480);
  side = min(width, height);
  radiusW = 0.021*PI;

  centerRW = 0.027 * PI;
  centerW = 0.01 * PI;
  shiftXW = 0.0018 * PI;
  shiftYW = 0.0028 * PI;

  for (t = 0; t <= maxT; t++) {
    step(t);
  }
  noLoop();
}

void step(int t) {

  float radius = side/7 + 10*cos(t*radiusW);

  float centerR = side/5 + 20*sin(t*centerRW);
  float centerX = centerR * cos(t*centerW);
  float centerY = centerR * sin(t*centerW);

  float shiftR = side/6;
  float shiftX = shiftR * cos(t*shiftXW);
  float shiftY = shiftR * sin(t*shiftYW);
  
  float x = centerX + shiftX;
  float y = centerY + shiftY;
  
  ellipse(width/2 + x, height/2 + y, radius, radius);
}

void draw() {
  step(t);
  t++;
}
