# A class is a blueprint for creating objects (a particular data structure), providing initial values
# for state (member variables or attributes), and implementations of behavior (member functions or
# methods).
#Polimorfismo

# Se crea la clase padre que es Animales, se crean 2 subclases de Leon y perro y despues ya podemos crear diferentes animales 
# a partir de leon y perro
class Animales:
    def __init__(self, name):
        self.name = name
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print('animal salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print('animal domestico')

nuevo_animal = Leon('SIMBA')
nuevo_animal.tipo_animal()


nuevo_animal2 = Perro('Docko')
nuevo_animal2.tipo_animal()

