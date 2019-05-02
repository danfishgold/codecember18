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
float minR = 0.003;
float maxR = 0.4;
float phi = (1+sqrt(5)) / 2;
float w = TWO_PI / phi;
int count = 800;

void setup() {
  size(800, 800);
  side = min(width, height);
  background(255);
  for (int i = 0; i < count; i++) {
    float f = (float)i / (float)count;
    // rdr/dt = const => r = sqrt(c1 + c2t)
    float r = side*sqrt(lerp(maxR*maxR, minR*minR, f));
    float len = side/65;
    float theta = w * i;
    draw_triangle(r, theta, len);
  }
  save("../day_02.png");
}


void draw() {}
