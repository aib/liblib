import threading

class ThreadRunner:
	def __init__(self, semaphore, target):
		self._semaphore = semaphore
		self._target = target

	def run(self, *args, **kwargs):
		try:
			self._target(*args, **kwargs)
		finally:
			self._semaphore.release()

class ThreadPool:
	def __init__(self, size):
		self._size = size
		self._thread_semaphore = threading.Semaphore(size)

	def run(self, target, args=(), kwargs={}):
		runner = ThreadRunner(self._thread_semaphore, target)
		thread = threading.Thread(target=runner.run, args=args, kwargs=kwargs)

		self._thread_semaphore.acquire()
		thread.start()

	def wait_all(self):
		for _ in range(self._size):
			self._thread_semaphore.acquire()
		for _ in range(self._size):
			self._thread_semaphore.release()
