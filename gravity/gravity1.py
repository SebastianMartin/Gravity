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
		self.initalMag = initalMag
		self.currentMag = magnitude
		self.movement = [self.currentMag[0]/self.mass,self.currentMag[1]/self.mass]
		self.radius = (mass/math.pi)**.5

def getCurrentMag(cEntity,allEntities):
	secondSplit = 1
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
			mags[0]+=((adjacent/1)/secondSplit)#cEntity.mass
			mags[1]+=((opposite/1)/secondSplit)
	return mags
#main is the one that will absorb secondary.
def CobineNodes(MainEntity,SecondaryEntity,allEntities):
	print(MainEntity.mass)
	print(SecondaryEntity.mass)

#plt.figure()
plt.figure(figsize=(10, 10))
ax = plt.gca()

Entities = []
mIm = 1
maxRange = 10
ax.set_xlim([0, maxRange])
ax.set_ylim([0, maxRange])

for i in range(20):
	x1 = random.uniform(0,maxRange)
	y1 = random.uniform(0,maxRange)
	#most tiny, barely any huge ones.
	mass1 = round(1/random.uniform(0, 5),3)
	magnitude1 = [0,0]
	initalMag = [0,0]#[random.uniform(-mIm, mIm),random.uniform(-mIm, mIm)]
	newEntity = Entity(i,x1,y1,mass1,magnitude1,initalMag)
	Entities.append(newEntity)
xs = []
ys = []
names =[]
for o in Entities:
	xs.append(o.x)
	ys.append(o.y)
	names.append(o.mass)
plt.scatter(xs,ys,marker='.')
for i, txt in enumerate(names):
    ax.annotate(i, (xs[i], ys[i]))
Entities.sort(key=lambda x: x.mass, reverse=True)
for E in Entities:
	print(E.name,E.mass)
for E in Entities:
	E.currentMag = getCurrentMag(E,Entities)
	E.currentMag = [E.currentMag[0]+E.initalMag[0],E.currentMag[1]+E.initalMag[1]]
	E.radius = (E.mass/math.pi)**.5
	E.movement = [E.currentMag[0]/E.mass,E.currentMag[1]/E.mass]

	ax.quiver(E.x,E.y,E.movement[0],E.movement[1], angles='xy', scale_units='xy',scale=1, width=.002,color='b')
	circle = plt.Circle((E.x, E.y), E.radius,fill=False)#, color='y')
	ax.add_artist(circle)



plt.savefig('1.pdf')
plt.show()


for E in Entities:
	combineNodes = {}
	encasedNodes = {}
	x1 = E.x
	y1 = E.y
	mags = [0,0]
	for E2 in Entities:
		if E.name != E2.name:
			x2 = E2.x
			y2 = E2.y
			distance = (((x2-x1)**2)+((y2-y1)**2))**.5
			if (distance+E2.radius)<E.radius:
				if E.name in encasedNodes:
					encasedNodes[E.name].append(E2.name)
				else:
					encasedNodes[E.name] = [E2.name]
			elif distance < E.radius+E2.radius:
				print(E.name,"\t",E2.name)
				if(E2.mass < E.mass):
					if E.name in combineNodes:
						combineNodes[E.name].append(E2.name)
					else:
						combineNodes[E.name] = [E2.name]
					print("combine too: ",E.name)
	print(combineNodes)
	print(encasedNodes)
