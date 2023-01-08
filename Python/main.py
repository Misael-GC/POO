from car import Car
from account import Account
from user import User

if __name__ == "__main__":
    print('Hola mundo')


    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))
    
    print('User')
    users = User('name', 'document', 'email', 'password')
    print(vars(users))
