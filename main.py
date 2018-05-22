###
#Class: Player
#Summary: Holds player name and keeps score
####
class player:
  def __init__(self,name):
    self.name=name
    self.score=0
  def __str__(self):
    return (str(self.name)+":"+str(self.score))
  ####
  #Function: addScore
  #Summary: Adds one to the score
  ####
  def addScore(self):
    self.score+=1
  ####
  #Function: subScore
  #Summary: Subtracts one from the score
  ####
  def subScore(self):
    self.score-=1
  
####
#Function: findPlayer
#Summary: Finds a player given a list and the name of the player
####
def findPlayer(array,name):
  for p in array:
    if(p.name == name):
      return p
      
inputSTR = input("Please Enter Your Score Code:")
players=[]

#Finds distinct letters in the input
possiblePlayers=[]
for char in inputSTR.lower():
  if not char in possiblePlayers:
    possiblePlayers.append(char)
#Creates instances of all players, adds them to players list
for possiblePlayer in possiblePlayers:
  tempPlayer=player(possiblePlayer)
  players.append(tempPlayer)

#Adds or removes score depending on letter case
for char in inputSTR:
  if char == char.upper():
    findPlayer(players,char.lower()).addScore()
  else:
    findPlayer(players,char).subScore()

for p in players:
  print(p)
