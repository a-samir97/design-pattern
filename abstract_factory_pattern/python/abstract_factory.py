class Frog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} says Croak'

    def __str__(self):
        return self.name


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} says Woof'

    def __str__(self):
        return self.name


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} says Meow'

    def __str__(self):
        return self.name


class Duck:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} says Quack'

    def __str__(self):
        return self.name


# Path: abstract_factory_pattern/python/abstract_factory.py
class PetShop:
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print(f'We have a lovely {pet}')
        print(f'It says {pet.speak()}')
        print(f'We also have {self.pet_factory.get_food()}')


# Path: abstract_factory_pattern/python/abstract_factory.py
class DogFactory:
    def get_pet(self):
        return Dog('Dog')

    def get_food(self):
        return 'Dog Food'


class CatFactory:
    def get_pet(self):
        return Cat('Cat')

    def get_food(self):
        return 'Cat Food'


class DuckFactory:
    def get_pet(self):
        return Duck('Duck')

    def get_food(self):
        return 'Duck Food'


class FrogFactory:
    def get_pet(self):
        return Frog('Frog')

    def get_food(self):
        return 'Frog Food'


if __name__ == '__main__':
    shop = PetShop(DogFactory())
    shop.show_pet()
    print('\n')
    shop = PetShop(CatFactory())
    shop.show_pet()
    print('\n')
    shop = PetShop(DuckFactory())
    shop.show_pet()
    print('\n')
    shop = PetShop(FrogFactory())
    shop.show_pet()
