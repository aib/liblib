import sys
import time

class EventProfiler:
	def __init__(self):
		self.events = {}
		self.active_event = None

	def now(self):
		return time.monotonic()

	def start(self, name, now=None):
		if now is None: now = self.now()
		self.end(now)
		self.active_event = name, now

	def end(self, now=None):
		if now is None: now = self.now()

		if self.active_event is not None:
			self._add_event(self.active_event[0], now - self.active_event[1])
		self.active_event = None

	def _add_event(self, name, elapsed):
		if name not in self.events:
			self.events[name] = 0

		self.events[name] += elapsed

	def get_events(self):
		return self.events

	def print_events(self, f=None):
		if f is None: f = sys.stdout

		total = sum(self.events.values())
		longest_name_len = max(map(len, self.events.keys()))

		print(("%-" + str(longest_name_len) + "s  Time  Percent") % ("Name",))
		for name, elapsed in sorted(self.events.items(), key=lambda e: e[1], reverse=True):
			print(("%-" + str(longest_name_len) + "s %6.3f   %2.0f%%") % (name, elapsed, elapsed*100/total), file=f)
