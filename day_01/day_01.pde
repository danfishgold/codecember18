// Inspired by the example here:
// https://processing.org/tutorials/gettingstarted/

int t = 0;
int maxT = 10000;
int side;


void setup() {
  fill(255);
  background(255);
  size(480, 480);
  side = min(width, height);

  for (t = 0; t <= maxT; t++) {
    step(t);
  }
  noLoop();
}

void step(int t) {
  float centerR = side/5 + 20*sin(t*0.027*PI);
  float circleR = side/7 + 10*cos(t*0.021*PI);
  float shiftR = side/6;

  float x = shiftR*cos(t*0.0018*PI + 0.8) + centerR * cos(t * 0.01 * PI);
  float y = shiftR*cos(t*0.0028*PI - 0.5) + centerR * sin(t * 0.01 * PI);
  
  ellipse(width/2 + x, height/2 + y, circleR, circleR);
}

void draw() {
  step(t);
  t++;
}
