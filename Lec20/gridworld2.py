

import numpy as np
WORLD_SIZE = 4
REWARD= -1.0
ACTION_PROB = 0.25

world = np.zeros((WORLD_SIZE,WORLD_SIZE))
policy  = np.zeros((WORLD_SIZE,WORLD_SIZE))
actions = ['L','U','R','D']

nextState = []
for i in range(0,WORLD_SIZE):
	nextState.append([])
	for j in range(WORLD_SIZE):
		nextS = dict()
		if i==0:
			nextS['U'] = [i,j]
		else:
			nextS['U'] = [i-1,j]

		if i == WORLD_SIZE -1:
			nextS['D'] = [i,j]
		else:
			nextS['D'] = [i+1,j]

		if j==0:
			nextS['L'] = [i,j]
		else:
			nextS['L'] = [i,j-1]

		if j==WORLD_SIZE - 1:
			nextS['R'] = [i,j]
		else:
			nextS['R'] = [i,j+1]


		nextState[i].append(nextS)

states = []
for i in range(0,WORLD_SIZE):
	for j in range(0,WORLD_SIZE):
		if (i==0 and j==0 ) or (i == WORLD_SIZE -1 and j==WORLD_SIZE -1):
			continue
		else:
			states.append([i,j])



while True:

	newWorld = np.zeros((WORLD_SIZE,WORLD_SIZE))

	for i,j in states:
		for action in actions:
			newPosition = nextState[i][j][action]
			newWorld[i,j] += ACTION_PROB*(REWARD + world[newPosition[0],newPosition[1]])
			print(newWorld)

	if np.sum(np.abs(world - newWorld)) < 1e-4:
		print('Work Over')
		print(newWorld)
		break
	world = newWorld



for i,j in states:
	max_value = -500
	curr_action = 0
	index = 0
	for action in actions:
		newPosition = nextState[i][j][action]
		value = REWARD + world[newPosition[0],newPosition[1]]
		if max_value < value:
			max_value = value
			curr_action = index
		index = index + 1
	policy[i,j] = curr_action
print('Best Policy')
print(policy)










