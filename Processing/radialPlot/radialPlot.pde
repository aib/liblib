double TAU = 2 * Math.PI;

double getR(double theta)
{
  return theta;
}

void setup()
{
  size(800, 800);
  background(color(0));

  double thetaDefaultStep = TAU / 4;
  double theta = 0;

  double prevTheta = theta;
  double prevR = getR(prevTheta);
  double prevRx = prevR * Math.cos(prevTheta);
  double prevRy = prevR * Math.sin(prevTheta);
  int prevX = (int) Math.round(prevRx);
  int prevY = (int) Math.round(prevRy);

  double thetaStep = thetaDefaultStep;

  while (theta < 3 * TAU) {
    while (true) {
      theta = prevTheta + thetaStep;
      println("theta is " + theta);
      double r = getR(theta);
      double rx = r * Math.cos(theta);
      double ry = r * Math.sin(theta);
      int ix = (int) Math.round(rx);
      int iy = (int) Math.round(ry);

      println("px: " + prevX + " py: " + prevY + " ix: " + ix + " iy: " + iy);

      if ((Math.abs(ix - prevX) + Math.abs(iy - prevY)) > 1) {
//      if (Math.abs(ix - prevX) > 1 || Math.abs(iy - prevY) > 1) {
        thetaStep /= 2;
        println("ts reduced to " + thetaStep);
        continue;
      } else {
        plot(ix, iy);
        prevX = ix;
        prevY = iy;
        prevTheta = theta;
        break;
      }
    }
  }

//  saveFrame();
}

void plot(int x, int y)
{
  int zx = width / 2;
  int zy = height / 2;
  set(zx + x, zy - y, color(255));
}

void loop()
{
}
