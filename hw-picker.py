#!/usr/bin/python
import argparse, random, re

def tryint(s):
		try:
				return int(s)
		except:
				return s

def alphanum_key(s):
		""" Turn a string into a list number chunks.
				"12.4" -> [12, 4]
		"""
		return [ tryint(c) for c in re.split('.', s) ]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='pick random homework problems from textbook.')
	parser.add_argument('chapter', type=int,
											help='chapter to pick problems from.')
	parser.add_argument('problems', type=int,
											help='total numbers of problem')
	parser.add_argument('pick', type=int, 
											help='number of problems to pick')
	args = parser.parse_args()

	try:
		set_problems = set()
		if args.pick > args.problems:
			raise ValueError('pick is larger than problems pool')
		while set_problems.__len__() < args.pick:
			tmp = "%d.%d" %(args.chapter, random.randint(1,args.problems))
			set_problems.add(tmp)

		list_probems = list(set_problems)
		list_probems.sort(key=alphanum_key)
		#print out list
		print(list_probems)
	except Exception as error:
		print('caught this error: ' + repr(error))

