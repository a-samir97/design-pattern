class Burger:
    def __init__(self, size):
        self.size = size
        self.cheese = None
        self.tomato = None
        self.spicy = None

    def __str__(self):
        info = (f"Burger Size: {self.size}",
                f"Cheese: {self.cheese}",
                f"tomato: {self.tomato}",
                f"Spicy: {self.spicy}")
        return "\n".join(info)


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger("Medium")

    def add_cheese(self):
        self.burger.cheese = "Yes"

    def add_tomato(self):
        self.burger.tomato = "Yes"

    def add_spicy(self):
        self.burger.spicy = "Yes"


class BurgerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.add_cheese()
        self.builder.add_tomato()
        self.builder.add_spicy()


def main():
    builder = BurgerBuilder()
    director = BurgerDirector(builder)
    director.construct()
    print(builder.burger)


if __name__ == "__main__":
    main()
