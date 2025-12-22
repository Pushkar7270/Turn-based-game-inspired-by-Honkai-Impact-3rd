from dataclasses import asdict

import File_handler as fh
from Entites import Entity, Move

kiana_moveset = [
    Move(
        name="Basic Attack",
        damage=440,
        pp=-1,
    ),
    Move(
        name="Subspace Lance",
        damage=490,
        pp=10,
    ),
    Move(
        name="Neko Charm",
        damage=500,
        pp=10,
    ),
    Move(
        name="Shamash Unleashed",
        damage=800,
        pp=5,
    ),
]


kiana = Entity(
    name="Kiana Kaslana",
    hp=5600,
    moves=kiana_moveset,
    crit_rate=4,
    speed=4,
    defence=2,
    playable=True,
)
mei_moveset = [
    Move(
        name="Basic Attack",
        damage=350,
        pp=-1,
    ),
    Move(
        name="Searing slash",
        damage=400,
        pp=10,
    ),
    Move(
        name="7 Thunders:Rumble",
        damage=500,
        pp=10,
    ),
    Move(
        name="Fate cutter",
        damage=780,
        pp=5,
    ),
    Move(name="Fate cutter", damage=780, pp=5),
]

mei = Entity(
    name="Mei",
    hp=5500,
    moves=mei_moveset,
    crit_rate=3,
    speed=4,
    defence=3,
    playable=True,
)
bronya_moveset = [
    Move(
        name="Basic Attack",
        damage=550,
        pp=-1,
    ),
    Move(
        name="Cognitive destruction",
        damage=400,
        pp=10,
    ),
    Move(name="Selene", damage=570, pp=10),
    Move(name="Quasi-black hole", damage=800, pp=5),
]


bronya = Entity(
    name="Bronya",
    hp=6000,
    moves=bronya_moveset,
    crit_rate=3,
    speed=2,
    defence=5,
    playable=True,
)

sa_moveset = [
    Move(
        name="Basic Attack",
        damage=350,
        pp=-1,
    ),
    Move(name="Matter erasure", damage=400, pp=-1),
    Move(name="Time acceleration", damage=650, pp=-1),
    Move(name="Power of Samsara", damage=850, pp=-1),
]


sa_boss = Entity(
    name="Sa",
    hp=9000,
    moves=sa_moveset,
    crit_rate=1,
    speed=3,
    defence=3,
    playable=False,
)


game_data = {
    "characters": [asdict(kiana), asdict(mei), asdict(bronya)],
    "boss": [asdict(sa_boss)],
}
arranged_game_data = {
    "Characters": [char for char in game_data["characters"]],
    "Boss": [bosss for bosss in game_data["boss"]],
}
fh.save_data(arranged_game_data, "Characters.json")
