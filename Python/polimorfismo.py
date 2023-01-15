#Polimorfismo
#rueda tiene diferentes valores y mismo nombre en metodo
class Auto:
    rueda = 4
    def desplazamiento(self):
        print('el auto se esta desplazando sobre 4 ruedas')


# A Moto is a thing that has two wheels and can move.
class Moto:
    rueda = 2
    def desplazamiento(self):
        print('la moto se esta desplazando sobre 2 ruedas')
