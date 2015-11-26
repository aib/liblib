public class GcodeSerial extends PApplet {
	private static final int RESPONSE_LOOP_DELAY = 10;

	private Serial port;
	private String readBuffer;

	public GcodeSerial(String portName, int baud) {
		println("Initializing GcodeSerial for port " + portName + " at " + baud + " baud");
		port = new Serial(this, portName, baud);
		readBuffer = "";
	}

	public void serialEvent(Serial s) {
		while (s.available() > 0) {
			readBuffer += s.readChar();
		}
	}

	public void sendLine(String line) {
		println("->" + line);
		port.write(line + "\n");
	}

	public String getNextResponse() {
		String nextResponse = "";
		for (int i=0; i < readBuffer.length(); ++i) {
			if (readBuffer.charAt(i) == '\r') continue;
			if (readBuffer.charAt(i) == '\n') {
				println("<-" + nextResponse);
				readBuffer = readBuffer.substring(i + 1);
				return nextResponse;
			}
			nextResponse += readBuffer.charAt(i);
		}

		return null;
	}

	public String waitForNextResponse() {
		String response = getNextResponse();
		while (response == null) {
			delay(RESPONSE_LOOP_DELAY);
			response = getNextResponse();
		}
		return response;
	}
}
