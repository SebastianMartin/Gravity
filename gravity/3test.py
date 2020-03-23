import random
import matplotlib.pyplot as plt
import pylab
import math


class object:     
		
	# The init method or constructor  
	def __init__(self, name,x,y,mass,magnitude,initalMag):  
			
		# Instance Variable  
		self.name = name
		self.x = x   
		self.y = y
		self.mass = mass
		self.magnitude = magnitude
		self.initalMag = initalMag
		self.mm = [00.00,00.00]
		self.mm2 = [00.00,00.00]

	'''
	# Adds an instance variable   
	def setColor(self, color):  
		self.color = color  
		
	# Retrieves instance variable      
	def getColor(self):      
		return self.color '''
plt.figure()
ax = plt.gca()

objects = []
mIm = 3
maxRange = 10
ax.set_xlim([0, maxRange])
ax.set_ylim([0, maxRange])

for i in range(3):
	x1 = random.uniform(0,maxRange)
	y1 = random.uniform(0,maxRange)
	mass1 = random.uniform(0, 1)
	magnitude1 = []
	initalMag = [0,0]#[random.uniform(-mIm, mIm),random.uniform(-mIm, mIm)]
	newObject = object(i,x1,y1,1,magnitude1,initalMag)
	objects.append(newObject)
xs = []
ys = []
names = []
for o in objects:
	xs.append(o.x)
	ys.append(o.y)
	names.append(str(o.name)+' '+str(o.mass))



for o in objects:
	x1 = o.x
	y1 = o.y

	for o2 in objects:
		x2 = o2.x
		y2 = o2.y

		distance = (((x2-x1)**2)+((y2-y1)**2))**.5

		if distance !=0:
			print(x1,' ',y1)
			print(x2,' ',y2)
			g = 10

			magnitude = g*((o.mass*o2.mass)/(distance**2))

			side1 = x2-x1
			side2 = distance
			acos = math.acos(side1/side2)
			#theta = math.degrees(acos)
			if(y2-y1>0):
				theta = math.degrees(acos)
			else: 
				theta =-1* math.degrees(acos)
			print(theta)

			print(magnitude,'\t',o.name,' ',o2.name)
			adjacent = math.cos(math.radians(theta))*magnitude
			opposite =  math.sin(math.radians(theta))*magnitude
			o.magnitude.append([adjacent,opposite])
			#print(adjacent)
			print('-----------------')
	m2 = [0.00,0.00]
	print(o.magnitude)
	for x in o.magnitude:
		m2[0]+=x[0]
		m2[1]+=x[1]
	o.mm = m2
	m3 = m2.copy()
	m3[0] += o.initalMag[0]
	m3[1] += o.initalMag[1]
	o.mm2 = m3
	






for o in objects:
	ax.quiver(o.x,o.y,o.mm[0],o.mm[1], angles='xy', scale_units='xy', scale=1,color='b')
	ax.quiver(o.x,o.y,o.mm2[0],o.mm2[1], angles='xy', scale_units='xy', scale=1,color='y')
	ax.quiver(o.x,o.y,o.initalMag[0],o.initalMag[1], angles='xy', scale_units='xy', scale=1,color='g')
	for mags in o.magnitude:
		ax.quiver(o.x,o.y,mags[0],mags[1], angles='xy', scale_units='xy', scale=1,color='r')

#for i in range(len(xs)):
#	ax.quiver(xs[i],ys[i],1,1, angles='xy', scale_units='xy', scale=1)


plt.scatter(xs,ys)
for i, txt in enumerate(names):
    ax.annotate(txt, (xs[i], ys[i]))

plt.show()








































