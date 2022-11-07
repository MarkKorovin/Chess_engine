class Gun:
    def __init__(self, model):
        self.model = model
 
    def __repr__(self):
        return self.model
 
    def get_model(self):
        return self.model
 
class Shop:
 
    def __init__(self, name):
        self.name = name
        self.guns = []
 
    def add_gun(self, gun):
        self.guns.append(gun)
 
    def get_guns(self):
        return self.guns
 
if __name__ == '__main__':
    shop = Shop('Qwerty')
    shop.add_gun(Gun('Gun0'))
    shop.add_gun(Gun('Gun1'))
    shop.add_gun(Gun('Gun2'))
    print(shop.get_guns())
