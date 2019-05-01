// Inspired by the example here:
// https://processing.org/tutorials/gettingstarted/

int t = 0;
int maxT = 10000;
int side;

float centerRW, centerW, radiusW, shiftXW, shiftYW;
float centerRP, centerP, radiusP, shiftXP, shiftYP;


void setup() {
  fill(255);
  background(255);
  size(480, 480);
  side = min(width, height);
  

  centerRW = random(0.017, 0.023)*PI; // 0.027
  centerW = random(0.008, 0.012)*PI; // 0.01
  radiusW = random(0.019, 0.023)*PI; // 0.021
  shiftXW = random(0.0016, 0.0020)*PI; // 0.0018
  shiftYW = random(0.0026, 0.0030)*PI; // 0.0028
  
  centerRP = random(0, 2)*PI;
  centerP = random(0, 2)*PI;
  radiusP = random(0, 2)*PI;
  shiftXP = random(0, 2)*PI;
  shiftYP = random(0, 2)*PI;



  for (t = 0; t <= maxT; t++) {
    step(t);
  }
  noLoop();
}


float centerR(int t) {
  return side/5 + 20*sin(t*centerRW + centerRP);
}

float shiftR(int t) {
  return side/6;
}

float dx(int t) {
  float centerX = centerR(t) * cos(t*centerW + centerP);
  float shiftX = shiftR(t) * cos(t*shiftXW + shiftXP);
  return centerX + shiftX;
}

float dy(int t) {
  float centerY = centerR(t) * sin(t*centerW + centerP);
  float shiftY = shiftR(t) * sin(t*shiftYW + shiftYP);
  return centerY + shiftY;
}

float radius(int t) {
  return side/7 + 10*cos(t*radiusW + radiusP);
}

void step(int t) {

  float f = (float)(maxT - t) / (float)maxT;
  float r = radius(t);
  ellipse(width/2 + pow(f, 0.25)*dx(t), height/2 + pow(f, 0.25)*dy(t), r, r);
}

void draw() {
  step(t);
  t++;
}
