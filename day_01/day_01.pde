int t = 0;
float theta = 0;
float centerR = 100;
float circleR = 80;

void setup() {
  size(480, 480);
  fill(255);
  background(255);
}

void draw() {
  centerR = 100 + 20*sin(t*0.027*PI);
  circleR = 70 + 10*cos(t*0.021*PI);

  float x = 80*cos(t*0.0018*PI + 0.8) + centerR * cos(t * 0.01 * PI);
  float y = 80*cos(t*0.0028*PI - 0.5) + centerR * sin(t * 0.01 * PI);
  
  ellipse(width/2 + x, height/2 + y, circleR, circleR);

  t++;
}
