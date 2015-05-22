/**
 * My first attempt at 2D Perlin noise generation
 * 
 * aib, 20130215
 */
function Perlin2D(gridSize)
{
	var self = this;

	this.gridSize = gridSize;
	this.grid = {};

	this.get = function(x, y) {
		x = x / gridSize;
		y = y / gridSize;
		
		var xn = Math.floor(x);
		var yn = Math.floor(y);
		var xp = Math.floor(x + 1);
		var yp = Math.floor(y + 1);

		var xdn = x - xn;
		var ydn = y - yn;
		var xdp = x - xp;
		var ydp = y - yp;

		var sGrad = getGradient(xn, yn);
		var sDot = sGrad.x * xdn + sGrad.y * ydn;

		var tGrad = getGradient(xp, yn);
		var tDot = tGrad.x * xdp + tGrad.y * ydn;

		var uGrad = getGradient(xn, yp);
		var uDot = uGrad.x * xdn + uGrad.y * ydp;

		var vGrad = getGradient(xp, yp);
		var vDot = vGrad.x * xdp + vGrad.y * ydp;

		var fInterp = function(t) { return 3*t*t - 2*t*t*t; };
		var lerp = function(a, b, t) { return a + (b - a) * t; };
		var xxyn = lerp(sDot, tDot, fInterp(xdn));
		var xxyp = lerp(uDot, vDot, fInterp(xdn));
		var yy = lerp(xxyn, xxyp, fInterp(ydn));

		return yy;
	};

	var getGradient = function(x, y) {
		if (self.grid[x] === undefined) {
			self.grid[x] = {};
		}

		if (self.grid[x][y] === undefined) {
			var theta = Math.random() * ajsl.TAU;
			var gx = Math.cos(theta);
			var gy = Math.sin(theta);
			self.grid[x][y] = { 'x': gx, 'y': gy };
		}

		return self.grid[x][y];
	};
}
