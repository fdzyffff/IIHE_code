import sys

class ShowProcess():
	i = 0
	max_steps = 0
	max_arrow = 50
	step_length = 1
	pre_percent = -1

	def __init__(self, max_steps, print_enable = True):
		self.max_steps = max_steps
		self.i = 0
		self.pre_percent = -1
		self.print_enable = print_enable

	def show_process(self, i=None):
		if i is not None:
			self.i = i
		else:
			self.i += 1
		if not self.print_enable:return
		if self.step_length > 1:
			if (self.max_steps > 100):
				if (not int(self.i) % int(float(self.max_steps)/float(self.step_length)) == 0):return
		percent = int(self.i * 100.0 / self.max_steps)
		if self.pre_percent == percent:return
		self.pre_percent = percent
		num_arrow = int(self.i * self.max_arrow / self.max_steps)
		num_line = self.max_arrow - num_arrow
		process_bar = '[' + '>' * num_arrow + '-' * num_line + ']' + '%2d' % percent + '%' + '\r'
		sys.stdout.write(process_bar)
		sys.stdout.flush()

	def close(self, words='done'):
		if self.print_enable: print "\n%s"%(words)
		self.i = 0
