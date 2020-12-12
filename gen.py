import pandas as pd
import numpy as np
import random
import math

import calc_win_chances

random.seed(0)

def generate(N):
    dictForDf = {}

    dictForDf["str"]=[]
    dictForDf["con"]=[]
    dictForDf["dex"]=[]
    dictForDf["cha"]=[]
    dictForDf["int"]=[]
    dictForDf["wis"]=[]
    
    dictForDf["result"]=[]

    df=pd.DataFrame(dictForDf)

    for i in range(N):
     newSTR = random.choice([1,2,3,4,5,6,7,8,9,10])+random.choice([1,2,3,4,5,6,7,8,9,10])
     newCON = random.choice([1,2,3,4,5,6,7,8,9,10])+random.choice([1,2,3,4,5,6,7,8,9,10])
     newDEX = random.choice([1,2,3,4,5,6,7,8,9,10])+random.choice([1,2,3,4,5,6,7,8,9,10])
     newCHA = random.choice([1,2,3,4,5,6,7,8,9,10])+random.choice([1,2,3,4,5,6,7,8,9,10])
     newINT = random.choice([1,2,3,4,5,6,7,8,9,10])+random.choice([1,2,3,4,5,6,7,8,9,10])
     newWIS = random.choice([1,2,3,4,5,6,7,8,9,10])+random.choice([1,2,3,4,5,6,7,8,9,10])

     totalPoints = newSTR + newCON + newDEX + newCHA + newINT + newWIS
     if totalPoints>=60:
      adv, dis = calc_win_chances.get_advantage_and_disadvantage(newSTR, newCON, newDEX, newINT, newWIS, newCHA)
      result = calc_win_chances.succeed_or_fail(adv,dis)
      dictToAppend = {"str":newSTR,"con":newCON,"dex":newDEX,"cha":newCHA,"int":newINT,"wis":newWIS, "result":result}
      df = df.append(dictToAppend, ignore_index=True)
    return df


if __name__ == '__main__':
 theDf=generate(10000)
 print(theDf)
 print len(theDf[theDf["result"]=="succeed"])
 theDf.to_csv("d_and_d.csv")
