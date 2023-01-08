from account import Account

class Driver(Account):
    email = str
    model = str
    
    def __init__(self, name, document, email, password):
        super().__init__(name, document)
        self.email = email
        self.model = model