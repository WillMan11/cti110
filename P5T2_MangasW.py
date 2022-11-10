# CTI 110
# P5T2 Offense
# MangasW
# 10/11/2022
import random

# very simple basketball play simulator.
def offense():
  """
  offense() - simulates one play in basketball
  arguments: none
  returns: none
  """
  print("You're on offense.")
  print("Type pass or shoot.")
  command = input("> ")
  print("You chose", command)
  if command == "shoot":
    # can score or miss
    # score -> other team takes possession
    # miss -> random chance who gets it
    print("He shoots...")
    # 50/50 chance
    roll = random.randint(1, 100)
    print("rolled", roll)
    if roll >= 50:
      print("...and it's good! 2 points!")
      # hand over possession
      return
    else:
      print("...it's no good!")
      # for now, turnover
      return
    
  if command == "pass":
    # either success, or turnover
    print("Ball passed...")
    # keep going
    offense()
    

def main():
  print("Now simulating one play.")
  offense()
  
# start program
main()
