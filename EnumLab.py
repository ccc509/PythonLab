import enum
from University import University
	
u = University['Cambridge']


	
d = 'Imperial'

if University[d] in (University.Imperial, University.Cambridge):
	print("Good University")
else:
	print("Rubbish School")
