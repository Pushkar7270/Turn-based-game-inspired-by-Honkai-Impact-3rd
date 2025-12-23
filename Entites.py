from dataclasses import dataclass, field


# dataclass is a decorator (the @ symbol thing) that lives in Python's standard library. It
@dataclass
class Move:
    name: str
    damage: int
    pp: int  # number of turns for a special attacks
    max_pp: int = field(init=False)

    def __post_init__(self):
        self.max_pp = self.pp


@dataclass
class Entity:  # __init__ method is created in the background because of dataclass
    name: str
    hp: int
    max_hp: int = field(init=False)
    moves: list[Move]
    crit_rate: int
    speed: int
    defence: int
    playable: bool = False
    image_path: str = "asset/default.png"

    @property  # This is a decorator that allows you to define a method that can be accessed like an attribute.
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def __post_init__(
        self,
    ):  # This is a special method that is called after the __init__ method. It is used to initialize the attributes of the class.
        self.max_hp = self.hp

    def take_damage(self, damage: int):
        self.hp -= damage
        print(f"{damage} was dealt")
        if self.hp < 0:
            self.hp = 0
