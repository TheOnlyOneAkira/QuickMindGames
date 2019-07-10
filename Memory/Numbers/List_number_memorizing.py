from random import randint
from copy import deepcopy


"""

  [FR]
Le but de ce jeu est d'apprendre
a retenir une suite de nombre de
facon approximative afin de retrouver
la valeur (pas l'emplacement) du
nombre retiré.

Vous pouvez modifier la longueur
(difficulté) en modifiant la valeur
de size_of_set.

  [EN]
This game goad is to enhance your
memory ability: you will have to
remind a suite of number, one will
be deleted and the list will be
told again. You have to find the
value (not the position) of this
deleted number.

You can change difficulty by changing
the size_of_set value.

"""

size_of_set = 100






full_set = []
modified_set = []

for i in range(size_of_set):
  full_set.append( randint(0,9) )

modified_set = deepcopy(full_set)
poped = modified_set.pop( randint( 0,len(modified_set)-1 ) )


input("pret ?")
for i in range(len(full_set)):
  print( "\n"*100, "* "*(i)   +str(full_set[i])+" "+   "* "*(len(full_set)-i-1) )
  input()

print( ("="*10+"\n")*3 )

input("on passe a la suite ?")
for i in range(len(modified_set)):
  print( "\n"*100, "* "*(i)   +str(modified_set[i])+" "+   "* "*(len(modified_set)-i-1) )
  input()

print( ("="*10+"\n")*3 )

r = input("reponse ? => ")
print( int(r)==poped )
print("la valeur est :",poped)
