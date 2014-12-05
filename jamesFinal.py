import sys,re,random
class BondMovie:
	actor = ''
	year = ''
	name = ''
	watched = 0 
	def __init__(self,t0 ='',t1 = '',t2 = '', t3 = 0): 
		if t0 != '' and t1 != '' and t2 != '':
			self.name = t0
			self.year = t1
			self.actor = t2
			self.watched = t3
try:
	movieNumber = int(sys.argv[1])
	if movieNumber != 1 and movieNumber != 2:
		raise IndexError
except IndexError:
	print 'Usage: python ' + sys.argv[0] + ' <1 or 2>'
	sys.exit(0)

myRegex = '^(\*\s)?([\w\s\W]+)\s(\d{4})\s([\w\s\W]+)$'

list1 = []
watchedNum = 0 
fh = open('jamesFinal.txt','r+') 
for line in fh: 
	match = re.match(myRegex,line) 
	watched = 0
	try:
		if match.group(1) is not None: 
			watched = 1
			watchedNum = watchedNum + 1
		temp = BondMovie(match.group(2),match.group(3),match.group(4).rstrip(),watched) 
		list1.append(temp)
	except AttributeError: 
		print "Regex Didnt Match anything"
		fh.close()
		sys.exit(0)

firstMovie = random.randint(0,len(list1)-1)
secondMovie = random.randint(0,len(list1)-1)
oneMovie = random.randint(0,len(list1)-1)

bailCount = 0
flag = 0
if watchedNum != len(list1): 
	if movieNumber == 2:
		while list1[firstMovie].watched == 1 or list1[secondMovie].watched == 1 or firstMovie == secondMovie:
			if list1[firstMovie].watched == 1: 
				firstMovie = random.randint(0,len(list1)-1)
			elif list1[secondMovie].watched == 1:
				secondMovie = random.randint(0,len(list1)-1)
			else:
				secondMovie = random.randint(0,len(list1)-1)
			bailCount = bailCount + 1
			if bailCount >= 1000000: 
				flag = 1 
				break
		if flag != 1:
			print 'The first Movie will be ' + list1[firstMovie].name + ' starring ' + list1[firstMovie].actor + ' and filmed in ' + list1[firstMovie].year
			print 'The second Movie will be ' + list1[secondMovie].name + ' starring ' + list1[secondMovie].actor + ' and filmed in ' + list1[secondMovie].year
		else:
			print "since there is an odd number of movies we only have 1 left..."
			if list1[secondMovie].watched == 1: 
				print 'The Movie will be ' + list1[firstMovie].name + ' starring ' + list1[firstMovie].actor + ' and filmed in ' + list1[firstMovie].year
			else:
				print 'The Movie will be ' + list1[secondMovie].name + ' starring ' + list1[secondMovie].actor + ' and filmed in ' + list1[secondMovie].year
		fh.seek(0)
		for x in range(len(list1)): 
			if list1[x].watched == 1 or x == firstMovie or x == secondMovie:
				fh.write('* ' + list1[x].name + ' ' + list1[x].year + ' ' + list1[x].actor + '\n')
			else:
				fh.write(list1[x].name + ' ' + list1[x].year + ' ' + list1[x].actor + '\n')
	else:
		while list1[oneMovie].watched == 1:
			oneMovie = random.randint(0,len(list1)-1)
		print 'The Movie will be ' + list1[oneMovie].name + ' starring ' + list1[oneMovie].actor + ' and filmed in ' + list1[oneMovie].year
		fh.seek(0)
		for x in range(len(list1)): 
			if list1[x].watched == 1 or x == oneMovie:
				fh.write('* ' + list1[x].name + ' ' + list1[x].year + ' ' + list1[x].actor + '\n')
			else:
				fh.write(list1[x].name + ' ' + list1[x].year + ' ' + list1[x].actor + '\n') 
	fh.truncate()
else: 
	print "WE HAVE WATCHED THEM ALL!!!!"
fh.close()
