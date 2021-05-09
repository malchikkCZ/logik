# Na motivy hry Logik naprogramoval Malchikk.CZ (C) 2021-03-14

import sys
import os
from random import randint

def cls():
  '''Tato funkce smaze obrazovku v ruznych OS.'''
  os.system('cls' if os.name=='nt' else 'clear')

def checkAnsw(x,y):
  '''Tato funkce vyhodnoti odpoved a urci napovedu pro hrace.'''  
  bkScore = 0                                   # tady se budou pocitat umistena cisla
  whScore = 0                                   # tady se budou pocitat uhadnuta cisla
  newY = []
  newX = []                                     # tady se budou ukladat cisla ktere nebyly spravne umistene pro dalsi pouziti         

  for i in range(4):
    if x[i] == y[i]:                            # nejprve se urci pocet spravne umistenych cisel
      bkScore +=1
    else:                                       # dvojice cisel, ktera nebyla spravne umistena, se ulozi do seznamu newX a newY
      newX.append(x[i])
      newY.append(y[i])
  
  for j in range(len(newX)):                    # nyni budeme pracovat pouze se zbylymi cisly
    if newY[j] in newX:                         # nejprve pro kazde cislo v odpovedi zjistime, zda je obsazeno v generovanem cisle
      cntX = newX.count(newY[j])
      cntY = newY.count(newY[j])                # pokud ano, porovname kolikrat se vyskytuje v jednotlivych seznamech newX a newY
      if cntY > cntX:
        newY[j] = 0                             # pokud je v odpovedi vickrat nez v zadani, prepiseme ho v odpovedi na 0 a preskocime
      else:
        whScore +=1                             # v opacnem pripade zapocitame odpoved
                                                # tenhle druhy cyklus zajisti, ze se nebude jedno cislo pocitat vicekrat
  hint = bkScore*"X " + whScore*"O "
  return hint                                   # programu posleme zpatky vysledek


cls()

print("+--+                       +--+")
print("|  |                   ++  |  |")
print("|  |    /----\\ /----\\ +--+ |  | __")
print("|  |    | /\\ | | /\\ | |  | |  |/ /")
print("|  +--+ | \\/ | | \\/ | |  | |  |\\ \\")
print("+-----+ \\----/ \\--+ | +--+ +--+ \\_\\")
print("                 /_/")
print()

print("Musis uhadnout 4-mistny kod sestaveny z cislic od 1 do 8. Jednotlive cislice se mohou opakovat.")
print("Pocitac ti vzdy napovi, jak jsi tipoval. X = spravne umistene cislo, O = spravne uhodnute cislo.")
print("Na uhodnuti kodu mas celkem 10 pokusu. Cislice ve svem tipu oddeluj mezerou.")
print()

logik = [randint(1, 8) for p in range(4)]                               # vygeneruje seznam 4 celych cisel v rozsahu 1 az 8 

answer = []                                                             # definuje prazdny seznam odpovedi

for i in range(1, 11):                                                  # na uhodnuti ma hrac 10 pokusu
  while len(answer) != 4 or min(answer)<1 or max(answer)>8:             # program ceka na odpoved, dokud nebude splnovat podminku
    answer = [int(x) for x in input(f"Pokus c.{i:2}>>> ").split()]      # program ocekava cele cisla, jinak spadne :(
    
  if answer == logik:                                                   # pokud odpoved souhlasi se zadanim, nic se nepocita a hrac vyhrava
    print("             ", "X X X X")
    print("\nVyhral jsi, skvele! Uhodl jsi cislo:", end=" ")
    print(logik)
    sys.exit()
  else:                                                                 # v opacnem pripade se jde do podprogramu checkAnsw nahore
    hint = checkAnsw(logik,answer)
    print("             ", hint)                                        # a vytiskne se vyhodnoceni (napoveda)
  
  answer = []                                                           # musime znovu vycistit seznam odpovedi

print("\nVycerpal jsi vsechny pokusy, spravna odpoved byla:", end=" ")
print(logik)                                                            # pokud hrac neuhodne v 10 pokusech, hra konci