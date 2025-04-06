class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

        if self.health <= 0:
            self.__class__.alive.remove(self)

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def __repr__(cls) -> str:
        return f"[{', '.join(str(animal) for animal in cls.alive)}]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herb: Herbivore) -> None:
        if isinstance(herb, Herbivore) and not herb.hidden:
            herb.health -= 50
