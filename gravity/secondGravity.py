import random
import matplotlib.pyplot as plt
import pylab
import math
import json
import pprint

def makeEntity(x,y,mass,initalForce,currentForce):
	newEntity = {}
	newEntity['x'] = x
	newEntity['y'] = y
	newEntity['mass'] = mass
	newEntity['initalForce'] = initalForce
	newEntity['currentForce'] = currentForce

	newEntity['movement'] = {'x':currentForce['x']/mass,'y':currentForce['y']/mass}
	newEntity['radius'] = (mass/math.pi)**.5
	return newEntity
def getCurrentMag(cEntity,allEntities):
	secondSplit = 1
	x1 = cEntity['x']
	y1 = cEntity['y']
	mags = {'x':0,'y':0}
	for keys in Entities.keys():
		E = Entities[keys]
		x2 = E['x']
		y2 = E['y']
		distance = (((x2-x1)**2)+((y2-y1)**2))**.5
		if distance != 0:
			gravity = 9.82
			magnitude = gravity*((cEntity['mass']*E['mass'])/(distance**2))
			side1 = x2-x1
			side2 = distance
			acos = math.acos(side1/side2)
			if(y2-y1>0):
				theta = math.degrees(acos)
			else: 
				theta =-1* math.degrees(acos)
			adjacent = math.cos(math.radians(theta))*magnitude
			opposite =  math.sin(math.radians(theta))*magnitude
			mags['x']+=((adjacent/1)/secondSplit)#cEntity.mass
			mags['y']+=((opposite/1)/secondSplit)
	return mags
def printJSON(jsonToPrint):
	json_formatted_str = json.dumps(jsonToPrint, indent=2)
	print(json_formatted_str)




Entities = {}
EntityCount = 10
plt.figure(figsize=(10, 10))
ax = plt.gca()
mIm = 1
maxRange = 10
ax.set_xlim([0, maxRange])
ax.set_ylim([0, maxRange])

for i in range(EntityCount):
	x = random.uniform(0,maxRange)
	y = random.uniform(0,maxRange)
	#most tiny, barely any huge ones.
	mass = round(1/random.uniform(0.01, 5),3)
	currentForce = {'x':0,'y':0}
	initalForce= {'x':0,'y':0}#{'x':random.uniform(-mIm, mIm),'y':random.uniform(-mIm, mIm)}
	Entities[i] =  makeEntity(x,y,mass,initalForce,currentForce)
printJSON(Entities)

xs = []
ys = []
names =[]

for keys in Entities.keys():
	CurrentData = Entities[keys]
	xs.append(CurrentData['x'])
	ys.append(CurrentData['y'])
	names.append(CurrentData['mass'])

plt.scatter(xs,ys,marker='.')
for i, txt in enumerate(names):
    ax.annotate(i, (xs[i], ys[i]))
for keys in Entities.keys():
	E = Entities[keys]
	E['currentForce']  = getCurrentMag(E,Entities)
	E['movement']['x'] = E['currentForce']['x']/E['mass']
	E['movement']['y'] = E['currentForce']['y']/E['mass']
	ax.quiver(E['x'],E['y'],E['movement']['x'],E['movement']['y'], angles='xy', scale_units='xy',scale=1, width=.002,color='b')
	circle = plt.Circle((E['x'], E['y']), E['radius'],fill=False)#, color='y')
	ax.add_artist(circle)
	ax.add_artist(circle)
printJSON(Entities)

EntitiesSorted = sorted(Entities.items(), key=lambda x: x[1]['mass'],reverse=True)
for e,x in EntitiesSorted:
	print(e)



plt.show()