// Day 01: Air Conditioner
// It looks like an air conditioning tube...
// Inspired by the example here:
// https://processing.org/tutorials/gettingstarted/

float t = 0;
float t1 = 10000; // movement with t^0.25 zoom
float t2 = t1 + 100; // movement with t^1 zoom

int side;

float centerRW, centerW, radiusW, shiftXW, shiftYW;
float centerRP, centerP, radiusP, shiftXP, shiftYP;


void setup() {
  fill(255);
  strokeWeight(4);
  background(255);
  size(4000, 4000);
  side = min(width, height);
  
  randomSeed(4);

  centerRW = random(0.025, 0.029)*PI; // 0.027
  centerW = random(0.008, 0.012)*PI; // 0.01
  radiusW = random(0.019, 0.023)*PI; // 0.021
  shiftXW = random(0.0016, 0.0020)*PI; // 0.0018
  shiftYW = random(0.0026, 0.0030)*PI; // 0.0028
  
  centerRP = random(0, 2)*PI;
  centerP = random(0, 2)*PI;
  radiusP = random(0, 2)*PI;
  shiftXP = random(0, 2)*PI;
  shiftYP = random(0, 2)*PI;



  while (t <= t2) {
    step(t);
  save("../day_01.png");
    t += 1;
  }  
  noLoop();
}


float centerR(float t) {
  return side/5 + 20*sin(t*centerRW + centerRP);
}

float shiftR(float t) {
  return side/6;
}

float dx(float t) {
  float centerX = centerR(t) * cos(t*centerW + centerP);
  float shiftX = shiftR(t) * cos(t*shiftXW + shiftXP);
  return centerX + shiftX;
}

float dy(float t) {
  float centerY = centerR(t) * sin(t*centerW + centerP);
  float shiftY = shiftR(t) * sin(t*shiftYW + shiftYP);
  return centerY + shiftY;
}

float radius(float t) {
  return side/7 + 10*cos(t*radiusW + radiusP);
}

float factor(float t) {
  float f = (t2 - t) / t2;
  if (t < t1) {
    return pow(f, 0.25);
  } else {
    return pow((t2-t1) / t2, 0.25) * (t2-t) / (t2-t1);
  }
}
void step(float t) {
  float r = radius(t);
  float f = factor(t);
  ellipse(width/2 + f*dx(t), height/2 + f*dy(t), r, r);
}

void draw() {
  step(t);
  t+= 1;
}
