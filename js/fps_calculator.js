class FPSCalculator
{
	constructor(calculationPeriod, onChange)
	{
		this.calculationPeriod = calculationPeriod;
		this.onChange = onChange;

		this.lastTime = new Date().getTime();
		this.framesSinceLast = 0;
		this.fps = 0;
	}

	frame()
	{
		let now = new Date().getTime();

		this.framesSinceLast++;

		let dt = (now - this.lastTime) / 1000.;
		if (dt > this.calculationPeriod) {
			this.lastTime = now;
			this.fps = this.framesSinceLast / dt;
			this.framesSinceLast = 0;

			if (this.onChange) {
				this.onChange(this.fps);
			}
		}
	}

	getFps() { return this.fps; }
}

