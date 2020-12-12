import pandas as pd
import numpy as np
import random
import math

def get_advantage_and_disadvantage(STR, CON, DEX, INT, WIS, CHA):
      advantage=1
      disadvantage=1
      if STR>12:
       advantage+=(STR-12)*2
      if CON>12:
       advantage+=(CON-12)*2
      if CHA>12:
       advantage+=(CHA-12)*2
      if INT>12:
       advantage+=(INT-12)*2
      if WIS>12:
       advantage+=(WIS-12)*2
      
      if STR<8:
       disadvantage+=(8-STR)*3
      if CON<8:
       disadvantage+=(8-CON)*3
      if CHA<8:
       disadvantage+=(8-CHA)*3
      if INT<8:
       disadvantage+=(8-INT)*3
      if WIS<8:
       disadvantage+=(8-WIS)*3
      
      if STR>CON:
       disadvantage+=2
      if INT>WIS:
       disadvantage+=2
      if CHA>16:
       advantage+=5
      
      
      return advantage, disadvantage

def succeed_or_fail(adv, dis):
 return random.choice(["succeed"]*adv+["fail"]*dis)


if __name__ == '__main__':
 print("default")
 advantage, disadvantage = get_advantage_and_disadvantage(6,14,13,13,12,4)
 print([advantage, disadvantage])
 
 print("optimized")
 advantage, disadvantage = get_advantage_and_disadvantage(8,14,13,13,16,8)
 print([advantage, disadvantage])
 
 print("anti-optimized")
 advantage, disadvantage = get_advantage_and_disadvantage(6,14,20,17,12,4)
 print([advantage, disadvantage])
 
 print("anti-optimized II")
 advantage, disadvantage = get_advantage_and_disadvantage(9,14,20,13,12,4)
 print([advantage, disadvantage])
 
 print("straggler-saving only")
 advantage, disadvantage = get_advantage_and_disadvantage(10,14,13,13,12,10)
 print([advantage, disadvantage])
 
 print("dex-dodging only")
 advantage, disadvantage = get_advantage_and_disadvantage(8,16,13,15,14,6)
 print([advantage, disadvantage])

 print(succeed_or_fail(10,20))
 print(succeed_or_fail(10,2000))
