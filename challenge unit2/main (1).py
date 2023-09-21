#define the basss class player
class player:
  def play(self):
   print("the plyeris playing cricket.")
   # define the derived class batsman
class batsman(player):
  def play(self):
   print("the batsman is batting.")
   #definethe derived class bowler
class bowler(player):
  def play(self):
   print("the bowler is bowling.")
   #create objects of batsman nd bowle classes
Batsman =batsman()
Bowler=bowler()
#call the play()method for each object
Batsman.play()
Bowler.play()