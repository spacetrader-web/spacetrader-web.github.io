from random import random, randint

class Universe():
    techLevels = ['Pre-Agriculture', 'Agriculture', 'Medieval', 'Renaissance', 'Early Industrial', 'Industrial', 'Post-Industrial', 'Hi-Tech']
    planetNames = [ "Aldea", "Andevian", "Antedi", "Balosnee", "Baratas", "Daled", "Damast","Davlos","Deneb","Deneva"]
    #locations = []
    planets = []


    def makeUniverse(self):

        for x in range(len(self.planetNames)):

            planetName = self.planetNames[x]
            planetLocation = Location(randint(0,150), randint(0,150))
            techLevel = self.techLevels[randint(0, len(self.techLevels) - 1)]

            planet = Planet(planetName, planetLocation, techLevel)

            self.planets.append([x, planet.serializePlanet()])


        return self.planets

    def __str__(self):
        result = ''
        for x in planets:
            result += "Planet: " + x.planetName
            result += "Location" + str(x.location)
            result += "Tech Level" + str(x.techLevel)
        return result
    def __repr__(self):
        result = ''
        for x in planets:
            result += "Planet: " + x.planetName
            result += "Location" + str(x.location)
            result += "Tech Level" + str(x.techLevel)
        return result








class Location():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        result = "(" + str(self.x) + ", " + str(self.y) + ")"
        return result
    def __repr__(self):
        result = "(" + str(self.x) + ", " + str(self.y) + ")"
        return result
    def serializeLocation(self):
        locationDict = {
            'x':self.x,
            'y':self.y
        }
        return locationDict



class Planet():

    planetName = ''
    location = ''
    techLevel = ''
    def __init__(self, planetName, location, techLevel ):
        self.planetName = planetName
        self.location = location
        self.techLevel = techLevel

    def __str__(self):
        result = "Planet: " + self.planetName + ", Location: " + str(self.location) + ", Tech Level: " + self.techLevel
    def __repr__(self):
        result = "Planet: " + self.planetName + ", Location: " + str(self.location) + ", Tech Level: " + self.techLevel
    def serializePlanet(self):
        planetDict = {
            'planetName' : self.planetName,
            'location' : self.location.serializeLocation(),
            'techLevel' : self.techLevel
        }
        return planetDict


        return result
