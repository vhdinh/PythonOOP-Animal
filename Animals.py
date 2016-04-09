class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        # print self.health
        return self

    def run(self):
        self.health -=5
        # print self.health
        return self

    def displayHealth(self):
        # print 'Name: ', self.name, ' Health: ', self.health
        print 'Name: %s \nHealth: %s' %(self.name,self.health)
        return self


class Dog(Animal):
    def __init__(self,name, health = 150):
        super(Dog,self).__init__(self)
        self.name = name
        self.health = health

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon,self).__init__(self)
        self.name = name
        self.health = health

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon"
        return super(Dragon,self).displayHealth()



animal = Animal("Husky").walk().walk().walk().run().run().displayHealth()

dog = Dog("Doggie").walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("Drago").walk().walk().walk().run().run().fly().fly().displayHealth()

dragon.fly("100")