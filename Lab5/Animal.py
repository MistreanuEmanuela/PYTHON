import copy


class Animal:
    def __init__(self, name, age, color, habitat):
        self._name = name
        self._age = age
        self._color = color
        self._habitat = habitat

    def eat(self):
        pass

    def move(self):
        pass

    def lay_eggs(self):
        pass

    def give_birth(self):
        pass

    def hibernate(self):
        pass

    def get_info(self):
        print(f"{self._name} lives in {self._habitat}")


class Mammal(Animal):
    def __init__(self, name, age, color, habitat, hibernate, food):
        super().__init__(name, age, color, habitat)
        self._hibernate = hibernate
        self._food = food

    def hibernate(self):
        if self._hibernate:
            return True
        return False

    def give_birth(self):
        return True

    def lay_eggs(self):
        return False

    def eat(self):
        x = copy.deepcopy(self._food)
        return x

    def move(self):
        return "In 4 legs"


class Bird(Animal):
    def __init__(self, name, age, color, habitat, wing_span, emigrate, fly):
        super().__init__(name, age, color, habitat)
        self.wing_span = wing_span
        self._emigrate = emigrate
        self._fly = fly

    def lay_eggs(self):
        return True

    def hibernate(self):
        return False

    def give_birth(self):
        return False

    def eat(self):
        food = ['seeds',  'insects',   'fruits',  'insects',  'nectar', 'fish', 'plankton']
        return food

    def move(self):
        if self._fly:
            return "It can fly or walk"
        else:
            return "It can only walk"

    def emigrate(self):
        if self._emigrate:
            return True
        return False


class Fish(Animal):
    def __init__(self, name, age, color, habitat, predator, scaly):
        super().__init__(name, age, color, habitat)
        self._predator = predator
        self._scaly = scaly

    def eat(self):
        if self._predator:
            return ['fish']
        else:
            return ['small plants from water']

    def move(self):
        return "It can swim"

    def lay_eggs(self):
        return True

    def give_birth(self):
        return False

    def hibernate(self):
        return False

    def scaly(self):
        if self._scaly:
            return "It has scaly on its body"
        else:
            return "It hasn't scaly on its body, only a smooth skin "


lion = Mammal(name="Simba", age=5, color="maro", habitat="savana", hibernate=False, food=["carne"])

eagle = Bird(name="vultur", age=3, color="maro", habitat="Munti", wing_span=2.5, emigrate=True, fly=True)

shark = Fish(name="rechin", age=8, color="albastru", habitat="Ocean", predator=True, scaly=True)


print("--------------------------------------------------------------")
lion.get_info()
print("Hibernează:", lion.hibernate())
print("Face pui:", lion.give_birth())
print("Se ouă:", lion.lay_eggs())
print("Ce mănâncă:", lion.eat())
print("Cum se mișcă:", lion.move())


print("--------------------------------------------------------------")
eagle.get_info()
print("Se ouă:", eagle.lay_eggs())
print("Hibernează:", eagle.hibernate())
print("Face pui:", eagle.give_birth())
print("Ce mănâncă:", eagle.eat())
print("Cum se mișcă:", eagle.move())
print("Emigrează:", eagle.emigrate())


print("--------------------------------------------------------------")
shark.get_info()
print("Ce mănâncă:", shark.eat())
print("Cum se mișcă:", shark.move())
print("Se ouă:", shark.lay_eggs())
print("Face pui:", shark.give_birth())
print("Hibernează:", shark.hibernate())
print("Tipul de solzi:", shark.scaly())
