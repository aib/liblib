import functools
import inspect

class ApiWrapper:
	def __init__(self):
		self.endpoints = {}

	def endpoint(self):
		def wrapper(fn):
			sig = inspect.signature(fn)
			params = sig.parameters.values()
			req_params = list(map(lambda p: p.name, filter(lambda p: p.default == inspect.Signature.empty, params)))
			opt_params = list(map(lambda p: p.name, filter(lambda p: p.default != inspect.Signature.empty, params)))

			self.endpoints[fn] = {
				'name': fn.__qualname__,
				'fn': fn,
				'required_params': req_params,
				'optional_params': opt_params
			}

			@functools.wraps(fn)
			def call(*args, **kwargs):
				data = self.build_data(self.endpoints[fn], args, kwargs)
				try:
					(fn_args, fn_kwargs) = self.build_args(self.endpoints[fn], data)
					return self.return_normal(self.endpoints[fn], fn(*fn_args, **fn_kwargs))
				except Exception as e:
					return self.return_error(self.endpoints[fn], e)
			return call
		return wrapper

	def build_args(self, epinfo, data):
		args = []
		for req in epinfo['required_params']:
			if req in data:
				args.append(data[req])
			else:
				self.handle_noarg(epinfo, req)

		kwargs = {}
		for opt in epinfo['optional_params']:
			if opt in data:
				kwargs[opt] = data[opt]

		return (args, kwargs)

	def build_data(self, epinfo, args, kwargs):
		raise NotImplementedError

	def handle_noarg(self, epinfo, argname):
		raise NotImplementedError

	def return_normal(self, epinfo, retval):
		raise NotImplementedError

	def return_error(self, epinfo, err):
		raise NotImplementedError
