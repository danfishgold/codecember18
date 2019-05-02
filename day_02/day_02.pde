void draw_triangle(float r, float theta, float length) {
    resetMatrix();
    translate(width/2 + r*cos(theta), height/2 + r*sin(theta));
    rotate(theta - HALF_PI);
    fill(255);
    stroke(255);
    triangle(-length/2, 0, 0, length, length/2, 0);
    stroke(0);
    line(-length/2, 0, 0, length);
    line(length/2, 0, 0, length);
}


float side;
float minR = 0.01;
float maxR = 0.4;
float phi = (1+sqrt(5)) / 2;
float w = TWO_PI / phi;
int count = 300;

void setup() {
  size(800, 800);
  side = min(width, height);
  background(255);
  for (int i = 0; i < count; i++) {
    float f = (float)i / (float)count;
    float r = side*lerp(maxR, minR, f);
    float len = lerp(1, 0.6, f) * side/40;
    float theta = w * i;
    draw_triangle(r, theta, len);
  }
}


void draw() {}
