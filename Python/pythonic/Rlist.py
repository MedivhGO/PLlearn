#!/usr/bin/python

class Rlist(object):
	class EmptyList(object):
		def __len__(self):
			return 0
	empty = EmptyList()
	def __init__(self,first,rest=empty):
		self.first = first
		self.rest = rest
	def __repr_(self):
		args = repr(self.first)
		if self.rest is not Rlist.empty:
			args+='.{0}'.format(repr(self.rest))
		return 'Rlist({0})'.format(args)
	def __len__(self):
		return 1 + len(self.rest)
	def __getitem__(self,i):
		if i==0:
			return self.first
		return self.rest[i-1]


s = Rlist(1,Rlist(2,Rlist(3)))
print(len(s))
print(s[1])
