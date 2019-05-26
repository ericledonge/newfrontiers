import random
import console

console.clear()
console.set_font('Verdana', 16)

tuileA = ['Expeditionary Force', 'Survey Team'] 
tuileB = ['Export Duties', 'Mining Robots']
tuileC = ['Alien Monument', 'Alien Researchers']
tuileD = ['Terraforming Engineers', 'Terraforming Specialists']
tuileE = ['Diversified Economy', 'Investment Credits']
tuileF = ['Improved Logistics', 'Terraforming Robots']
tuileG = ['Drop Ships', 'Galactic Salon']
tuileH = ['Technology Investors', 'Trade League']
tuileI = ['Free Trade Association', 'Pan-Galactic Hologrid']
tuileJ = ['Imperium War Profiteers', 'Mining League']
tuileK = ['Military Industry', 'New Galactic Order']
tuileL = ['Alien Tech Institute', 'Galactic Exchange']
tuileM = ['Pan-Galactic League', 'Uplift Gene Hunters']
tuileN = ['Galactic Imperium', 'Imperium Lords']
tuileO = ['Federation Survey', 'Frontier Settlers']
tuileP = ['Galactic Federation', 'New Economy']

playerBoards = [1, 2, 3, 4, 5, 6, 7, 8]

print('Tuile A: ' + random.choice(tuileA))
print('Tuile B: ' + random.choice(tuileB))
print('Tuile C: ' + random.choice(tuileC))
print('Tuile D: ' + random.choice(tuileD))
print('Tuile E: ' + random.choice(tuileE))
print('Tuile F: ' + random.choice(tuileF))
print('Tuile G: ' + random.choice(tuileG))
print('Tuile H: ' + random.choice(tuileH))
print('Tuile I: ' + random.choice(tuileI))
print('Tuile J: ' + random.choice(tuileJ))
print('Tuile K: ' + random.choice(tuileK))
print('Tuile L: ' + random.choice(tuileL))
print('Tuile M: ' + random.choice(tuileM))
print('Tuile N: ' + random.choice(tuileN))
print('Tuile O: ' + random.choice(tuileO))
print('Tuile P: ' + random.choice(tuileP))

player1Board = random.choice(playerBoards)
playerBoards.remove(player1Board)
player2Board = random.choice(playerBoards)

print('Player 1: ' + str(player1Board))
print('Player 2: ' + str(player2Board))

startingPlayer = ['Player 1', 'Player 2']

print('Starting player: ' + str(random.choice(startingPlayer)))