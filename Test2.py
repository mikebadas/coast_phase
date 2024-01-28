import math
angle = 74.1*0.0174533
velocity = 2943
height = 83383
distance = 138597

for t in range(0, 57):

	velocity = math.sqrt(2*3.986*math.pow(10,14)*((1/(6378000+velocity*math.cos(angle)+height))
	-(1/(6378000+height)))+math.pow(velocity, 2))                                                # формула швидкості

	change = 6378000*velocity*math.sin(angle)/(6378000+height)                                   # формула темпу переміщення
	distance += change                                                                           # загальне переміщення

	angle += math.asin(math.sin(angle)*9.8/velocity) - 360*0.0174533*change/40000000             # формула кута

	height += velocity*math.cos(angle)                                                           # формула висоти

	print(angle/0.0174533, velocity, height, distance)

























#import math
#angle = math.acos(0.97)
#velocity = 1142
#height = 51631
##distance = 138597
#
#for t in range(0, 115):
#
#	velocity = math.sqrt(2*3.986*math.pow(10,14)*((1/(6378000+velocity*math.cos(angle)+height))
#	-(1/(6378000+height)))+math.pow(velocity, 2))                                                # формула швидкості
#
#	change = 6378000*velocity*math.sin(angle)/(6378000+height)                                   # формула темпу переміщення
#	#distance += change                                                                           # загальне переміщення
#
#	angle += math.asin(math.sin(angle)*9.8/velocity) - 360*0.0174533*change/40000000             # формула кута
#
#	height += velocity*math.cos(angle)                                                           # формула висоти
#
#	print(angle/0.0174533, velocity, height, distance)

