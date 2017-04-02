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
	
  parser.add_argument('chapter', type=int, help='chapter to pick problems from.')
	
  parser.add_argument('problems', type=int, help='total numbers of problem')
	
  parser.add_argument('pick', type=int, help='number of problems to pick')
	
  args = parser.parse_args()
	list = []
	i = 0
	while i < args.pick:
		tmp = "%d.%d" %(args.chapter, random.randint(0,args.problems))
		list.append(tmp)
		i += 1
  list.sort(key=alphanum_key)
  #print out list
  print(list)
