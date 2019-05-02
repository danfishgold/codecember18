// Day 01: Air Conditioner
// It looks like an air conditioning tube...
// Inspired by the example here:
// https://processing.org/tutorials/gettingstarted/

float t = 0;
float t1 = 10000; // movement with t^0.25 zoom
float t2 = t1 + 100; // movement with t^1 zoom
float dt = 0.1; // the minimum time difference to add
float minDist; // the minimum distance between consecutive circle centers

float prevDx, prevDy;
int side;

float centerRW, centerW, radiusW, shiftXW, shiftYW;
float centerRP, centerP, radiusP, shiftXP, shiftYP;


void setup() {
  fill(255);
  background(255);
  size(2000, 2000);
  side = min(width, height);
  minDist = side / 180;
  strokeWeight(ceil(side/700));
  
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

  prevDx = dx(0);
  prevDy = dy(0);
  float newDx = prevDx;
  float newDy = prevDy;

  while (t < t2) {

    while (dist(prevDx, prevDy, newDx, newDy) < minDist) { // while the new circle is too close to the previous one
      t += dt; // increase t and try again
      float fac = factor(t);
      newDx = fac*dx(t);
      newDy = fac*dy(t);
    }
    step(t);
    prevDx = newDx;
    prevDy = newDy;
  }
   save("../day_01.png");
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
