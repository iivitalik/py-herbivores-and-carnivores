class Animal:
    alive = []
    def __init__(
            self,
            health: int=100,
            name: str=None,
            hidden: bool=False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.__class__.alive.append(self)

    def take_damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            self.__class__.alive.remove(self)


class Herbivore(Animal):
    def hide(self, name: str) -> None:
        self.name = name
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herb : Herbivore) -> None:
        if not herb.hidden and isinstance(herb, Herbivore):
            herb.health -= 50
        if herb.health <= 0:
            Animal.alive.remove(herb)




