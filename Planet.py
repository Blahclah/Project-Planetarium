class Planet(object):
    
    names = ["Mercury","Venus", "Earth", "Mars","Jupiter","Saturn", "Uranus", "Neptune","Pluto"]
    sizes = ['1,516','3,760.4','3,958.8','2,106.1','43,441','36,184','15,759','15,299','738.38']
    distances = ['33.7','66.868','92.041','142.09','484.25','930.45','1,841.6','2,781.9','3,670']
    
    def __init__(self, name, size,distance):
        self.nameIndex = name
        self.sizeIndex = size
        self.distanceIndex = distance
        

    def __str__(self):
        
        name = Planet.names[self.nameIndex]
        size = Planet.sizes[self.sizeIndex]
        distance = Planet.distances[self.distanceIndex]
        return  name+": Planet size: " + size+" miles; Distance from the sun: " + distance+ " million miles."


        
