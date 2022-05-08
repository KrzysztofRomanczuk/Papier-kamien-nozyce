import random

def gra():
     gracz = input("Zagrajmy w gre papier, kamień, nożyce \n" 
                   "Co wybierasz? \n "
                   "'p' for papier, 'k' for kamien, 'n' for nozyce\n")
     komputer = random.choice(['p','k','n'])

     if gracz == komputer:
        return 'Remis!'

     if win(gracz,komputer):
        return 'Wygrałeś!'

     return 'Przegrałeś!'

def win(uczestnik,przeciwnik):
        if (uczestnik == 'k' and przeciwnik == "n") or (uczestnik == 'n' and przeciwnik == 'p') \
        or (uczestnik == 'p' and przeciwnik == 'r'):
         return True
print(gra())
