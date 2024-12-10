import random

class pokemon:

    power = 0
    health = 0.0
    speed = 0
    defence = 0
    offence  = 0
    name = ""

    def __init__(self, power, health, speed, defence, offence, name):
        self.power = power
        self.health = health
        self.speed = speed
        self.defence = defence
        self.offence = offence
        self.name = name

    def dodge(self):
        print(self.speed)

    def attack(self):
        print(self.name, "is attacking")

    def agility(self):
        print(self.name, "is getting agilized")

    def defence(self):
        print(self.name, "is defending")

    def offencing(self):
        print(self.name, "is offending")

    def name(self):
        print(self.name)

    def myfunc(self):
        print("Hello my name is " + self.name)

Earthquake = pokemon(4, 60, 5, 4, 3, "Earthquake")
Tornado = pokemon(7, 80, 6, 5, 8, "Tornado")
Wildfire = pokemon(3, 50, 4, 7, 5, "Wildfire")
Tsunami = pokemon(8, 90, 5, 8, 7, "Tsunami")
ChosenPokemon = pokemon(0, 0, 0, 0, 0, " ")

Pokemen = [Earthquake, Tornado, Wildfire, Tsunami]

randinteger = random.randint(0, (len(Pokemen) - 1))

print(
"""\n
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
""")


AIChosenPokemon = Pokemen[randinteger]

inputtedPokemon = int(input("Enter a number to choose a pokemon - (1: Earthquake), (2:Tornado), (3:Wildfire), (4:Tsunami): "))

while randinteger == inputtedPokemon:

    print("Enter another number, the pokemon has been chosen.")

    inputtedPokemon = int(input("Enter a number to choose a pokemon - (1: Earthquake), (2:Tornado), (3:Wildfire), (4:Tsunami): "))

HumanChosenPokemon = Pokemen.index[(inputtedPokemon - 1)]

print("Human pokemon chosen: ", HumanChosenPokemon.myfunc())
print(randint)
print("AI opponent pokemon chosen: ", AIChosenPokemon.myfunc())

