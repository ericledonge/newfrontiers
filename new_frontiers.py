import random
#import console

#console.clear()
#console.set_font('Verdana', 16)

def setup():

    '''Fonction d'initialisation du jeu'''

    output = ''

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

    output += 'Tuile A: ' + random.choice(tuileA)
    output += '<br>Tuile B: ' + random.choice(tuileB)
    output += '<br>Tuile C: ' + random.choice(tuileC)
    output += '<br>Tuile D: ' + random.choice(tuileD)
    output += '<br>Tuile E: ' + random.choice(tuileE)
    output += '<br>Tuile F: ' + random.choice(tuileF)
    output += '<br>Tuile G: ' + random.choice(tuileG)
    output += '<br>Tuile H: ' + random.choice(tuileH)
    output += '<br>Tuile I: ' + random.choice(tuileI)
    output += '<br>Tuile J: ' + random.choice(tuileJ)
    output += '<br>Tuile K: ' + random.choice(tuileK)
    output += '<br>Tuile L: ' + random.choice(tuileL)
    output += '<br>Tuile M: ' + random.choice(tuileM)
    output += '<br>Tuile N: ' + random.choice(tuileN)
    output += '<br>Tuile O: ' + random.choice(tuileO)
    output += '<br>Tuile P: ' + random.choice(tuileP)

    player1Board = random.choice(playerBoards)
    playerBoards.remove(player1Board)
    player2Board = random.choice(playerBoards)

    output += '<br><br>Eric: ' + str(player1Board)
    output += '<br>Noémie: ' + str(player2Board)

    startingPlayer = ['Eric', 'Noémie']

    output += '<br><br>Starting player: ' + str(random.choice(startingPlayer))
    
    return output
    