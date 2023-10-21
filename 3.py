#a = ["ananas", "apple", "peach", "candy", "pear", "maracuja", "lemon", "sweets"]
#print(a)
#for i in a:
    #if i == "candy" or i == "sweets":
       # a.remove(i)
#print(a)
class Animals:
    def __init__(self, name,type,weight):
        self.name = name
        self.type = type
        self.weight = weight
        print(self.name, self.type, self.weight)
dog = Animals(name="Mia", type="Dog", weight= 5)
cat = Animals(name="Ji", type="Cat",weight= 3)
parrot = Animals(name="Chi",type="Perrot",weight= 1)

