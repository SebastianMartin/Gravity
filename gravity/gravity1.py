import random
import matplotlib.pyplot as plt
import pylab
import math



class Entity:     

	def __init__(self, name,x,y,mass,magnitude,initalMag):  
		self.name = name
		self.x = x   
		self.y = y
		self.mass = mass
		#force acting on the object proportional to the mass, aka the final movement 
		self.currentMag = magnitude
		self.initalMag = initalMag
		self.radius = (mass/math.pi)**.5

def getCurrentMag(cEntity,allEntities):
	x1 = cEntity.x
	y1 = cEntity.y
	mags = [0,0]
	for E in allEntities:
		x2 = E.x
		y2 = E.y
		distance = (((x2-x1)**2)+((y2-y1)**2))**.5
		if distance != 0:
			gravity = 9.82
			magnitude = gravity*((cEntity.mass*E.mass)/(distance**2))
			side1 = x2-x1
			side2 = distance
			acos = math.acos(side1/side2)
			if(y2-y1>0):
				theta = math.degrees(acos)
			else: 
				theta =-1* math.degrees(acos)
			adjacent = math.cos(math.radians(theta))*magnitude
			opposite =  math.sin(math.radians(theta))*magnitude
			mags[0]+=(adjacent/cEntity.mass)
			mags[1]+=(opposite/cEntity.mass)
	return mags



#plt.figure()
plt.figure(figsize=(10, 10))
ax = plt.gca()

Entities = []
mIm = 1
maxRange = 1000
ax.set_xlim([0, maxRange])
ax.set_ylim([0, maxRange])

for i in range(5000):
	x1 = random.uniform(0,maxRange)
	y1 = random.uniform(0,maxRange)
	#most tiny, barely any huge ones.
	mass1 = round(1/random.uniform(0, 2),3)
	magnitude1 = [0,0]
	initalMag = [0,0]#[1/random.uniform(-mIm, mIm),1//random.uniform(-mIm, mIm)]
	newEntity = Entity(i,x1,y1,mass1,magnitude1,initalMag)
	Entities.append(newEntity)


for E in Entities:
	E.currentMag = getCurrentMag(E,Entities)
	E.currentMag = [E.currentMag[0]+E.initalMag[0],E.currentMag[1]+E.initalMag[1]]
	E.radius = (E.mass/math.pi)**.5

	ax.quiver(E.x,E.y,E.currentMag[0],E.currentMag[1], angles='xy', scale_units='xy',scale=1, width=.002,color='b')
	circle = plt.Circle((E.x, E.y), E.radius,fill=False)#, color='y')
	ax.add_artist(circle)




xs = []
ys = []
names =[]
for o in Entities:
	xs.append(o.x)
	ys.append(o.y)
	names.append(o.mass)
plt.scatter(xs,ys,marker='.')
#for i, txt in enumerate(names):
#    ax.annotate(txt, (xs[i], ys[i]))
plt.show()
