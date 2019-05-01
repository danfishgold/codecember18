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

void step(int t) {

  float f = (float)(maxT - t) / (float)maxT;

  float radius = side/7 + 10*cos(t*radiusW + radiusP);

  float centerR = side/5 + 20*sin(t*centerRW + centerRP);
  float centerX = centerR * cos(t*centerW + centerP);
  float centerY = centerR * sin(t*centerW + centerP);

  float shiftR = side/6;
  float shiftX = shiftR * cos(t*shiftXW + shiftXP);
  float shiftY = shiftR * sin(t*shiftYW + shiftYP);
  
  float x = centerX + shiftX;
  float y = centerY + shiftY;
  
  ellipse(width/2 + pow(f, 0.25)*x, height/2 + pow(f, 0.25)*y, radius, radius);
}

void draw() {
  step(t);
  t++;
}
