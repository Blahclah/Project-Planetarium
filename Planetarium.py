import random
from Planet import Planet

class Planetarium(object):

 

    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(planet) for planet in self.planets) + ']'
        
    
    def create(self):
        self.planets = []
        
        for i in range(9):
            self.planets.append(Planet(i,i,i))
            
    def menu(self):
        answer = 10
        while(answer != 0):
            print("1: Mercury")
            print("2: Venus")
            print("3: Earth")
            print("4: Mars")
            print("5: Jupiter")
            print("6: Saturn")
            print("7: Uranus")
            print("8: Neptune")
            print("9: Pluto")
            print("0: Quit program")
            answer = int(input("Which planet's information do you want to see? "))
            print(self.planets[answer-1])
