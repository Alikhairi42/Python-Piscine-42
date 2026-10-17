
from ex00 import FlameFactory, AquaFactory


def test_factory(factory):
    print("Testing factory")

    base = factory.create_base()
    base.describe()
    print(base.attack())

    evolved = factory.create_evolved()
    evolved.describe()
    print(evolved.attack())

    print()


def test_battle(factory1, factory2):
    print("Testing battle")

    c1 = factory1.create_base()
    c2 = factory2.create_base()

    c1.describe()
    print("vs.")
    c2.describe()

    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    ff = FlameFactory()
    af = AquaFactory()

    test_factory(ff)
    test_factory(af)
    test_battle(ff, af)
