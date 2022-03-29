from random import randint, random

prix = int(input(print("choisir un nombre entre 0 et 1000")))
juste_prix = randint(0,1000)
while prix != juste_prix :
 if prix < juste_prix :
   prix = int(input(print("c'est plus retry")))
 else :
   prix = int(input(print("c'est moins retry")))
 
if prix == juste_prix :
   print("c'est gagné")

