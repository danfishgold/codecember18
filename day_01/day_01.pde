// Inspired by the example here:
// https://processing.org/tutorials/gettingstarted/

int t = 0;
int t1 = 10000; // movement with t^0.25 zoom
int t2 = t1 + 100; // movement with t^1 zoom

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



  for (t = 0; t <= t2; t++) {
    step(t);
  }
  save("../day_01.png");
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

  float f = (float)(t2 - t) / (float)t2;
  
  float factor;
  if (t < t1) {
    factor = pow(f, 0.25);
  } else {
    factor = pow((float)(t2-t1) / (float)t2, 0.25) * (float)(t2-t)/(float)(t2-t1);
  }

  float r = radius(t);
  ellipse(width/2 + factor*dx(t), height/2 + factor*dy(t), r, r);

}

void draw() {
  step(t);
  t++;
}
