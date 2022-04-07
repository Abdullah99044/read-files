import yaml
from yaml import Loader

yaml_file = open('settings.yml' , 'r' )  
data = yaml.load(yaml_file, Loader=Loader)

print(data)

bolletjes = data['bolletjes']

hoorentjes = data['hoorentjes']

bakjes = data['bakjes']

toppings = data['toppings']
 
liter = data['liter']

btw = data['btw']

#Functions

Bol = "bolletjes" #Global scope


def sorryFunction(): #Print dit zin als de klant heeft iets fout gekozen
    print(".........................")
    print("Sorry dat is geen optie die we aanbieden...")
    print(".........................")

def stap_3_Function(n , y ):
    print("Hier is uw " , y , " met " , n , "bolletje(s)" )

def eindeFunction(): #Dit function laat de klant nog een keer bestellen
    print("Wilt u nog meer bestellen?") 
    while True: 
        answer5 = input("(Y/N) :")  
        if answer5 == "Y" :
            print("....................")
            print("Terug naar het begin")
            programFunction()  
        elif answer5 == "N" :
            print("Bedankt en tot ziens!") 
            return  
        else :
            sorryFunction()      

def smakenFuction(x): #Hier zit de smaken 
    z = 1
    for i in range(x):
        while True:
            print("Welke smaak wilt u voor " , Bol , " nummer?" , z)
            print("A) Aardbei")
            print("C) Chocolade")
            print("V) Vanille?")
            
            k = input("A , C  , OF V ? : ")
            if k == "A" or "C" or "V"  :
                z += 1
                break
            else:
                print("Sorry dat snap ik niet...")

def bonenFunction(x , y , z , i , n , c): #Dit function reken de prijzen om een bonen te maken 
    global    bolletjes , hoorentjes , bakjes  , liter , btw  

    bolletjes_prijs = x * bolletjes
    hoorentjes_prijs = y * hoorentjes
    bakjes_prijs = z * bakjes
    toppings_prijs = i * 1

    total = bolletjes_prijs + hoorentjes_prijs + bakjes_prijs + i  
    if c == "C" and i > 0.3 :
        n = x
    print("----------[Papi Gelato]----------")
    print("Bolletjes  ", x , " x " " € 0,95   =","€",bolletjes_prijs )
    print("Horrentjes ", y , " x " " € 1,25   =","€",hoorentjes_prijs )
    print("Bakjes     ", z , " x " " € 0,75   =","€",bakjes_prijs)
    print("Topping    ", n , " x " ,"€",i , "   =","€",toppings_prijs )
    print("                          ----- +")
    print("Total                    =", "€",float(total))

def zakelijk_bonen(x): #Zakelijk bonen
    liter_prijs = x * liter
    btw = liter_prijs / 100 * btw
    print("----------[Papi Gelato]----------")
    print("Liter  ", x , " x " " € 9.8   =","€",liter_prijs)
    print("                          ----- +")
    print("Total                    =", "€", liter_prijs)
    print("BTW 6%                   =", "€", float(btw))
    return

def knopF():
    TreugGaan = input("Druk op een knop om treug te gaan naar het begin")
    
def toppingFunction(i , n , A): #Dit function output de prijs van topping
    global toppings

    if  A == "A" :
        return 0
    elif A == "B" :
        return toppings['slagroom']
    elif A == "C" :
        return 0.3 * n 
    elif A == "D" and i == 2:
        return toppings['caramel']['bakje'] * n
    elif A == "D" and i == 1:
        return toppings['caramel']['hoorentje'] * n
    elif A == 'E':
        return toppings['bottetjes']  * n 

    
def toppingFunction1(): #Dit is topping lijst
    print("Wat voor topping wilt u: ")
    print(" A) Geen ")
    print(" B) Slagroom" )
    print(" C) Sprinkels ( prijs x aantal bolletjes ")
    print(" D) Caramel Saus ")
    print(" E) bottetjes ")

def programFunction(): #Het programma
    while True:
        print(".........................")
        print("Bent u")
        print("1) particulier")
        print("2) zakelijk")
        an = input("1/2 :")
        if an == "1" :
            print(".........................")
            answer = int(input("Hoeveel bolletjes wilt u? : "))
            print(".........................")
            if answer <= 4 :
                smakenFuction(answer) 
                print("Wilt u deze " , answer , " bolletje(s) in")
                print("A) een hoorntje? ")
                print("B) of een bakje?")
                while True:
                    answer1 = input("A/B")
                    if answer1 == "A":
                        stap_3_Function(answer , "hoorntje") 
                        if answer != 0: 
                            toppingFunction1()
                            answer2 = input(" : ")
                            bonenFunction(answer , 1 , 0 , toppingFunction(1 , answer , answer2), 1 , answer2)
                        eindeFunction()
                        break          
                    elif answer1 == "B":
                        stap_3_Function(answer , "bakje")
                        if answer != 0: 
                            toppingFunction1()
                            answer2 = input(" : ")
                            bonenFunction(answer , 0 , 1 , toppingFunction(2, answer , answer2) , 1  , answer2 )
                        eindeFunction()
                        break
                    else:
                        sorryFunction()
                break
            elif answer > 4 and answer <= 8:
                print("..........................................................")
                print("Dan krijgt u van mij een bakje met " , answer , "bolletjes")
                smakenFuction(answer)
                if answer != 0: 
                    toppingFunction1()
                    answer2 = input(" : ")
                    bonenFunction(answer , 0 , 1 , toppingFunction(2, answer , answer2) , 1  , answer2 )
                eindeFunction()
                break
            elif answer > 8:
                    print("........................................")
                    print("Sorry, zulke grote bakken hebben we niet")
                    print("........................................")
                    knopF()
            else :
                sorryFunction()
                knopF()
        elif an == "2":
            global Bol
            Bol = "Liter"
            print(".........................")
            answer = int(input("Hoeveel lite wilt u? : "))
            print(".........................")
            smakenFuction(answer)
            zakelijk_bonen(answer)
            break
        else:
            sorryFunction()
            knopF()

#Programma

print("................................................................................")
print("Welkom bij Papi Gelato")
print("................................................................................")
next = input("druk op een knop om door te gaan")
programFunction()






